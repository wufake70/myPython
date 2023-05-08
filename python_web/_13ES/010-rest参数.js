//ES6 引入rest 参数，用于获取函数的实参，用来代替 argum

// function f(){
//     console.log(arguments)
// }
// f(1,2,3,4,5)
// 返回的是 一个对象
// [Arguments] { '0': 1, '1': 2, '2': 3, '3': 4, '4': 5 }

// 声明 rest参数 格式:  ...名称
// 注意：rest参数 必须放到 最后
function f(...args1){
    console.log(args1)
}
f(1,2,3,4,5)
// 返回的是一个数组 [ 1, 2, 3, 4, 5 ]