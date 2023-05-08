const fs = require('fs');
const { networkInterfaces } = require('os');
const { resolve } = require('path');

// 读取 多个文件，多个异步任务
// 没有 promise,陷入 回调地狱
// fs.readFile('./_13ES/test1.txt',(err,data)=>{
//     if(err) throw err
//     let content = data;
//     fs.readFile('./_13ES/test2.txt',(err,data)=>{
//         if(err) throw err
//         content = `${content}\n${data}`;
//         fs.readFile('./_13ES/test3.txt',(err,data)=>{
//             if(err) throw err
//             content = `${content}\n${data}`;
//             console.log(content)
             
//         })
//     })
// })


// 使用 promise
const p1 = new Promise((resolve,reject)=>{
    fs.readFile('./_13ES/test1.txt',(err,data)=>{
        if(err) reject('读取失败')
        resolve(data)
    })
})

// 使用链式回调，避免 回调地狱
p1.then(value=>{
    // 返回一个 新的 promise 对象，方便直接使用 then方法
    return new Promise((resolve,reject)=>{
        fs.readFile('./_13ES/test2.txt',(err,data)=>{
            if(err) reject(err)
            resolve(`${value}\n${data}`)
        })
    })
},
(reason)=>{
    console.error(reason)
}).then(value=>{    // 直接调用 then方法
    return new Promise((resolve,reject)=>{
        fs.readFile('./_13ES/test3.txt',(err,data)=>{
            if(err) reject(err)
            console.log(`${value}\n${data}`)
        })
    })
})
