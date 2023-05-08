// ES6 引入一个 新的原始数据类型 Symbol，表示独一无二的
// symbol 类似 字符串，不能与其他数据 作运算
// 也不能使用 for...in..(用于遍历对象的属性)遍历

// 创建symbol
let s = Symbol();
console.log(s);  // 返回 Symbol()，内部数据是不可见的

let s1 = Symbol("hello")
console.log(`%s\t%s`,s1,typeof(s1));


// 应用: 向对象中添加(唯一的，私有的，不可以修改的)方法 
// 添加f1、f2
// 法一:    
let a = {
    name: 'wufake',
    age: 999
}
let methods = {
    f1: Symbol(),
    f2: Symbol()
}
a[methods.f1] = function(){
    console.log('fun1');
}
a[methods.f2] = function(){
    console.log('fun2');
}

// 调用 f1
// 获取 对象上的symbol属性,
const sbl = Object.getOwnPropertySymbols(a)[0]
// 通过symbol属性调用
a[sbl]()

// 法二: 
let b = {
    [Symbol('hello')]: function(){
        console.log('b');
    }
}
// 调用 
const sbl2 = Object.getOwnPropertySymbols(b)
b[sbl2[0]]();

/**
 * 使用 symbol 向对象添加 方法的意义?
 *      使用Symbol添加方法的意义在于，它允许你向对象添加私有方法和属性，
 *      这些方法和属性不会被意外修改或覆盖，因为Symbol值在JavaScript中是唯一的，不能被复制或重复创建
 */
