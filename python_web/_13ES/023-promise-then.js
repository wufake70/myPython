// 创建promise对象
const p = new Promise((resolve,reject)=>{
    setTimeout(()=>{
        resolve('成功')
    },1000)
})

// 调用 then方法
const result = p.then((value)=>{
    console.log(value)
    return value    // 将value的值 作为 promise对象的 value属性值
},
(reason)=>{
    console.error('err...')
})
console.log(result)     // then返回的结果也是 Promise 对象

// 链式调用，避免回调地狱
p.then(value=>{
    
},
(reason)=>{
    
}).then(value=>{    // 开启另一个 异步任务

})