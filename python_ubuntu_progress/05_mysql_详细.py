# _*_coding :utf-8 _*_
# @Time :2022/7/25 8:09
# @File : MySQL_查询
# @Project : python_ubuntu_progress


"""
###SQL（structured query language 结构化查询语言）的分类
    1.DDL（Data Definition Languages、数据定义语言），这些语句定义了不同的数据库、表、视图、索
        引等数据库对象，还可以用来创建、删除、修改数据库和数据表的结构。
        主要的语句关键字包括 CREATE 、 DROP 、 ALTER 、TRUNCATE(truncate 清空表数据 结构保留)、
        RENAME等。

    2.DML（Data Manipulation Language、数据操作语言），用于添加、删除、更新和查询数据库记
        录，并检查数据完整性。
        主要的语句关键字包括 INSERT 、 DELETE 、 UPDATE 、 SELECT 等。
        SELECT是SQL语言的基础，最为重要。

    3.DCL（Data Control Language、数据控制语言），用于定义数据库、表、字段、用户的访问权限和
    BEGIN 、COMMIT、ROLLBACK、SAVEPOINT、GRANT(授权)、REVOKE（撤权）、等。

###MySQL 变量
    系统变量

    声明变量 并 赋值；
    SET @a:= 变量值
    mysql> SELECT @a:=555,@a;
    +---------+------+
    | @a:=555 | @a   |
    +---------+------+
    |     555 |  555 |
    +---------+------+

###导入现有的 数据表
    1.命令 ： SOURCE 路径（数据库文件 的后缀为.sql)
    2.在图形化界面 中 使用具体工具
###去除 数据表中的 重复数据 DISTINCT （distinct 不同的）
    SELECT DISTINCT 指定相关字段 FROM 任意表；

###"` ``` " 着重号 （反引号） 用于区别 与MySQL关键字 一样的 数据表名 ，将其包围，或者是 字符串的表名;
    中文表（或字段） 全部使用 反引号包围


###SELECT 查询时 添加常数
    SELECT "尚硅谷" 字段  FROM 数据表名字
    尚硅谷    ……
    尚硅谷    ……

###显示表结构 DESC (describe 描述) 、SHOW COLUMNS FROM 数据表名字

###算数运算符    + 、-、*、/ or div（除法）、% or mod（取模，取余）  先乘除后加减
    SELECT 100 , 100+1,100*0, 100/50,100 div 50,100%51,100 mod 51 FROM DUAL;
    +-----+-------+-------+--------+------------+--------+------------+
    | 100 | 100+1 | 100*0 | 100/50 | 100 div 50 | 100%51 | 100 mod 51 |
    +-----+-------+-------+--------+------------+--------+------------+
    | 100 |   101 |     0 | 2.0000 |          2 |     49 |         49 |
    +-----+-------+-------+--------+------------+--------+------------+
    1 row in set (0.00 sec)
    DUAL 是MySQL 中一张虚拟的表

    SELECT '80'*'4' FROM DUAL;
    +----------+
    | '80'*'4' |
    +----------+
    |      320 |
    +----------+
    在SQL语言中 会将 数字型 字符串 转换 成为 数值类型（隐式转换） 进行计算
    纯字符串 做运算 转换为 数值 0；
    null值 参与 运算 为null；
    mysql> SELECT 1+NULL,1-NULL,1*NULL,1/NULL,1%NULL;
    +--------+--------+--------+--------+--------+
    | 1+NULL | 1-NULL | 1*NULL | 1/NULL | 1%NULL |
    +--------+--------+--------+--------+--------+
    |   NULL |   NULL |   NULL |   NULL |   NULL |
    +--------+--------+--------+--------+--------+
    实现字符串 拼接 使用 CONCAT函数

###比较运算符
    1.= （等于）、<=> 安全等于运算符、!= <> 不等于、……
    返回 1 为 真；返回 0 为 假；
    在使用等号运算符时，遵循如下规则：
    如果等号两边的值、字符串或表达式 都为字符串，则MySQL会按照字符串进行比较，其比较的
    是每个字符串中字符的 ANSI编码 （美国国家标准局 ASCII码）是否相等。
    如果等号两边的值都是整数，则MySQL会按照整数来比较两个值的大小。
    如果等号两边的值一个是整数，另一个是字符串，则MySQL会将字符串转化为数字进行比较（会隐式转换。
    如果等号两边的值、字符串或表达式中有一个为NULL，则比较结果为NULL。
    对比：SQL中赋值符号使用 :=

    安全等于 <=> 用于 与 null 比较，两端都是null 返回 1 ；

###逻辑运算符
    或 OR ||、
    且 AND &&、
    NOT 非 ！（取反）、
    XOR 逻辑异 或
    两边一真一假 为真

###位运算符



### WHERE过滤 的 条件格式
     LIKE               模糊匹配；   % 表示 不确定个数的字符 类似 正则 的 “.*” 零到多次
     SELECT * FROM stu_tab WHERE name LIKE '%张%'

     REGEXP             正则匹配；
     SELECT * FROM stu_tab WHERE id REGEXP '3$'   匹配格式要用 引号 包围

     IS NULL            判断是否为空； IS NOT NULL；注意 ISNULL() 是函数
     BETWEEN A AND B    判断一个值是否在 A B 之间。
     SELECT * FROM stu_tab WHERE id BETWEEN 10003 AND 10005;

     IN() / NOT IN()

### LIMIT 实现 分页
    格式： LIMIT 位置偏移量 行数（显示）
    SELECT * FROM stu_tab LIMIT 0,2;    显示前两条数据
    公式： LIMIT (要显示页面 - 1)*每页显示的条数， 每页显示条数；


###多表查询 的分类：
    1.等值连接（=） ， 非等值连接（范围）
    2.自连接（表本身 自我链接） ， 非自链接（不同之间的 表进行链接）
    3.内连接（inner join），外连接（outer join）






###函数
   基本函数
   数值型函数
    LEAST()返回最小 ascii码值的 字符;        GREATEST(), 相反
    SELECT LEAST(1,2,3,4,5);                    返回 1
    SELECT LEAST('Z','A','a','t','d','p');      返回 "A"

    进制转换 BINz(),OCT(),HEX()
    mysql> SELECT BIN(10),OCT(10),HEX(10);
    +---------+---------+---------+
    | BIN(10) | OCT(10) | HEX(10) |
    +---------+---------+---------+
    | 1010    | 12      | A       |
    +---------+---------+---------+

    ROUND() 函数 ，对浮点数 ，进行四舍五入
    mysql> SELECT ROUND(99.777,2);  保留两位，默认 整数（integer）
    +-----------------+
    | ROUND(99.777,2) |
    +-----------------+
    |           99.78 |
    +-----------------+

   字符型函数
    CONCAT()函数 MySQL 字符串 拼接
    SELECT CONCAT('hello',' ','world');

    mysql> SELECT CONCAT_WS('-','hello','world') ,字符串输出 格式化。
    +--------------------------------+
    | CONCAT_WS('-','hello','world') |
    +--------------------------------+
    | hello-world                    |
    +--------------------------------+

    实操：mysql> SELECT CONCAT_WS('-',name,sex,age,place) FROM stu_tab;
    +-----------------------------------+
    | CONCAT_WS('-',name,sex,age,place) |
    +-----------------------------------+
    | 张华-男-20-香港                   |
    | 李虎-男-19-四川                   |
    | 杨舒-女-19-贵州                   |
    | 张宇-男-18-云南                   |
    | 陈明-男-18-湖南                   |
    | 杨华-男-18-湖南                   |
    | 程刚-男-20-湖南                   |
    +-----------------------------------+

    LENGTH()    返回字符串 字节数 ，utf8中 一个汉字 三个字节。
    SELECT LENGTH('你好');

   思维提升：学生管理系统 登录的初始密码 设置；
   mysql> UPDATE stu_tab SET pwd=CONCAT_WS('_',id,'love');   字符串的 格式化输出
    mysql> SELECT * FROM stu_tab;
    +-------+--------+------+------+--------+--------+------------+
    | id    | name   | sex  | age  | place  | aca_id | pwd        |
    +-------+--------+------+------+--------+--------+------------+
    | 10001 | 张华   | 男   |   20 | 香港   |    104 | 10001_love |
    | 10002 | 李虎   | 男   |   19 | 四川   |    104 | 10002_love |
    | 10003 | 杨舒   | 女   |   19 | 贵州   |    104 | 10003_love |
    | 10004 | 张宇   | 男   |   18 | 云南   |    101 | 10004_love |
    | 10005 | 陈明   | 男   |   18 | 湖南   |    101 | 10005_love |
    | 10006 | 杨华   | 男   |   18 | 湖南   |    103 | 10006_love |
    | 10007 | 程刚   | 男   |   20 | 湖南   |    102 | 10007_love |
    +-------+--------+------+------+--------+--------+------------+

   日期和时间类函数:
    CURDATE() 获取当前日期    （current 当前的
    CURTIME() 获取当前时间
    NOW()   获取当前的日期 和时间
    SELECT CONCAT_WS('-',CURDATE(),CURTIME());

    获取格林威治时间（utc 世界同一时间）
    SELECT CONCAT_WS('-',UTC_DATE(),UTC_TIME());

    返回当前时间 以 时间戳 形式
    SELECT UNIX_TIMESTAMP(NOW());


### if判断语句  （非流程控制
    IF(条件判断，value（为真 返回值）,value2（为假 返回值）)
    SELECT IF(TRUE,999,000);
    实例：mysql> SELECT *,IF(sex='男','男学生',' 女学生') '学生性别'(显示该列字段) FROM stu_tab;
    +-------+--------+------+------+--------+--------+------------------------------
    | id    | name   | sex  | age  | place  | aca_id | IF(sex='男','男学生','女学生')
    +-------+--------+------+------+--------+--------+------------------------------
    | 10001 | 张华   | 男   |   20 | 香港   |    104 | 男学生
    | 10002 | 李虎   | 男   |   19 | 四川   |    104 | 男学生
    | 10003 | 杨舒   | 女   |   19 | 贵州   |    104 | 女学生
    | 10004 | 张宇   | 男   |   18 | 云南   |    101 | 男学生
    | 10005 | 陈明   | 男   |   18 | 湖南   |    101 | 男学生
    | 10006 | 杨华   | 男   |   18 | 湖南   |    103 | 男学生
    | 10007 | 程刚   | 男   |   20 | 湖南   |    102 | 男学生

    IFNULL()…………



####CASE WHEN （条件判断） THEN （返回值） …… ELSE... END '显示字段'
    实例: SELECT *,CASE
    WHEN id BETWEEN 10000 AND 10002 THEN '低年级'
    WHEN id BETWEEN 10003 AND 10005 THEN '中年级'
    ELSE '高年级' END '年级'
    FROM stu_tab;
    +-------+--------+------+------+--------+--------+-----------+
    | id    | name   | sex  | age  | place  | aca_id | 年级      |
    +-------+--------+------+------+--------+--------+-----------+
    | 10001 | 张华   | 男   |   20 | 香港   |    104 | 低年级    |
    | 10002 | 李虎   | 男   |   19 | 四川   |    104 | 低年级    |
    | 10003 | 杨舒   | 女   |   19 | 贵州   |    104 | 中年级    |
    | 10004 | 张宇   | 男   |   18 | 云南   |    101 | 中年级    |
    | 10005 | 陈明   | 男   |   18 | 湖南   |    101 | 中年级    |
    | 10006 | 杨华   | 男   |   18 | 湖南   |    103 | 高年级    |
    | 10007 | 程刚   | 男   |   20 | 湖南   |    102 | 高年级    |
    +-------+--------+------+------+--------+--------+-----------+

###明文 加密处理
    PASSWORD(pwd) 不可逆
    UPDATE stu_tab SET pwd=PASSWORD(CONCAT_WS('_',id,'love'));
    +-------+--------+------+------+--------+--------+-------------------------------------------+
    | id    | name   | sex  | age  | place  | aca_id | pwd                                       |
    +-------+--------+------+------+--------+--------+-------------------------------------------+
    | 10001 | 张华   | 男   |   20 | 香港   |    104 | *37BC51F1F48B6EBB6829F654DC5CF7077247CA7C |
    | 10002 | 李虎   | 男   |   19 | 四川   |    104 | *E46EA482BAED918BA440AC80A24E0F3E5413D247 |
    | 10003 | 杨舒   | 女   |   19 | 贵州   |    104 | *B1EBED29764E77115C1700113A6A7E0B8A253A1C |
    | 10004 | 张宇   | 男   |   18 | 云南   |    101 | *2497DAE10CFF895A7F13BE02C87A7A1E9A471375 |
    | 10005 | 陈明   | 男   |   18 | 湖南   |    101 | *841C6F478403B7FCA68B53C21F6C384996BCF5B9 |
    | 10006 | 杨华   | 男   |   18 | 湖南   |    103 | *5993C2667EB30FBE97C08E634F62A836499B78B7 |
    | 10007 | 程刚   | 男   |   20 | 湖南   |    102 | *7BC42F0BCC0C35941ED7B3A971ECCACC828AD495 |
    +-------+--------+------+------+--------+--------+-------------------------------------------+

    MD5(pwd) 返回字符串str的md5加密后的值，也是一种加密方式。若参数为NULL，则会返回NULL
    mysql> UPDATE stu_tab SET pwd=MD5(CONCAT_WS('_',id,'love'));
    +-------+--------+------+------+--------+--------+----------------------------------+
    | id    | name   | sex  | age  | place  | aca_id | pwd                              |
    +-------+--------+------+------+--------+--------+----------------------------------+
    | 10001 | 张华   | 男   |   20 | 香港   |    104 | 9d00f5f4bca530ac5302a0c792f8d96d |
    | 10002 | 李虎   | 男   |   19 | 四川   |    104 | 328f1b077cf18c6b90fd733297bfa75b |
    | 10003 | 杨舒   | 女   |   19 | 贵州   |    104 | 09e4f3339077ce5bc9f33ea796481b7c |
    | 10004 | 张宇   | 男   |   18 | 云南   |    101 | 108a7e8a12a6c1635ab6223062308c31 |
    | 10005 | 陈明   | 男   |   18 | 湖南   |    101 | a87bbd5a29b11d30e681dd3c959742d2 |
    | 10006 | 杨华   | 男   |   18 | 湖南   |    103 | fd2c9349a9c2e457e3a2d8f831abc02b |
    | 10007 | 程刚   | 男   |   20 | 湖南   |    102 | 8f40115f3f2548c90acdbb1b86ce1777 |
    +-------+--------+------+------+--------+--------+----------------------------------+

    SHA(str) 从原明文密码str计算并返回加密后的密码字符串，当参数为NULL时，返回NULL。 SHA加密算法比MD5更加安全 。
    注：
    1.以上加密都是不可逆的。
    2.若 报错  "Data too long for column 'pwd'" 字段pwd 的 字符长度 限制太短了，修改即可；


###常用的聚合（多行）函数；         下列 函数 自动过滤 null值
    MAX(整型字段) 返回该列的最大值；MIN(……) 相反
    可将它 返回的结果 作为过滤的 条件（用括号包围）
    SELECT * FROM stu_fee WHERE (SELECT MAX(fee) FROM stu_fee)=stu_fee.fee;

    AVG(相关字段) 求多行数据的 平均值
    mysql> SELECT AVG(age) FROM stu_tab;
    +----------+
    | AVG(age) |
    +----------+
    |  18.8571 |
    +----------+

    SUM(相关字段)  求多行数据的 总和。

    COUNT(相关字段)  统计 该字段的数据 行数；   COUNT(*)，COUNT(数值) 返回 总行数
    mysql> SELECT COUNT(age) FROM stu_tab;
    +------------+
    | COUNT(age) |
    +------------+
    |          7 |
    +------------+

    GROUP BY 相关字段、     按照某个字段 进行分组
    mysql> SELECT age,COUNT(age) FROM stu_tab GROUP BY age ;
    +------+------------+
    | age  | COUNT(age) |
    +------+------------+
    |   18 |          3 |
    |   19 |          2 |
    |   20 |          2 |
    +------+------------+

    按照多个字段 进行分组         （GROUP BY 字段，……
    mysql> SELECT age,sex,COUNT(sex),COUNT(age) FROM stu_tab GROUP BY sex,age ;
    +------+------+------------+------------+
    | age  | sex  | COUNT(sex) | COUNT(age) |
    +------+------+------------+------------+
    |   19 | 女   |          1 |          1 |
    |   18 | 男   |          3 |          3 |
    |   19 | 男   |          1 |          1 |
    |   20 | 男   |          2 |          2 |
    +------+------+------------+------------+

    注意： 按什么字段 分组 ，就只能显示（SELECT） 什么字段；

    分组的条件 HAVING 过滤，        只能 选择分组的字段 进行 条件判断。
    mysql> SELECT age,sex,COUNT(sex),COUNT(age) FROM stu_tab GROUP BY sex,age HAVING sex='女';
    +------+------+------------+------------+
    | age  | sex  | COUNT(sex) | COUNT(age) |
    +------+------+------------+------------+
    |   19 | 女   |          1 |          1 |
    +------+------+------------+------------+


###设置 字符集
    CHARACTER SET 相关字符集
    CHARSET=相关字符集

    查看数据局 所使用的字符集
    SHOW VARIABLES LIKE 'CHARACTER%';
    STATUS      查看数据 相关信息

###复制 / 拷贝 一张表  （数据库 同理
    mysql> CREATE TABLE employees AS (SELECT * FROM atguigudb.employees);


###求中位数(median)     （以stu_tab 表 的age字段 为例
    mysql> SET @index:=0;               设置 索引变量时 ，最好不用 “*”。
    SELECT * FROM
    (SELECT @index:=@index+1 'index',name,age
    FROM stu_tab ORDER BY age ASC) a  按相关字段 排序，并添加索引变量
    WHERE a.index=CEIL(@index / 2) ;
    +-------+--------+------+
    | index | name   | age  |SELECT * FROM
    (SELECT @index:=@index+1 'index',name,age
    +-------+--------+------+
    |     4 | 李虎   |   19 |
    +-------+--------+------+
    注意：以上只适用于 奇数行数据

    偶数行数据 求中位数
    mysql> SET @index:=0;       设置 索引变量
    SELECT AVG(age) FROM        求最中间 两个数的平均值
    (SELECT * FROM
    (SELECT @index:=@index+1 'index',name,age FROM
    stu_tab ORDER BY age ASC) a     添加索引
    WHERE a.index=CEIL(@index / 2) OR
    a.index=CEIL(@index/2+1)) b;    过滤出最中间的两条数据
    +----------+
    | AVG(age) |
    +----------+
    |  18.5000 |
    +----------+


    

###预处理语言    （结合 存储结构使用
    可执行 字符串命令 , 需要拼接字符串，特别是 表名 字段名 这类参数；

    PREPARE test FROM 字符串命令；    只能 准备一条语句 ,并将它赋值给 test
    EXECUTE test;                   执行 该字符串命令
    DROP PREPARE test;              删除 预处理 释放内存 也可使用 DEALLOCATE 关键字
    mysql> SET @a=CONCAT("SELECT AVG(","age",") FROM (SELECT * FROM (SELECT
    @index=@index+1 'index',name,age FROM ","stu_tab"," ORDER BY age ASC) a WHERE a.index=CEIL(@index / 2) OR
    a.index=CEIL(@index / 2+ 1)) b");
    mysql> prepare test from @a;
    mysql> set @index=0// execute test;
    +----------+
    | AVG(age) |
    +----------+
    |  18.6250 |
    +----------+


###存储过程 和 存储函数
    存储过程:
    存储过程的英文是 Stored Procedure 。它的思想很简单，就是一组经过 预先编译 的 SQL 语句
    的封装。
    执行过程：存储过程预先存储在 MySQL 服务器上，需要执行的时候，客户端只需要向服务器端发出调用
    存储过程的命令，服务器端就可以把预先存储好的这一系列 SQL 语句全部执行。

    分类：
    存储过程的参数类型可以是IN、OUT和INOUT。根据这点分类如下：
    1、没有参数（无参数无返回）
    2、仅仅带 IN 类型（有参数无返回）
    3、仅仅带 OUT 类型（无参数有返回）
    4、既带 IN 又带 OUT（有参数有返回）
    5、带 INOUT（有参数有返回）
    注意：IN、OUT、INOUT 都可以在一个存储过程中带多个

##创建 / 删除 存储过程
    格式:
    CREATE PROCEDURE 存储过程名(IN|OUT|INOUT 参数名 参数类型,...)
    [characteristics ...]
    BEGIN
    存储过程体
    END

    需要设置新的结束标记
    DELIMITER $ …………创建存储过程……$ 设置结束符
    注意: 默认情况下 命令结束符 是 分号 ";" ,使用 DELIMITER $ 命令后
    将切换成 $ ,以便于 在虚拟机的mysql 交互界面 上 编写 存储过程体。

    创建一个 可以求中位数（偶数行 数据）的存储过程
    CREATE PROCEDURE stu_med(IN f VARCHAR(10),IN t VARCHAR(10))
    BEGIN
    SET @a=CONCAT("SELECT AVG(",f,") FROM
    (SELECT *
    FROM (SELECT @index:=@index+1 'index',name,",f,"FROM
    ",t," ORDER BY ",f," ASC) a
    WHERE a.index=CEIL(@index/2) OR a.index=CEIL(@index/2+1)) b");
    PREPARE test FROM @a;
    SET @index=0; EXECUTE test;
    DROP PREPARE test;
    END //
    注意：
    1.存储过程 只能使用 在 一个数据库里面。
    2.每个参数必须要在 存储过程 中使用到，否则不要写

    封装 求中位数的 存储过程 （升级版# UNION
     CREATE PROCEDURE median(IN f VARCHAR(20),IN t VARCHAR(20))      （f 为字段 、t 为数据表
     BEGIN
     SET @a:=CONCAT("SELECT AVG(",f,") '中位数(平均)' FROM
     (SELECT * FROM
     (SELECT @index:=@index+1 'index',name,",f," FROM ",                    预处理 第二种情况字符串形式
     t," ORDER BY ",f," ASC) a WHERE a.index=CEIL(@index/2) OR a.index=CEIL(@index/2+1)) b");
     SET @b:=CONCAT("SELECT ",f," '中位数' FROM
     (SELECT * FROM (SELECT @index:=@index+1 'index',name,",f," FROM ",
     t," ORDER BY ",f," ASC) a WHERE a.index=CEIL(@index/2)) b");           预处理 第一种情况字符串形式
     SET @index:=0;
     SET @aa:=CONCAT("SET @ab:=(SELECT COUNT(*) FROM ",t,")");
     PREPARE test3 FROM @aa;EXECUTE test3;
     IF @ab % 2=0 THEN PREPARE test FROM @a;                               （使用了 if分支控制语句
     EXECUTE test; DROP PREPARE test;
     ELSE PREPARE test2 FROM @b;
     EXECUTE test2; DROP PREPARE test2;
     END IF;
     END

####调用存储过程      CALL 名称(参数);


###游标 （光标）
    可以逐行处理数据，如 将某个字段逐行累加，并规定 不能大于多少，返回相关信息

#### UNION
    合并查询结果 利用UNION关键字，可以给出多条SELECT语句，
    并将它们的结果组合成单个结果集。
    合并时，两个表对应的列数和数据类型必须相同，并且相互对应。
    各个SELECT语句之间使用 UNION 或 UNION ALL 关键字分隔。

    格式:
         SELECT * FROM stu_tab WHERE age >= 18
         UNION
         SELECT * FROM stu_tab WHERE age <= 18;    (将两边的表 组合成单个结果集

    注意：
    1.合并时，两个表对应的 列数(filed 字段) 和 数据类型 必须相同，并且相互对应。
    2.union 有去重 效果、union 无去重 效果










##存储函数
    ……………………








































"""