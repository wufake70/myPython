/**
 * 在node 中有一个全局对象global
 * 
 * 在 函数里声明全局变量 直接 变量 = 值 即可
 * 
 */

a = 99999

console.log(global.a)

// 返回 函数代码
console.log(arguments.callee + "")

/**
 * function (exports, require, module, __filename, __dirname) { your code }
 * exports、require、
 * module:  代表当前模块本身，exports是 module的属性
 * 
 * __filename:  当前模块的完整路径
 * __dirname:  当前模块所在文件夹的路径
 * 
 * 
 * 
 */


