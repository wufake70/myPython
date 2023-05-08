// 生成器可以实现 异步编程
// 1s后输出 111,2s后输出 222,3s后输出 333

// 纯用定时器
// '回调地狱' 即为了实现某个 某个逻辑 写出了 层层嵌套的回调函数
// 可读性极差
// setTimeout(()=>{
//     console.log(111);
//     setTimeout(()=>{
//         console.log(222);
//         setTimeout(()=>{
//             console.log(333);
//         },1000)
//     },1000)
// },1000)


// 使用生成器函数，可读性高
// 创建对应三个函数
function one(){
    setTimeout(()=>{
        console.log(111)
        generator.next()    // 自动调用 下个yield代码块
    },1000)
}
function two(){
    setTimeout(()=>{
        console.log(222)
        generator.next()
    },2000)
}
function three(){
    setTimeout(()=>{
        console.log(333)
    },3000)
}
// 创建 生成器函数,
function * gen(){
    yield one();
    yield two();
    yield three();
}

let generator = gen();
generator.next()