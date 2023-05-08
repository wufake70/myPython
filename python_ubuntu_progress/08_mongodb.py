
"""
##存放字典的小仓库  集合
##{_id:1 ,name: "zl",age: 18}  字典-->文档
##{_id:1 ,name: "zl",age: 18}
##{_id:1 ,name: "zl",age: 18}
##{_id:1 ,name: "zl",age: 18}
##{_id:1 ,name: "zl",age: 18}
##{_id:1 ,name: "zl",age: 18}      

MongDB的存储形式：

            {_id:1 ,name: "zl",age: 18}          
            {_id:2 ,name: "bd",age: 28}          
            {_id:3 ,name: "mr",age: 29}  		


##登录
mongo       （# ip:127.0.0.1  端口:27017
exit  #退出MongoDB


# 注意：mongo需要注意大小写使用

##1、库操作

#显示所有库
show dbs
show databases # 最开始都只有三个库: admin config local

#切换数据库  创建
use 数据库名    # 如果没有，就会创建一个新的数据库 ,创建的空数据库 不会有显示，
返回 "switched to db test"
可创建中文名的 数据库

##注意: 插入数据之后才会显示已创建好的数据库名

#查看现在在哪个数据库
db # 默认进入test数据库

#删除数据库 
db.dropDatabase()  # 删除某个数据库要先进入那个数据库，退出之后，就会彻底删除


##2、集合操作 （集合就像mysql中的表一样，用来存储文档数据）

#查看所有集合，类似于mysql中的表
show collections  

#创建集合，记得引号，如：‘table’
db.createCollection('class_29')  # 创建一个名为class_29的集合

#删除集合
db.class_29.drop()  #删除class_29集合

#默认创建
db.test2.insert({message:'你好'})     （之前 不存在 test2 集合，默认创建
一个不存在的集合，向里面插入数据，他不会取报错，
并且它还会帮我们创建好这个不存在的集合


##3、插入及查询

#插入一条 文档数据
db.class_29.insert({'name': "zl", 'age':18})

#插入多条 文档数据 要用中括号 "[]" 括起来
db.test1.insert(
[{'name':'花小龙','age':19,'message':'健身达人'},
{'name':'波多野结衣','age':37,'message':'著名女优'},
{'name':'王心凌','age':40,'message':'歌手'}])

注意: 插入键值对 数据时， 键 默认都是字符串类型(可不用加上双引号)，
值 有字符串类型 和 数值类型，字符串时 需要加上引号

#查询数据
db.class_29.find() #查询class_29集合中的所有数据


#指定 _id 插入数据
db.class_29.insert({"_id":1, 'name': "xq", 'age':17})

#格式化显示出来加上 pretty()                 （数据 输出 更加美观）
db.class_29.find().pretty()


##条件查询
db.class_29.find({'name':'zl'}).pretty() #查询名字叫zl的文档数据


##and查询，直接用 逗号 分割即可                 格式: {……,……}
db.class_29.find({'name':'zl','age':18}).pretty() #查询名字叫zl并且年龄为18的文档数据


##or查询  使用 $or              (格式: {$or:[{……},{……}]}
db.class_29.find({$or:[{'age':17},{'age':18}]}).pretty() #查询age是17或者18岁的文档数据

## and 与 or 一起使用
##查询名字是zl的并且age是17或者18岁的文档数据，名字一定是zl
db.class_29.find({'name':'zl', $or:[{'age':17},{'age':18}]}).pretty()

##查询年龄大于18并且小于29的文档数据
db.class_29.find({'age':{$gt:16},'age':{$lt:29}})

##操作符查询
db.class_29.find({'age':{$gt:18}}).pretty()  #查询年龄大于十八岁文档数据

##操作符
$gt大于
$gte(greater than equal)大于等于
$lt小于
$lte(less than equal)小于等于
$ne不等于
$eq等于


#4、修改文档
# 注意: 修改文档的某个键 需要 用到 $set       (格式： {$set:{……}}
##修改一条数据 (只会修改第一条文档数据)
db.class_29.update({age:18}, {$set:{age:20}})  #将年龄18的修改为20

# 可以为文档 添加 新的键值对
db.test1.update({name:'小红'},{$set:{message:'beautiful gril!!'}})
db.test1.update({name:'小红'},{$set:{sex:'女'}},{$set:{message:'beautiful gril!!'}})


##修改集合中所有满足条件的文档数据      使用{multi:true}
db.class_29.update({age:18}, {$set:{age:20}}, {multi:true})  #修改所有年龄为18改成20
#方法二 updateMany
db.class_29.updateMany({age:20}, {$set:{age:18}})

##全文档替换 (将一条文档数据改成 你所提供的数据)
db.class_29.update({name:'zl'}, {age:19}) #将名字为zl的文档数据修改，修改成 只有{age:19}

# 全文档 替换 （重写 填入 多条信息
db.test1.update({'name':'成龙'},{'name':'成龙','age':65,'message':'动作演员'})

#5、删除文档

##删除一条文档数据 只删除满足条件的第一条数据文档(第一个 写入的数据) {justOne:true}
db.class_29.remove({name:"bd"},{justOne:true})  #删除名字为bd的文档数据
没有{justOne:true}, 满足条件 全部删除


##删除集合中所有满足条件的文档数据，和更新不同，会删除所有符合条件的内容
db.class_29.remove({age:18})  #删除所有age为18岁的文档数据

##删除所有 文档数据
db.class_29.remove({})  #删除所有数据 (建议不执行)


##remove() 方法 并不会真正释放空间
# 需要继续执行 db.repairDatabase() 来回收磁盘空间，直接exit也可清空磁盘空间
db.repairDatabase()

##remove() 方法已经过时了，现在官方推荐使用 deleteOne() 和 deleteMany() 方法
db.class_29.deleteOne({name:'zl'})  #删除名字为zl的文档数据
db.class_29.deleteMany({age:18})  #删除所有age为18的文档数据


##6、Python 与 MongoDB交互
# pip list 查看 当前Python的模块
# 安装模块
pip install pymongo -i https://pypi.douban.com/simple/   # 换源安装模块
pip install PyMySQL
pip install redis
#注意: 如果以上 pip 指令 不管用 可尝试 pip3指令

# 豆瓣(douban) https://pypi.douban.com/simple/ 
# 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/

"""


