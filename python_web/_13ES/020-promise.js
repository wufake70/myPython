/**
 * Promise是 ES6引入的异步编程的 新解决方案 。
 * 语法上 Promise是一个构造函数，
 * 用来封装异步操作并可以获取其成功或失败的结果。
 * 
 */

// 创建 promise对象
const p = new Promise((resolve,reject)=>{
    setTimeout(()=>{
        // 成功
        // let data = '数据库中数据'
        // resolve(data);

        // 失败
        let err = '操作失败'
        reject(err)
    },1000);
})

// 调用promise对象的then方法
// then方法 是 Promise 中用于处理异步操作结果的方法
p.then((value)=>{
    console.log(value)
},
(reason)=>{
    console.log(reason)
})


