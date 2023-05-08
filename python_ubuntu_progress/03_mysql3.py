"""
导入现有的 数据表
    1.命令 ： SOURCE 路径（数据库文件 的后缀为.sql)
    2.在图形化界面 中 使用具体工具


##单表查询
##1、查询所有数据
SELECT * FROM `表名`;

##2、查询部分字段数据
SELECT <字段1,字段2,....> FROM `表名`;

##3、条件查询
SELECT <字段1,字段2,....> FROM `表名`;
WHERE 条件;  #可以是:大于> 小于< 等于= 并且and 或or 不等于<>

##4、表取别名
SELECT `字段名` FROM `表名` AS 表别名;
# 通过表的别名点调用查看该字段
SELECT 表别名.`字段名` FROM `表名` AS 表别名;

SELECT `字段名` AS 字段别名 FROM `表名` AS 表别名;
# 取别名可以不使用as 只用一个空格代替


##多表查询
##内连接(INNER) ：将两张表结合组成笛卡尔积表(列是两张表列相加，行是两张表行相乘)

#以下四种都一样（内连接无条件查询）
SELECT  *  FROM  <表一>  INNER JOIN  <表二>;
SELECT  *  FROM  <表一>,<表二>;
SELECT  *  FROM  <表一>  CROSS JOIN  <表二>;
SELECT  *  FROM  <表一>  JOIN  <表二>;
#加上条件去查询（内连接条件查询）
SELECT * FROM <表一> INNER JOIN <表二>  ON  连接条件;  #使用join进行连接，添加条件的方式为ON
SELECT * FROM <表一> , <表二>  WHERE  连接条件;
SELECT * FROM <表一>  CROSS JOIN <表二>  WHERE 连接条件;

##外连接 (OUTER )
##左外连接   LEFT OUTER(可不写) JOIN  (以左边的表为主，展示左边表的所有数据)
SELECT * FROM <表一> LEFT JOIN <表二> ON 连接条件;
主表中 有null 都会展示 ，附表 有null 都不会展示

##右外连接   RIGHT JOIN (右连接和左连接类似，只是作用相反)
SELECT * FROM <表一> RIGHT JOIN <表二> ON 连接条件;

##全外连接  FULL OUTER JOIN

##子表查询
##子表查询就是 将前俩张表的 查询结果 与另一张表 做连接查询，可以说是三张表连接查询。
如下:
 SELECT * FROM
 (SELECT stu_tab.id,stu_tab.name 名字,sex 性别,age 年龄, place 籍贯,
 aca_id 学院编号,aca_tab.name 学院名
 FROM stu_tab inner join aca_tab ON aca_tab.id=aca_id) as 新表
 INNER JOIN stu_cla ON 新表.id=stu_cla.s_id;

常见报错：
1.Every derived table must have its own alias       每个派生表 必须有自己的 别名
    需要给 这张结果表（派生表） 名一个别名 以方便 后面条件 过滤
2.Duplicate column name 'id'    字段名 为 id 的列 有重复
 删去 重复字段

##子表查询的第二种使用方式，就是将查询的结果作为条件去查询使用。




##排序
##将查询出来的信息按某一字段升序或降序进行显示
SELECT <字段1,字段2,....> FROM  `表名`  ORDER BY <参照字段升序> ASC;  # ASC升序 不写ASC默认升序
SELECT <字段1,字段2,....> FROM  `表名`  ORDER BY <参照字段降序>  DESC;  # DESC降序
注意：不能使用 通配符

##限制行数
##LIMIT 对查询出来的结果限制显示的行数
SELECT <字段1,字段2,....> FROM  `表名`  ORDER BY <参照字段升序> ASC LIMIT 2;  # LIMIT只显示前两行
SELECT <字段1,字段2,....> FROM  `表名`  ORDER BY <参照字段升序> ASC LIMIT 2,3;  #从索引为2开始，向后获取3条数据

##GROUP BY中的count分组统计
##统计一段字段的个数，可通过HAVING子句对分组后的表进行条件筛选。
##注意：SELECT 之后能查询的字段只能是 GROUP BY 之后出现过的字段。

SELECT `字段名`,count(*) FROM  `表名`  GROUP BY <要统计的字段> HAVING <条件>;


##`sql`优化
MYSQL执行顺序  SELECT-->WHERE-->GROUP BY-->ORDER BY --> LIMIT 2,4;

建议：创建表时尽量添加约束，想好对应关系，避免出现过多的重复值的，减少数据冗余。

在表与表之间查询时要以外键作为连接查询的条件，最好每张表都有对应的外键关联，这样就能避免表孤立，出现非关系的情况。

总结：多多熟悉sql语句，多多尝试表与表之间的查询，记住语句执行的先后顺序，合理使用各类连接方法。

"""





