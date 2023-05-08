//声明常量
// const a; 必须要有初始值,也不可重复声明
const b = "hello world"

console.log(b)
// 规范 常量名 要大写

// 常量值 不能进行修改
// b = 9

// const也是一个块级作用域
{
    const c = 9999999;
}
// console.log(c)

// 对于数组和对象的元素修改，不算对常量的修改，不会报错
const D = [1,2,3,4]
D.push(5)
console.log(D)
// 原因: 常量指向的地址值 并没有改变
// 可用于声明 函数，防止 该函数被重写