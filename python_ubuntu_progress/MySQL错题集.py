# _*_coding :utf-8 _*_
# @Time :2022/8/8 8:58
# @File : MySQL错题集
# @Project : python_ubuntu_progress

"""
1. 判断一个 字段 是否 为null时，需要 用 is null 或者 安全等于号  <=>     (为null 而生
  不能使用等于号 =

2.MySQL 不支持 全外连接（FULL OUTER JOIN）

3.union 将 两张表（作为单一结果集 输出） 有去重效果、union all 无去重 效果。(必须字段相同)

4.MySQL 查询语句的先后 顺序
    1. FROM阶段
    2. WHERE阶段      (无内连接时
    3. GROUP BY阶段
    4. HAVING阶段     (分组条件)
    5. SELECT阶段
    6. ORDER BY阶段


5.  # DISTINCT 关键字 可以去除 重复数据
    # 可以配合 COUNT() 使用，COUNT(DISTINCT `字段`)
    #
    # ROUND() 函数 可以 四舍五入,(注意：只对小数有用)
    # 可以 通过 'num / 1' 获取 相关小数，
    # ROUND(num / 1, 3)，即可 保留 3位小数

6.  # 查找字符串 方法
    # 方法1：使用通配符%，配合 LIKE 模糊查询。（还有 '_'）
    # 方法2 正则
    # REGEXP


"""




































