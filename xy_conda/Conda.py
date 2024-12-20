# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Conda"
"""
  * @File    :   Conda.py
  * @Time    :   2023/06/03 08:10:08
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, Ship of Ocean
  * @Desc    :   None
"""

import os
import platform
from pathlib import Path
from datetime import datetime


class Conda:
    def conda_install_url(self, system_name, machine, suffix):
        if (
            not isinstance(system_name, str)
            or len(system_name) <= 0
            or not isinstance(machine, str)
            or len(machine) <= 0
            or isinstance(suffix, str)
            or len(suffix) <= 0
        ):
            return None
        return f"https://repo.anaconda.com/miniconda/Miniconda3-latest-{system_name}-{machine}.{suffix}"

    @property
    def default_conda_install_url(self) -> str:
        system_name = platform.system()
        machine = platform.machine()
        url_format = "https://repo.anaconda.com/miniconda/Miniconda3-latest-{system_name}-{machine}.{suffix}"
        if system_name.lower() == "windows":
            return url_format.format(
                system_name=system_name,
                machine="machine",
                suffix="exe",
            )
        elif system_name.lower() == "darwin":
            return url_format.format(
                system_name="MacOSX",
                machine=machine,
                suffix="sh",
            )
        return url_format.format(
            system_name=system_name,
            machine=machine,
            suffix="sh",
        )

    def base_conda_path(self):
        conda_exe_path_text = os.environ.get("CONDA_EXE")
        if conda_exe_path_text:
            conda_exe_path = Path(conda_exe_path_text)
            return (
                conda_exe_path.parent.parent
                if conda_exe_path.exists() and conda_exe_path.parent.parent
                else None
            )
        return None

    def envs_path(self):
        base_conda_path = self.base_conda_path()
        if base_conda_path:
            env_path = base_conda_path.joinpath("envs")
            if env_path and env_path.exists() and env_path.is_dir():
                return env_path
        return None

    def env_exists(self, name) -> bool:
        exists = False
        envs_path = self.envs_path()
        if envs_path and name and (isinstance(name, str) or isinstance(name, Path)):
            env_path = envs_path.joinpath(name)
            return env_path.exists() and env_path.is_dir()
        return exists

    def output_file_name(self, name) -> str:
        file_name_suffix = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return f"{name}_{file_name_suffix}.tar.gz"

    def command(self, name) -> str:
        output_file_name = self.output_file_name(name)
        return f"conda pack -n {name} -o {output_file_name}"

    def current_conda(self):
        return os.environ.get("CONDA_DEFAULT_ENV")

    def backup(self, name) -> bool:
        command = self.command(name)
        return os.system(command) == 0

    def link(
        self,
        source: Path,
        target: Path,
        password: str,
    ) -> bool:
        if (
            not isinstance(source, Path)
            or not source.exists()
            or not isinstance(target, Path)
            or not target.exists()
        ):
            return False
        password_text = ""
        if isinstance(password, str) and len(password) > 0:
            password_text = f"echo {password} | sudo -S "
        cmd = f"{password_text}cp -rf{source} {target}"
        return os.system(cmd) == 0

    def download(self) -> bool:
        if not os.access(Path.cwd(), os.W_OK):
            return False
        wget_result = os.system(f"wget {self.default_conda_install_url}") == 0
        if not wget_result:
            return False
        else:
            return True

    def install(self) -> bool:
        if not os.access(Path.cwd(), os.W_OK):
            print("当前工作目录没有写入权限")
            return False
        install_cmd = f"sh {Path(self.default_conda_install_url).name}"
        conda_install_package_path = Path(Path(self.default_conda_install_url).name)
        if conda_install_package_path.exists() and conda_install_package_path.is_file():
            sh_result = os.system(
                install_cmd,
            )
            return sh_result == 0
        wget_result = os.system(f"wget {self.default_conda_install_url}") == 0
        if not wget_result:
            return False
        else:
            sh_result = os.system(
                install_cmd,
            )
            return sh_result == 0

    def install_b(self) -> bool:
        if not os.access(Path.cwd(), os.W_OK):
            print("当前工作目录没有写入权限")
            return False
        install_cmd = f"sh {Path(self.default_conda_install_url).name} -b"
        conda_install_package_path = Path(Path(self.default_conda_install_url).name)
        print(f"conda_install_package_path {conda_install_package_path.resolve()} {os.access(conda_install_package_path, os.X_OK)} = {os.access(conda_install_package_path.as_posix(), os.X_OK)}")
        if conda_install_package_path.exists() and conda_install_package_path.is_file():
            sh_result = os.system(
                install_cmd,
            )
            return sh_result == 0
        wget_result = os.system(f"wget {self.default_conda_install_url}") == 0
        if not wget_result:
            print(f"下载文件失败，url = {self.default_conda_install_url}")
            return False
        else:
            sh_result = os.system(
                install_cmd,
            )
            return sh_result == 0

    def install_pack(self) -> bool:
        cmd = "conda install -c conda-forge conda-pack -y"
        return os.system(cmd) == 0
