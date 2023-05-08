const fs = require('fs');

// 直接调用 方法读取
// fs.readFile('./_13ES/020-promise.js',(err,data)=>{
//     //出错，则抛出错误
//     if(err) throw err;

//     // 没出错继续执行
//     console.log('读取成功,%s'，data)
// })


// 使用 promise 封装
const p2 = new Promise((resolve,reject)=>{
    fs.readFile('./_13ES/ 020-promise.js',(err,data)=>{
        // 失败
        if (err) reject('读取失败');

        // 成功
        resolve(data);
    })
})

p2.then((value)=>{
    console.log(value)
},
(reason)=>{
    console.log(reason)
})

/**
 * promise 可以解决 回调地狱(callback cell)的问题，
 * Promise 具有更加直观的代码结构、更好的错误处理、
 * 更好的可读性和可组合性、减少缩进
 * 更加符合现代的异步编程规范以及更好的性能和安全性等优势。
 * 
 */