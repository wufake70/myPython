/*
ES6 提供了 Map 数据结构。它类似于对象，也是键值对的集合。 但是“键”
的范围不限于字符串，各种类型的值（包括对象）都可以当作键。 Map也实现了
iterator接口，所以可以使用『扩展运算符』和『 for…of…』进行遍历。 Map的属
性和方法：
    1) size 返回 Map的元素个数
    2) set 增加一个新元素，返回当前 Map
    3) get 返回键名对象的键值
    4) has 检测 Map中是否包含某个元素，返回 boolean值
    5) clear 清空集合，返回 undefined
*/

// 声明 Map
let m = new Map();

// 添加元素,键名可以是任意类型数据
m.set('name','尚硅谷');
m.set(999,()=>{console.log('天下没有难学的技术！！');})
let key = {
    school: 'ATGUIGU',
};
m.set(key,['北京','上海','深圳'])

// 长度
console.log(m.size);

// 删除
m.delete(999)
console.log(m.size);

// 获取
console.log(m.get(key))

// for...of 遍历
for (let v of m) console.log(v);    // 数组

// 清空
m.clear()
console.log(m.size);
