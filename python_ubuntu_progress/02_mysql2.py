"""
##添加非空约束    （添加 非空约束 的字段 不能为null 必须填值 斗则报错）

##非空约束也就是设定表的字段值不能为空值，也就是不为NULL（空值）
ALTER TABLE <数据表名> CHANGE COLUMN <字段名> <字段名> <数据类型> NOT NULL;
ALTER TABLE <数据表名> MODIFY COLUMN <字段名> <数据类型> NOT NULL;
注意： 不能给 已有 null的字段 添加 非空约束

##删除非空约束
ALTER TABLE <数据表名> CHANGE COLUMN <字段名> <字段名> <数据类型> NULL;
ALTER TABLE <数据表名> MODIFY COLUMN <字段名> <数据类型> NULL;

##添加唯一约束    ( id 是唯一的
##唯一约束就是限制字段唯一性，
##使得具有 标识的字段 只能有一个，该字段的值不重复，且只出现一次，可以为空值  (空值不代表 重复
ALTER TABLE <数据表名> ADD CONSTRAINT <唯一约束名> UNIQUE( 字段名 );      （constraint 约束
注意： 可添加 多个 唯一约束 ，添加前 查看 原字段值 有没有重复的；
##删除唯一约束
ALTER TABLE <数据表名> DROP INDEX <唯一约束名>;

##添加主键约束        （主键只能设置一个
##字段添加了主键约束之后，该字段不能为空值并且值不可以重复，     （条件：非空+唯一
##也就是说主键约束包含了非空且唯一的条件
ALTER TABLE <数据表名> ADD PRIMARY KEY(字段名);
##删除主键约束
ALTER TABLE <数据表名> DROP PRIMARY KEY;

##添加自增约束                    （条件：非空+唯一+整型，自增约束 可不用指定 相应字段
##为字段数据自动添加编号
##字段为唯一约束或主键约束才可以添加自增约束
ALTER TABLE <数据表名> CHANGE <字段名> <字段名> <整型> NOT NULL AUTO_INCREMENT;
##删除自增约束
#CHANGE修改删除自增
ALTER TABLE <数据表名> CHANGE COLUMN <字段名> <字段名> <数据类型> NOT NULL;
#删除主键约束
ALTER TABLE <数据表名> DROP PRIMARY KEY;

##添加默认约束
##字段没有明确给数据时，添加默认约束的值
ALTER TABLE <数据表名> ALTER <字段名> SET DEFAULT <默认值>;
注意： 整型 不能设置 默认 约束，默认字符 长度 不能超过 限制
设置默认约束，就不能设置 非空约束

##删除默认约束
ALTER TABLE <数据表名> ALTER <字段名> DROP DEFAULT;
ALTER TABLE <数据表名> ALTER <字段名> SET DEFAULT NULL;
ALTER TABLE stu_info CHANGE total total varchar(8) NULL;

在创建表的时候 设置约束：
mysql> CREATE TABLE stu (
    -> id int PRIMARY KEY AUTO_INCREMENT,       设置 主键、自增
    -> name varchar(30) NOT NULL,                   非空
    -> sex varchar(3) DEFAULT '未定义',              默认
    -> age int(3) DEFAULT NULL,
    -> phone varchar(11) NOT NULL UNIQUE KEY)       非空、唯一
    -> AUTO_INCREMENT=100 DEFAULT CHARSET=utf8;     设置 自增起始值、编码格式
    注意：设置 唯一约束时 自动将约束名 改为 字段名




##外键的值：他一定 是来自于 另一张表的主键 所包含的值，或是null（可以为null）
外键 可以用联系表
##一对多：一个学院可以有多个学生
##一对一：每个学生都对应一条详情信息
##多对多：就如 一个学生 可以选多个课程，而一个课程 可以有多个 学生；   需要创建 中间表
中间表 ： 外键（学生表主键） + 外键（课程表主键）   联合主键（防止组合重复）。


##外键约束
ALTER TABLE <主表> ADD CONSTRAINT <外键名> FOREIGN KEY(字段名) REFERENCES <参照表>(字段名);

ON DELETE SET NULL  #添加级联删除，依赖性外键删除时字段值设置为空，针对一对多关系
ON DELETE CASCADE  #添加级联删除，依赖性都被删除，针对一对一关系

创建表示 添加外键约束
 CREATE TABLE stu_info (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(9) NOT NULL,
    aca_id int,
    CONSTRAINT aca_id FOREIGN KEY(aca_id) REFERENCES aca_tab(id)
    ON DELETE SET NULL)         添加外键、级联删除
    AUTO_INCREMENT=10001 DEFAULT CHARSET=UTF8;



#事务只有两种情况：
1、开始事务--结束事务  #这种就是开始到结束中间一系列操作全部执行
2、开始事务--回滚事务  #这种就是开始事务之后中间不小心做了错误操作，进行事务回滚，回滚会将之前的一系列操作撤销
##BEGIN--COMMIT         （commit 提交
##BEGIN--ROLLBACK

##创建视图
##将一张表的查询结果，作为一张虚拟表（视图表）存储在数据库内
##还会跟着你原来的表，进行更新。

CREATE VIEW <视图名>(字段名,字段名) AS <SELECT查询语句>;

DROP VIEW <视图名>
"""
