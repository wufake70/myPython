/**
ES6 提供了新的数据结构 Set（集合 。它类似于数组，但成员的值都是唯
一的 ，集合实现了 iterator接口，所以可以使用『扩展运算符』和『 for…of…』进
行遍历，集合的属性和方法：
    1) size 返回集合的元素个数
    2) add 增加一个新元素，返回当前集合
    3) delete 删除元素，返回 boolean 值
    4) has 检测集合中是否包含某个元素，返回 boolean值
    5) clear 清空集合，返回 undefined
 */

// 声明一个 set,不存重复元素
let a = new Set([1,1,2,3,4,5,'hello']);
console.log(`${a}\t${typeof(a)}`)

// 长度
console.log(`a集合元素个数: ${a.size}`);

// 添加
a.add('world')
console.log(`a集合元素个数: ${a.size}`);

// 删除
a.delete(1)
console.log(`a集合元素个数: ${a.size}`);

// 检测
console.log(a.has(2));

// for..of 遍历
for(let i of a) console.log(i);

// 清空
a.clear()
console.log(`a集合元素个数: ${a.size}`);




