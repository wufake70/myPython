#!/bin/bash
# 此文档可以配置python开发环境，仅适用于Ubuntu，并在18服务器版通过测试！

# 版本号
VERSION=12
# 获取当前路径
THISPATH=`pwd -P`
# 获取当前所在文件夹
DIRNAME=`basename $THISPATH`
# 获取当前登录用户
USERNAME=`logname`
echo -e "\033[46;5m 当前登录用户为:$USERNAME  \033[0m"

## 获取版本号
function version(){
  return $VERSION
}

## xxxxxxx更新当前脚本xxxx 需要修改此函数，防止被迫修改脚本
function update_shell(){
  echo "hello shell"
  # sudo apt install -y curl
  # curl -fsSL https://gitee.com/ConnerClem/PythonEnv/raw/master/configure.sh|bash -s -- -v
  # if [ $? -ne $VERSION ]; then
  #   if [ $DIRNAME = "PythonEnv" ]; then
  #     git fetch --all
  #     git reset --hard origin/master
  #     git pull
  #     echo -e "\033[46;5m 脚本更新完成 \033[0m"
  #     curl -fsSL https://gitee.com/ConnerClem/PythonEnv/raw/master/configure.sh|bash
  #     exit 0
  #   else
  #     git clone https://gitee.com/ConnerClem/PythonEnv.git $HOME/PythonEnv
  #     cd $HOME/PythonEnv
  #     sudo bash configure.sh
  #     exit 0
  #   fi
  # fi
}

## 更换apt源为阿里源,此源适用于Ubuntu18.04
function change_apt_sources() {
  echo -e "\033[46;5m 开始执行换源 \033[0m"
  sudo grep -q "aliyun" /etc/apt/sources.list
  if [ $? -ne 0 ]; then
    sudo cp /etc/apt/sources.list > /etc/apt/sources.list.bak
    sudo echo "
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
" > /etc/apt/sources.list
  fi
  echo -e "\033[46;5m 换源完成 \033[0m"
}

## 软件更新
function update_apt(){
  echo -e "\033[46;5m 开始更新系统 \033[0m"
  sudo apt -y  update   # 更新源
  sudo dpkg --configure -a
  sudo apt -y  upgrade  # 更新已安装的包
  sudo apt -y  dist-upgrade  # 升级系统
  # 注意以上安装过程中出现的安装选项，直接回车或者选择yes即可
  sudo apt-get -y  autoremove
  sudo apt -y autoclean
  echo -e "\033[46;5m 更新结束 \033[0m"
}

## 安装Python相关的环境
function install_python() {
  echo -e "\033[46;5m 开始安装Python \033[0m"
  ## 安装pip
  sudo apt install -y python3-pip
  sudo apt install -y python-pip

  ## 安装虚拟环境对应的包
  sudo pip list | grep virtualenvwrapper
  if [ $? -ne 0 ]; then
    sudo pip3 install -i https://pypi.douban.com/simple  virtualenv
    sudo pip  install -i https://pypi.douban.com/simple  virtualenvwrapper
    sudo pip3 install -i https://pypi.douban.com/simple  virtualenvwrapper
  fi
  ## 配置虚拟环境
  envdir="$HOME/.virtualenvs"
  if [ ! -d "$envdir" ]; then
    mkdir "$envdir"
  else
    echo "$envdir is already exist !!!"
  fi

  grep -q "WORKON_HOME" ~/.bashrc
  if [ $? -ne 0 ]; then
    echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
  fi

  sh ~/.bashrc
  ## 创建虚拟环境
  . /usr/local/bin/virtualenvwrapper.sh
  if [ ! -d $HOME/.virtualenvs/py3env ]; then
    mkvirtualenv -p /usr/bin/python3 py3env
    deactivate
    echo -e "\033[46;5m Python虚拟环境安装完成 \033[0m"
  fi

  grep -q "workon" $HOME/.bashrc
  if [ $? -ne 0 ]; then
    echo "workon py3env" >> $HOME/.bashrc
  fi
  echo -e "\033[46;5m Python安装结束 \033[0m"
}


## 安装MySQL
function install_mysql(){
  echo -e "\033[46;5m 开始安装Mysql \033[0m"
  ## 安装mysql必须的模块，安装完成之后会自动启动mysql
  sudo apt install -y mysql-server
  ## 停止mysql服务
  sudo systemctl stop  mysql.service
  ## 修改mysql配置文件。修改远程连接IP地址，修改成任意地址可以连接；修改编码为utf8
  sudo sed -i 's/127.0.0.1/0.0.0.0/g' /etc/mysql/mysql.conf.d/mysqld.cnf
  grep -q 'default-character-set' /etc/mysql/mysql.conf.d/mysqld.cnf
  if [ $? -ne 0 ]; then
    sudo sed -i "/nice/a\[client]\ndefault-character-set=utf8\n" /etc/mysql/mysql.conf.d/mysqld.cnf
    sudo sed -i "/server-key/a\character_set_server=utf8" /etc/mysql/mysql.conf.d/mysqld.cnf
  fi
  ## 启动mysql服务
  sudo systemctl start  mysql.service
  ### 修改mysql root 密码
  grep -q 'skip-grant-tables' /etc/mysql/mysql.conf.d/mysqld.cnf
  if [ $? -ne 0 ]; then
    sudo sed -i "/character_set_server=utf8/a\skip-grant-tables" /etc/mysql/mysql.conf.d/mysqld.cnf
    sudo systemctl restart  mysql.service
  fi
  sudo systemctl restart  mysql.service
  ## 修改mysql root密码为：Root123
  mysql << EOF
update mysql.user set authentication_string=password('Root123') where user='root' and Host ='localhost';
update mysql.user set plugin='mysql_native_password';
flush privileges ;
EOF
  sudo systemctl restart  mysql.service

  grep -q 'skip-grant-tables' /etc/mysql/mysql.conf.d/mysqld.cnf
  if [ $? -ne 1 ]; then
    sudo sed -i "/skip-grant-tables/d" /etc/mysql/mysql.conf.d/mysqld.cnf
    sudo systemctl restart  mysql.service
  fi
  ## 添加管理员用户admin，密码为：qwe123
  mysql -uroot -pRoot123<< EOF
CREATE USER 'admin'@'%' IDENTIFIED BY 'qwe123';
GRANT ALL  ON *.* TO 'admin'@'%';
FLUSH PRIVILEGES;
EOF
  echo -e "\033[46;5m 安装配置Mysql完成 \033[0m"
}


## 安装MongoDB
function install_mongodb(){
  echo -e "\033[46;5m 开始安装MongoDB \033[0m"
  sudo apt -y install mongodb
  echo -e "\033[46;5m MongoDB安装完成 \033[0m"
}

## 查看是否存在vim，不存在则安装vim
function install_vim(){
  echo -e "\033[46;5m 开始安装VIM \033[0m"
  vimtest=`which vim`
  if [ -n $vimtest ]; then
    sudo apt -y install vim
  fi
  echo -e "\033[46;5m VIM安装完成 \033[0m"
}

## 判断网络情况，下载速度可以的话，就会下载vim插件
function test_Network_speed(){
  all=0
  ## 取5次测速的平均值
  for i in {1..5}
  do
    speed=`curl -o /dev/null -w %{time_total}"\n" "$1"`
    all=$(echo "$all+$speed" | bc)
  done
  avg=$(echo "$all/5" | bc)
  return $avg
}

function install_vim_plugin(){
  test_Network_speed https://spacevim.org/install.sh
  if [ $? -le 3 ];then
    echo -e "\033[46;5m 开始安装VIM插件 \033[0m"
    ## 注意配置vim有两种方法，默认使用第一种 如果使用的是阿里云服务器，并且内存小于 1G，那么建议使用第一种
    ## 配置vim 方法一： 适用SpaceVim 网址： https://spacevim.org/
    sudo apt -y install git
    sudo apt -y install curl
    curl -sLf https://spacevim.org/install.sh | bash
    if [ -f $HOME/.SpaceVim.d/init.toml ]; then
      # sed -i "s/gruvbox/colorscheme/" $HOME/.SpaceVim.d/init.toml
      sed -i 's/enable_guicolors = true/enable_guicolors = false/g' $HOME/.SpaceVim.d/init.toml
      grep -q "lang#python" $HOME/.SpaceVim.d/init.toml
      if [ $? -ne 0 ]; then
        sed -i '$a[[layers]]\n  name = "lang#python"'  $HOME/.SpaceVim.d/init.toml
      fi
    fi
    yes ""| vim +SPInstall +qall

    ### ### 配置vim 方法二 使用此方法时需要卸载SpaceVim
    ### Spacevim 卸载命令
    ### mv ./.vimrc_back $dirname
    ### curl -sLf https://spacevim.org/install.sh | bash -s -- --uninstall
    ### vundledir="$HOME/.vim/bundle/Vundle.vim"
    ### if [ ! -e "$vundledir" ]; then
    ###   echo "DownLoad Vundle.vim ..."
    ###   git clone https://github.com/VundleVim/Vundle.vim.git $HOME/.vim/bundle/Vundle.vim
    ### fi
    ### yes "" |vim +PluginInstall +qall
    ### cd $HOME/.vim/bundle/YouCompleteMe
    ### # 安装扩展
    ### sudo apt -y install git cmake  clang  python3-dev
    ###
    ### # 编译安装YouCompleteMe
    ### ./install.sh --clang-completer --system-libclang
    echo -e "\033[46;5m VIM插件安装完成 \033[0m"
  fi
}



## 配置开机启动界面
function change_motd(){
  grep -q "MySQL" /etc/motd
  if [ $? -ne 0  ]; then
    sudo echo "
┌────────────────────────────────────────────────────────────┐
│                                                            │
│                               ▄▄                           │
│                       ██      ██                           │
│ ██▄███▄   ▀██  ███  ███████   ██▄████▄   ▄████▄   ██▄████▄ │
│ ██▀  ▀██   ██▄ ██     ██      ██▀   ██  ██▀  ▀██  ██▀   ██ │
│ ██    ██    ████▀     ██      ██    ██  ██    ██  ██    ██ │
│ ███▄▄██▀     ███      ██▄▄▄   ██    ██  ▀██▄▄██▀  ██    ██ │
│ ██ ▀▀▀       ██        ▀▀▀▀   ▀▀    ▀▀    ▀▀▀▀    ▀▀    ▀▀ │
│ ██         ███                                             │
│                                                            │
│       MySQL:                                               │
│            用户        密码                                │
│            root      Root123                               │
│            admin     qwe123                                │
└────────────────────────────────────────────────────────────┘
  " >> /etc/motd
  fi
}

## 安装拓展包
function install_other(){
  sudo apt-get -y install lrzsz sl fortune fortune-zh cowsay lolcat screen toilet figlet openssh-server
  sudo apt -y  install python-flake8 python3-flake8 flake flake8

  grep -q "cowsay" $HOME/.bashrc
  if [ $? -ne 0 ]; then
    echo "fortune-zh |cowsay -f elephant|lolcat" >> $HOME/.bashrc
  fi
  service sshd restart
}

## 安装 Redis
function install_redis(){
  echo -e "\033[46;5m 开始安装Redis \033[0m"
  ## 安装redis
  sudo apt -y install redis-server
  ## 修改配置文件
  sudo sed -i 's/bind 127.0.0.1 ::1/bind 0.0.0.0/g' /etc/redis/redis.conf
  sudo sed -i 's/127.0.0.1 ::1/0.0.0.0/g' /etc/redis/redis.conf
  sudo sed -i 's/127.0.0.1/0.0.0.0/g' /etc/redis/redis.conf
  sudo /etc/init.d/redis-server restart
  echo -e "\033[46;5m Redis安装完成 \033[0m"
}

## 将用户家目录下所有文件赋权给当前用户
function change_power(){
  sudo chown -R $USERNAME:$USERNAME $HOME
}

## 调用函数
function main(){
  if [ $# -gt 0 ]
  then
    case $1 in
      --version|-v)
        version
        exit $?
        ;;
      --update|-u)
        update_shell    ## 更新当前shell脚本
        change_apt_sources  ## 更换源
        update_apt      ## 更新系统
        exit 0
        ;;
      --python|-p)
        install_python  ## 安装与配置python
        exit 0
        ;;
      --mysql|-m)
        install_mysql   ## 安装与配置mysql
        exit 0
        ;;
      --mongodb|-mongo)
        install_mongodb ## 安装与配置mongodb
        exit 0
        ;;
      --vim|-vim)
        install_vim     ## 安装vim
        exit 0
        ;;
      --vim_plugin|-vp)
        install_vim     ## 安装vim插件
        exit 0
        ;;
      --other|-o)
        install_other   ## 安装杂项软件包
        change_power    ## 更改之前安装的所有文件的权限
        exit 0
        ;;
      --redis|-r)
        install_redis   ## 安装与配置redis
        exit 0
	      ;;
      --change|-c)
        change_power    ## 更改之前安装的所有文件的权限
        exit 0
        ;;
      --install|-i)
        update_shell    ## 更新当前shell脚本
        change_apt_sources  ## 更换源
        update_apt      ## 更新系统
        install_python  ## 安装与配置python
        install_mysql   ## 安装与配置mysql
        install_mongodb ## 安装与配置mongodb
        install_vim     ## 安装vim
        install_vim_plugin  ## 安装vim 插件
        change_motd     ## 配置启动界面
        install_other   ## 安装杂项软件包
        install_redis   ## 安装与配置redis
        change_power    ## 更改之前安装的所有文件的权限
        exit 0
        ;;
    esac
  else
    update_shell    ## 更新当前shell脚本
    change_apt_sources  ## 更换源
    update_apt      ## 更新系统
    install_python  ## 安装与配置python
    install_mysql   ## 安装与配置mysql
    install_mongodb ## 安装与配置mongodb
    install_vim     ## 安装vim
    install_vim_plugin  ## 安装vim 插件
    change_motd     ## 配置启动界面
    install_other   ## 安装杂项软件包
    install_redis   ## 安装与配置redis
    change_power    ## 更改之前安装的所有文件的权限
    echo -e "\033[43;34m 脚本执行完成！！！ \033[0m"
  fi
}

main $@

