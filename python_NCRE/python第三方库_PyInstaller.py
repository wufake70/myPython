# _*_coding :utf-8 _*_
# @Time :2022/7/13 21:39
# @File : python第三方库_PyInstaller
# @Project : python_NCRE


"""
pyinstall库是一个将Python语言脚本(.py文件)打包成可执行文件的第三方库，可用于window,linux,
osx 等等操作系统
通过对源文件打包，Python程序可以在没有安装Python的环境中运行，

命令行使用:
1.进入cmd，使用pyinstaller 源文件(即py文件，注意源文件使用绝对或 相对路径)
生成的dist文件夹中 包含着许多 其中双击 exe可执行文件即可

2.可使用 pyinstaller -F 源文件(这两个命令中 路径名或文件名中不得包含中文字符)
生成的dist文件夹中 只用一个exe文件 双击即可运行

3. 将py文件和图片文件 打包成一个带图标的exe文件（必须是 ico后缀）
    pyinstaller –i a.ico –F a.py

4.其他 参数
    -F或--onefile：在dist文件夹中 打包成单个可执行文件。
    -D或--onedir：打包成单个文件夹。
    -n或--name：指定可执行文件的名称。
    -i或--icon：指定可执行文件的图标文件。
    -c获--clean：清除零时文件

5. 敲击任意键退出
    input("enter any key to exit ...")

=======================================================
使用pyinstaller 命令报错集合
1.UPX is not availabl
原因分析：
python环境的Scripts文件夹内缺少了一个upx.exe的文件
解决方案：
到官网https://upx.github.io/中下载一个UPX,
将下载文件解压后得到的upx.exe文件(解压后的所有文件里只要这一个文件即可,其他文件不需要),
将其复制粘贴到python环境的Scripts文件夹中即可解决该问题;

2.TypeError: _get_sysconfigdata_name() missing 1...'check_exists'
这个错误的解决方法是，进入python命令行模式，然后依次执行如下两行命令：
import sysconfig
print(sysconfig.__file__)
执行后你可以获得sysconfig.py这个文件的路径，打开它，
然后找到里面的_get_sysconfigdata_name函数，
将其中的check_exists参数默认值设置为True。
即_get_sysconfigdata_name(check_exists=True)。
然后保存，再去运行打包命令，就可以了。

3.RuntimeError: No metadata path found for distribution ‘greenlet‘
解决方法一
遇到这种问题直接卸载原来的重装但是这个重装会
    ERROR: Cannot uninstall ‘greenlet’. It is a distutils installed
    project and thus we cannot accurately determine which files belong to
    it which would lead to only a partial uninstall.
然后你可以根据重装的地址找到这个文件的地方删除就好了。
方法二
输入：pip  install --ignore-installed greenlet

4.打包成exe文件后，双击exe文件 出现闪退
    进入cmd 启动该exe文件 ，可以查看 其报错情况
列如: ModuleNotFoundError: No module named 'docx'
出现该bug 是因为python中 未安装 相关的docx模块 即在打包时
未能将 该模块导入成功

注意事项: 打包时 注意 源文件中模块导入就， 尽量导入 使用的 相关模块的相关函数 即可
避免打包出来的exe文件 容量 过于庞大
列如: from time import sleep 从time模块中sleep函数 就不用加载整个time模块
    注意： 上式 导入后 直接使用sleep（）调用 ，不需要time.sleep()调用


"""






































