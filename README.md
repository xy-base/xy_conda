<!--
 * @Author: yuyangit yuyangit.0515@qq.com
 * @Date: 2024-10-18 20:35:49
 * @LastEditors: yuyangit yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-18 20:37:17
 * @FilePath: /xy_conda/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_conda

| [简体中文](./README.md)         | [繁體中文](readme/README.zh-hant.md)        |                      [English](readme/README.en.md)          |
| ----------- | -------------|---------------------------------------|

## 说明
简单Conda工具，提供不同平台conda的安装，加载，备份等功能。

## 源码仓库

| [Github](https://github.com/xy-base/xy_conda.git)         | [Gitee](https://gitee.com/xy-opensource/xy_conda.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_conda.git)          |
| ----------- | -------------|---------------------------------------|


## 安装

```bash
# bash
pip install xy_conda
```

## 使用

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
# 静默安装最新 Miniconda3

xy_conda -w install_pack
# 安装pack包

xy_conda -w load -f python_3_11_3_2024_03_19_20_15_22.tar.gz
# 加载环境包

```

## 许可证
xy_conda 根据 <木兰宽松许可证, 第2版> 获得许可。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

## 捐赠

如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢?  

![Pay-Total](./readme/Pay-Total.png)


## 联系方式

```
微信: yuyangiit
邮箱: yuyangit.0515@qq.com
```