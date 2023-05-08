// ES6 可以声明 箭头函数
let fun = (a,b)=>{
    console.log(`参数1: ${a},参数2: ${b}`);
}

fun('hello','world');

// 箭头函数新特性
// 1.this 是静态的，
//   始终指向声明时所在的作用域下的this的值

global.name = 'global' 
let fun2 = ()=>{
    console.log(this.name);
}
let fun3 = function() {
    console.log(this.name);
}

fun2()  // 返回 {};     在浏览器的全局中 this 指向的就是 window
fun3()  // 返回全局对象 global

const a = {fun2,fun3,name: 'a'};
a.fun2();   // 返回 {};
a.fun3();   // 返回实例对象

// 2.箭头函数 不能做 构造函数
// 3.不能使用 arguments(arguments用来保存实参)
// 4.箭头函数的简写 
        // ①省略小括号，当形参 当且仅当只有一个时
        // ②省略花括号，当代码 有且只有 一行时，
        //  可以省略花括号，并且会将其作为返回值

/**引用场景
 *  适用于 与this 无关的回调，定时器回调，数组的方法回调
 *  不适于 与this 有关的回调，事件回调(事件监听器)，对象的方法
 */

// 练习 返回数组中偶数:
numli = [1,2,3,4,5,6,7,8,9,0]
console.log(numli.filter((i)=> i%2===0))