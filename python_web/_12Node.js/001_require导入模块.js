/**
 * 在node中 ，使用require() 引入模块以后，该函数 会返回一个对象，该对象代表引入的的模块。
 * 
 * 
 * 模块化
 *      在node 中 ，一个js文件 就是一个模块
 *      每个js文件中的js代码都是 独立运行在一个函数中的，而不是全局作用域，所以一个模块中的变量和函数在导入后无法直接访问
 * 
 * 
 * 可以通过 exports 来向外部暴露变量和方法
 *  只需要将其 设置为 exports的 属性即可
 */


var a = require("./000.js")
// console.log(a.obj.name)
ab = 100
console.log(global.ab)
