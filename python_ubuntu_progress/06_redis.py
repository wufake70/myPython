"""
##启动服务
redis-server

##关闭Redis
redis-cli SHUTDOWN  # redis-cli 向Redis发送SHUTDOWN命令

##登录redis执行命令

redis-cli 命令参数   #临时登陆Redis 直接执行命令      （ 可用于 管道符结合 执行多名
redis-cli  ##直接登录redis
redis-cli -h 127.0.0.1 -p 6379  #远程登录Redis  -h(host)指定ip地址 -p(port)指定sq端口6379


##Redis提供了`PING`命令来测试客户端与Redis的连接是否正常，如果连接正常会收到回复`PONG`。
redis-cli PING   #临时登陆Redis直接执行 PING 命令



##Redis和mysql有区别，它存储的数据库有限制，最大上限为16个数据库，为0-15 ，登陆时默认使用0号库
切换库     命令: 'SELECT 库',


************1、基础命令应用*******************

##设置键和值，通过 SET key values  来设置一个新的键值对
SET 键 值   # 键为bar，值为1
MSET 键1 值 键2 值 ... # 同时设置多个键值对


## KEYS patten 查看有哪些键,patten可以理解为正则匹配的结果
KEYS *  #查看所有创建好的键,匹配任意个（包括0个）字符
KEYS ?  #匹配一个字符
KEYS []  #匹配括号间的任一字符，可以使用“-”符号表示一个范围，如a[b-d],可以匹配：ab,ac,ad
KEYS \x  #匹配字符x，用于转义符号。如要匹配“？”就需要使用\?


## 通过 GET 来获取key的值
GET 键 # 存在返回对应的value值，没有返回 nil ，表示空的意思
MGET 键1 键2 ... # 同时获得多个值


## EXISTS 判断一个键是否存在
EXISTS 键  #查看bar键是否存在，存在返回1，不存在返回0


## RENAME 对键重命名
RENAME 键 新的键名  #将bar重命名为bar_1
键名 可为中文字符


## 设置key过期时间
EXPIRE 键 10000  #设置过期时间s秒
TTL 键  # TTL 可以查看key还剩余的时间， -1 表示永久，-2 表示设置过期时间的键不存在
PERSIST 键 # 让键重新变成永久，成功返回1， 否则返回0，表示键不存在或者本身就是永久的

# 通过 SET key value EX seconds 来设置过期时间
SET 键 值 EX 时间 # 也可以在设置key时顺便设置时间 
# 或者 SETEX key seconds value 来设置过期时间
SETEX 键 时间 值


## 查看键对应值的数据类型

Redis 中有五种数据类型 键值对的值有五种数据类型
string(字符串类型，必须加 双引号)、hash(散列类型)、list(列表类型)、set(集合类型)、zset(有序集合类型)


TYPE 键  #查看数据类型


##删除键
DEL 键  #删除单个键值对
DEL 键1 键2 ...  #删除多个键值对


##删除所有符合规则的键，结合`Linux`的管道和`xargs`命令在shell中实现

#在shell执行以下命令，注意：redis里面执行不了。
redis-cli KEYS "user*"  #查看所有user开头的键，记得加引号
redis-cli KEYS "user*" | xargs redis-cli DEL  #shell里面删除Redis键
# 注意： 这里的键名 需要 要用到引号

# 在shell中 DEL 还可这样删除键
redis-cli DEL redis-cli KEYS "bar1"  #删除键bar1

##清空库所有的键
FLUSHALL  #清空所有库键
FLUSHDB  #清空当前库键


************************ 2、Redis 中数据类型的使用 ***********************

TYPE 键

##1、字符串类型

{"num":"1"}

SET 键 值  # 设置键值时默认值为字符串类型

APPEND 键 添加的值  # 添加字符，类似于拼接
append a ' world'     'hello world'

# 如果value值是纯数字，还可以进行加减
INCR 键 # 值加 1
DECR 键 # 值减 1

# + 整数
INCRBY 键 10  #加10
# - 整数
DECRBY 键 5  #减5


##2、列表类型  ， 列表可以实现队列，元素可以重复，满足先进先出原则

{"myli":[5,4,3,2,1]}

## 添加元素
LPUSH myli 3 4 5  # LPUSH 左边添加 （栈 先进 后出，索引增大） left 逆序输出5 4 3
RPUSH myli 2 1  # RPUSH 右边添加 （队列 先进 先出，索引靠前） right 顺序输出2 1
# 注意： 当键名 已存在 且是 string 不能添加 列表

## 获取列表长度
LLEN myli

## 查看指定位置元素
LINDEX myli 3  #查看下标索引为3的元素

## 获取列表片段值
LRANGE myli 0 5  #取索引[0:5]的值，不是左闭右开，包含右边
LRANGE myli 0 -1  # -1 表示最后一个

## 弹出元素（相当于删除）
LPOP myli  # 从左边弹出元素
RPOP myli  # 从右边弹出元素

# 删除多个元素 LREM key count value

LREM myli 2 1  # 当count>0时从列表左边开始删,删除2个值为1元素
LREM myli -1 2 # 当count<0时从列表右边开始删,删除1个值为2元素
LREM myli 0 4  # 当count=0时,删除所有值为4的元素


##3、哈希类型（简单来说它也是一个键值对形式，只不过它的值也是一个字典（键值对）

{"user":{"name":"zilin","age":"18","height":"180"}}

#添加键值
HSET user name zl
HSET user age 18
HSET user height 180

#获取值
HGET user name  #查看用户的名字


#添加多个键值
HMSET student name bd age 28    #添加名字和年龄
#获取多个值
HMGET student name age  #获取名字和年龄


HKEYS user # 获取所有键(keys)
HVALS user # 获取所有值(value)
HGETALL user # 获取所有键(keys)和值(value)
HLEN user # 获取键对应的值里面有几个键值对个数


##判断字段是否存在
HEXISTS user name  # 存在返回1 不存在返回0
HSETNX user name1 zl # 存在什么都不做,不存在添加键值

##增加数字
HINCRBY user age 10  #+ 整数
HINCRBY user age -10  #- 整数

##删除字段
HDEL user name name1


##4、集合类型 （和Python中的集合类似，没有重复值，并且无序）

{"set1":{1,2,3,"a","b"}}

## 添加元素
SADD set1 1 2 3 a b b # 添加两个集合
SADD set2 a b c 1 2 2
type set1  # 查看数据类型

## 查看所有元素
smembers set1  # (慢博丝)查看所有元素

## 删除元素
srem set1 2 # 指定元素删除
spop set2 2 # 随机删除2个元素，会提示删除了哪个元素

## 判断元素是否存在
sismember set1 1  # 存在返回1，不存在返回0

## 获取集合长度
scard set1  # 获取集合元素个数

## 随机获取几个元素 
srandmember set2 3  #随机获取3个元素,如果参数是正数表示不允许出现重复值
srandmember set2 -3  #随机获取3个元素,如果参数是负数表示允许出现重复值

##集合运算

##交集运算 两个集合共有的元素
sinter 集合1  集合2  #求集合1和集合2的交集
sinterstore  集合3  集合1  集合2  #  集合3中保存set3 和 set4的交集


##并集运算 两个元素合并去重
sunion 集合1  集合2  #求集合1和集合2的并集
sunionstore 集合3  集合1  集合2  #  集合3中保存set3 和 set4的并集


##差集运算 第一个集合有的第二个集合没有的元素
sdiff 集合1  集合2   #求集合1和集合2的差集
sdiffstore 集合3  集合1  集合2  #  集合3中保存set3 和 set4的差集


##5、有序集合

有序集合理解起来就是，一个有顺序的这么一个集合。
将集合里面每一个元素绑定一个值，根据每个元素的值决定前后顺序。


{ "age":{xq(17), zl(18), wz(18), bd(35)} }

{ "age":{xq(17), zl(18), wz(18), bd(35) } }

## 添加元素
zadd age 17 xq 18 zl 18 wz 35 bd

## 查看元素个数
zcard age

## 查看元素的值
zscore age bd  #查看bd的年龄

## 按照索引范围查看集合元素, 查看集合对应的值就加上 [WITHSCORES] 
zrange age 0 -1  #从小到大排序
zrange age 0 -1 WITHSCORES  #携带值查看
zrevrange age 0 -1  #从大到小排序（reverse）

# 移除元素
zrem age bd  #移除北斗的键值对

## 获取指定范围的元素
zrangebyscore age 17 28  #查看17岁到28岁之间排序好的元素，包含17和18岁
zrangebyscore age (17 28  #查看不包含17岁的
zrangebyscore age (17 (28  #查看既不包含17岁，也不包含28岁的元素     
zrangebyscore age 17 28 limit 0 2  #查看排序好的元素，从0开始保留2个
                       
## 统计指定范围的元素个数                     
zcount age 15 28   #统计15岁到28岁之间的元素个数
                       
## 增加或递减某个元素的值
zincrby age 1 zl  #将子冧年龄加1岁
zincrby age -2 zl #将子冧年龄减2岁
                       
## 按照索引范围删除元素
zremrangebyrank age 0 2 #删除排序好，索引0到2的值，包括2
                        
## 按照指定范围删除元素   
zremrangebyscore age 17 28  #删除17岁到28岁之间排序好的元素
                       
#运算集合1和集合2两个有序集合的交集结果，存入集合3有序集合里面                  
zinterstore 集合3 2 集合1 集合2   # 数字2指运算两个有序集合  

#运算集合1和集合2两个有序集合的并集结果，存入集合3有序集合里面 
zunionstore 集合3 2 集合1 集合2  # 数字2指运算两个有序集合  



redis = {"bar1":"a", "myli":[5,4,3,2,1], "user":{"name":"zilin","age":18,"height":180},
         "set1":{1,2,3},"age":{'xq'(17),'zl'(18),'wz'(18),'bd'(35)}}
"""
