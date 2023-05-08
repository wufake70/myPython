// 声明变量
let a = 9
console.log(a)

// let 特性

// 1.不支持 重复声明
// let b = "罗志祥"
// let b = "小猪"

// 2.块级作用域，只在大括号(if,else,for,while)内 有用,
// {
//     let c = "hello world"
// }
// console.log(c)

//3.不存在变量提升,
// console.log(d)
// let d = 9999     // 用var关键字 声明，提前调用 返回undefined

//4.不影响作用域链
{
    let e = "尚硅谷";
    function fun(){
        console.log(e)
    }
}
fun()