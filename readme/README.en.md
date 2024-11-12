<!--
 * @Author: yuyangit yuyangit.0515@qq.com
 * @Date: 2024-10-18 20:35:42
 * @LastEditors: yuyangit yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-18 20:41:15
 * @FilePath: /xy_conda/readme/README.en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_conda

| [简体中文](../README.md)         | [繁體中文](./README.zh-hant.md)        |                      [English](./README.en.md)          |
| ----------- | -------------|---------------------------------------|

## Description
Simple Conda tool that provides installation, loading, backup and other functions of conda on different platforms.

## Source Code Repositories

| [Github](https://github.com/xy-base/xy_conda.git)         | [Gitee](https://gitee.com/xy-opensource/xy_conda.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_conda.git)          |
| ----------- | -------------|---------------------------------------|

## Installation

```bash
# bash
pip install xy_conda
```

## How to use

```bash
# bash
# 工作方式:
# "backup + [name]" 备份，环境名称可选,
# "download" 下载最新 Miniconda3 安装包到当前目录下
# "install" 安装最新的 Miniconda3,
# "install_b" 静默安装最新版本 Miniconda3, 默认安装路径到~/Miniconda3, 相当于 sh ./Miniconda3-安装包.sh -b
# "install_pack" 安装pack包,
# "load + [name] + [target_path] + [filepath]" 加载环境包, name:conda环境名称, target_path:目标路径, filepath:环境包文件路径,

xy_conda -w backup
# 是否备份当前环境 python_3_11_3 
# 输入 [Y/n]
# Y

xy_conda -w backup -n conda_name
# 是否备份当前环境 conda_name
# 输入 [Y/n]
# Y

xy_conda -w download
# 下载 Miniconda3 最新安装包

xy_conda -w install
# 安装 Miniconda3

xy_conda -w install_b
# 安装 Miniconda3

xy_conda -w install_pack
# 安装pack包

xy_conda -w load -f python_3_11_3_2024_03_19_20_15_22.tar.gz
# 加载环境包

```

## License
xy_conda is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```