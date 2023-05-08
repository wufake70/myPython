##port端口：3306
"""
#登录
# u表示用户（user），登录admin用户，p表示密码（password）
mysql -uadmin -p
回车 输入密码：qwe123 登录mysql

#h(host)指定ip地址 -p(port)指定sq端口3306
mysql -h127.0.0.1 -p3306 -uadmin -p

mysql数据库不区分大小写，命令但是最好大写，
其次写完命令后都必须以分号进行结尾;
分号表示着一个命令的结束
以 # 号 单行注释
以 "-- " 单行注释
以 /*  ……*/  多行注释
system clear 清屏(要小写)
退出 quit


#查看数据库
SHOW DATABASES;

##使用 某个数据库
USE mysql;

# 查看自己正在使用的数据库
SELECT DATABASE();

# 查看当前登录用户
SELECT user();


##CREATE创建数据库
CREATE DATABASE `库名`;
CREATE DATABASE IF NOT EXISTS `库名`; #如果不存在创建，存在提示不创建

#DROP删除数据库
DROP DATABASE `库名`;
DROP DATABASE IF EXISTS `库名`;  #如果存在删除，不存在不做操作

MySQL 语句的规范
关键字与函数名称全部大写
数据库名称、表名称、字段名称全部小写，用反引号括起来
SQL语句必须以分号结尾


##USE使用数据库
USE `库名`;


##SHOW查看数据库中的表格
SHOW TABLES; #查看当前数据库中的数据表
SHOW TABLES FROM `库名`;  #查看某个库中具体的表


#CREATE创建表
#创建一个stu_name表，记得括号开头结尾，分号结束

CREATE TABLE [IF NOT EXISTS] `表名`(
   #字段 （数据）类型,
    id int(11),  #每个学生有一个字段id，id由数字组成，是一个整型, INT() 最大 100亿，不能超过
    BIGINT() ,可以更大
    TINYINT(),范围 0~150。
    name varchar(20) #名字限制最多存储20个字符，varchar可变长度字符
);

varchar  可变长度字符串 该类型 括号中必须填入一个数值 限制字符数量

##查看数据表信息
#查看表的创建信息
SHOW CREATE TABLE `表名`;     (可用于查看 约束名 主键字段

#查看表字段 （field）信息:
DESC stu_name;  (desc 描述）
或者
SHOW COLUMNS FROM `表名`;


#DROP删除表
DROP TABLE `表名`;


##ALTER修改数据表
##添加字段
ALTER TABLE `表名` ADD `字段` 类型;   #ADD单个字段添加

ALTER TABLE `表名` ADD(   #ADD多个字段添加
    `字段1` 类型1,
    `字段2` 类型2,
    .....
);


##删除字段
ALTER TABLE `表名` DROP `字段`;  #DROP单个删除
ALTER TABLE `表名` DROP `字段`,DROP `字段`; #DROP多个删除

##修改字段 类型
ALTER TABLE `表名` MODIFY `字段` 类型;  #MODIFY修改单个字段的类型

##同时修改字段名字和字段类型
ALTER TABLE `表名` CHANGE `字段` `新字段` 类型; #CHANGE修改单个字段的字段名和类型
注意： 可以将 整型 转换为 字符型，

##修改表名
ALTER TABLE `表名` RENAME `新表名`;


##表数据的增删改查

##1、INSERT INTO增  ,  VALUE 插入内容

##在不指定具体字段时，必须相应的有 几个字段 就需要给 多少值
INSERT INTO `stu_table` VALUE(1,'zilin',18,'男',180,'英语');

# 指定字段插入        （必要括号
INSERT INTO `stu_table`(`id`,`name`) VALUE(2,'moran');

# 如果说要插入多 行 数据，就需要将VALUE改成VALUES
INSERT INTO `stu_table`(`id`,`name`) VALUES(3,'bd'),(4,'yy');

##2、SELECT查
SELECT * FROM `stu_table`;  #星号默认查看所有字段
SELECT `id`,`name` FROM `stu_table`;  #查看单个字段
SELECT * FROM `stu_table` WHERE id=1;  #指定id为1查看字段信息 （条件筛选去看）


##3、UPDATE改
UPDATE `stu_table` SET age=20;  #默认会修改所有
注意：
筛选中 字段 与 VALUE之间 可用 = ,<,>
不同的字段间 可用 or，and

# WHERE 添加条件去修改数据
UPDATE `stu_table` SET age=20
WHERE name='zilin';

# 修改多个字段信息只需要加上逗号
UPDATE `stu_table` SET name='墨染',age=20 WHERE name='moran';

##4、DELETE删
DELETE FROM `stu_table`;  #不给条件 默认将所有 表数据删除，谨慎删除!
DELETE FROM `stu_table` WHERE id=4;  #指定删除id为4的字段
"""