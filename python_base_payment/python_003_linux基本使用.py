# _*_coding :utf-8 _*_
# @Time :2022/6/17 17:53
# @File : python_002_linux基本使用
# @Project : python_base_payment

"""
一、linux和window的区别：
1.Linux开源，window闭源
2.Linux只有一个根目录，window有很多盘


二、linux命令行
1.ubuntu图形界面中的终端（terminal）可以设置默认不进入图形界面（重启后直接进入tty）
  sudo systemctl set-default multi-user.target

2.进入Ubuntu无界面交互模式（纯文本交互模式，控制台console，tty），切换到图形交互界面
  使用 startx 即可

3.恢复默认开机启动图形界面
  sudo systemctl set-default graphical.target（该命令要在图形化界面的终端进行使用，再重启即可）

4.切换到root用户
  root用户的密码是随机的，
  我们可先修改用户密码（使用 sudo passwd），
  在切换到 root （使用 su root）
  在使用修改后的密码


gnome-terminal  打开终端
poweroff  立刻关机
shutdown -h now  立刻关机
shutdown -r now  立刻重启
exit  退出终端
pwd  查找当前所在的目录 /home
who  查看当前系统登录的用户  wufake   :0           2022-06-17 04:30 (:0)
ls  查看当前的所有文件夹







"""



























