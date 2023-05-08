const { rejects } = require("assert")

const p = new Promise((resolve,reject)=>{
    setTimeout(()=>{
        //设置为失败的状态
        reject('出错了...')
    })
})

// 使用then方法 
// p.then(value=>{},
//     reason=>{
//         console.error(reason)
//     })

// 使用catch 方法,只用指定失败的回调函数 
p.catch(reason=>{
    console.warn(reason)
})