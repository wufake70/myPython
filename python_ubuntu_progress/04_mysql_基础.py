# _*_coding :utf-8 _*_
# @Time :2022/7/22 17:00
# @File : MySQL_001_基础
# @Project : python_ubuntu_progress

"""
一、MySQL 介绍
    1.数据库概念
        （1）基本概念：
            数据库就类型与 一个文件夹，里面存放了很多Excel表格，
            但是数据库是专门用来管理数据的软件，所以效率要远高于excel
            或者文本的存储方式。

        （2)数据管理系统（Data-Management System DBMS)
            由一个相互关联的数据的集合和一组用以访问这些数据的程序组成。
            这个数据集合通常称作 数据库（database）

        (3)关系型数据库
            关系型数据库 基于关系模型，使用一系列表 来表达数据以及这些数据之间的
            关系。MySQL就是关系型数据库。关系型已经成为当今主要的数据模型。
            只存储 复杂的 数据

        (4)非关系型数据库
            数据 与 数据 没有联系
            redis、mongodb
            只存储 简单 数据

    2.MySQL初步了解
        (1)MySQL 配置文件
            乌班图上通过 apt 安装MySQL 配置文件目录 是
            /etc/mysql/mysql.conf.d
            port = 3306 （默认端口)

        (2)登录到MySQL
            本地连接:
            mysql -u用户名 -p  （常用）
            密码

            远程连接
            mysql -hIP地址 -p端口(port) -u用户 -p
            密码

            注意 1.使用 quit 退出 MySQL中不区分大小写, 命令之后要用 分号 “；”结尾
                2.Type 'help;' or '\h' for help.
                \h 获取帮助
                2.Type '\c' to clear the current input statement.
                \c 清屏

    3.查看MySQL 服务
        linux 上 通过:
        service mysql status/start/stop
        查看状态/启动该服务/停止该服务

        windows 下通过 任务管理器查看

    4.查看数据库（相当于 文件夹）
        查看有哪些数据库s:       SHOW DATABASES;
        +--------------------+
        | Database           |
        +--------------------+
        | information_schema |
        | mysql              |
        | performance_schema |
        | sys                |
        +--------------------+

        进入某个数据库：        USE mysql;
        返回 Database changed

        判断在那个数据库里： SELECT DATABASE();

        查看当前的用户:         SELECT user();
        admin

        注意要写 分号 ";"

二、数据库(DATABASE）基本操作
    1.创建一个数据库
        （1）创建数据库
            CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] `db name`
            大括号部分 就是多选一 （效果一样 多用 DATABASE）
            中括号 是 可选项（如果 不存在 就帮你创建）
            mysql 中 数据库名要用 反引号 ``

            创建成功 返回 Query OK, 1 row affected (0.00 sec)

        （2）删除 数据库
            DROP DATABASE `数据库名`   （drop

            删除成功 返回 Query OK, 0 rows affected (0.00 sec)

            MySQL语法规范：
            关键字 尽量大写
            数据库、表、字段的名称 全部小写
            SQL 语句 必须分号结尾;

        （3）使用 （进入）某个数据库
            USE 数据库名

    2.表（TABLE）操作
        （1）创建表
            SHOW TABLES;        查看当前库的 所有表
            SHOW TABLES FROM 库名; 查看某个库 的表

            创建格式
            CREATE TABLE student_name(
            id int(11),               id字段，整型 默认 11 位
            name varchar(20),       name字段 字符串 类型 限制20字符
            sex varchar(5),         sex字段…………
            age int                 age字段……
            );
            注意字段 类型 有括号 必填数值，

            SHOW CREATE TABLE 表名;       查看创建 表的信息
            DESC 表名;                    查看字段信息
            SHOW COLUMNS FROM 表名;        查看字段信息

        （2）删除表
            DROP TABLE 表名；          删除表

        （3）修改表
            添加 字段
            ALTER TABLE 表名 ADD 字段 类型；       一个字段
            ALTER TABLE 表名 ADD(字段 类型，……）； 多个字段

            删除 字段
            ALERT TABLE 表名 DROP 字段；         一个
            ALERT TABLE 表名 DROP 字段，DROP字段，……多个

            修改字段类型
            ALERT TABLE 表名 MODIFY 字段 类型； (modify)

            同时修改 字段名和类型
            ALERT TABLE 表名 CHANGE 旧字段 新字段 新类型； (change)

            修改 表名
            ALERT TABLE 表名 RENAME 新表名；  （重命名）

        （4）表（内数据）的增删改查
            增
            INSERT INTO ，VALUE 插入的值  （insert to）

            在不指定具体字段时 必须有几个字段就需要 给多少值
            INSERT INTO 表名 VALUE（………………）；     一列数据

            指定具体 字段时
            INSERT INTO 表名 (字段1，字段2） VALUE(……,……)；

            插入多个值时
            INSERT INTO 表名 （字段，……） VALUES(……)，（……）…
            查看
            SELECT * FROM 表名；       查看该表的 所有内容
            SELECT 字段，…… FROM 表名；指定字段查看
            SELECT * FROM 表名 WHERE 字段=VALUE,……； 使用WHERE 进行条件 筛选

            注意：
            筛选中 字段 与 VALUE之间 可用 = ,<,>
            不同的字段间 可用 or，and

            修改
            UPDATE 表名 SET 字段=VALUE;     默认修改 全部的数据
            UPDATE 表名 SET 字段=VALUE WHERE id=value；  WHERE 添加条件

            删去
            DELETE 删
            DELETE FROM 表名 ；   会将表 全部删掉
            DELETE FROM 表名 WHERE 字段=value，…………； 添加条件删去















"""































