<!--
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-18 20:35:42
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-18 20:42:33
 * @FilePath: /xy_conda/readme/README_zh_TW.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_conda

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## 說明
簡單Conda工具，提供不同平臺conda的安裝，載入，備份等功能。

## 程式碼庫

- <a href="https://github.com/xy-base/xy_conda.git" target="_blank">Github位址</a>  
- <a href="https://gitee.com/xy-base/xy_conda.git" target="_blank">Gitee位址</a>

## 安裝

```bash
pip install xy_conda
```

## 使用

###### 1. 命令行
```bash
# 工作方式:
# "backup + [name]" 备份，环境名称可选,
# "install + [url]" 安装 miniconda,
# "install_pack" 安装pack包,
# "load + [name] + [target_path] + [filepath]" 加载环境包, name:conda环境名称, target_path:目标路径, filepath:环境包文件路径,

> xy_conda -w backup
> 是否备份当前环境 python_3_11_3 
> 输入 [Y/n]
> Y

> xy_conda -w backup -n conda_name
> 是否备份当前环境 conda_name
> 输入 [Y/n]
> Y

> xy_conda -w install

> xy_conda -w install conda安装包url

> xy_conda -w install_pack

> xy_conda -w load -f python_3_11_3_2024_03_19_20_15_22.tar.gz

```

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: 845262968@qq.com
```