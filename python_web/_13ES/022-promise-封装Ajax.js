// api https://api.apiopen.top/getJoke

// 没有使用 promise封装
// 创建对象
// const xhr = new XMLHttpRequest();
// // 初始化
// xhr.open('get', 'https://www.baidu.com')
// // 发送
// xhr.send()
// xhr.onreadystatechange = () => {
//     if (xhr.readyState === 4) {
//         if (xhr.status >= 200 && xhr.status <= 300) {
//             //成功 请求
//             console.log(xhr.response)
//         } else {
//             // 失败
//             console.error(xhr.status)
//         }
//     }
// }


// 使用 promise封装
const p = new Promise((resolve,reject)=>{
    const xhr = new XMLHttpRequest();
    // 初始化
    xhr.open('get', 'https://www.baidu.com')
    // 发送
    xhr.send()
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            if (xhr.status >= 200 && xhr.status <= 300) {
                //成功 请求
                resolve(xhr.response)                
            } else {
                // 失败
                reject(xhr.status)
            }
        }
    }

})
p.then((value)=>{
    console.log(value)
},
(reason)=>{
    console.log(reason)
})
