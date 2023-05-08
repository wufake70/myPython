/**
 * 解构赋值:
 *  ES6 允许按照一定模式从数组和对象中提取值，
 *  对变量进行赋值。
 */

// 1.数组的解构赋值
const A = ['小沈阳','刘能','赵四','宋小宝'];
let [a,b,c,d] = A;
console.log("%s\t%s\t%s\t%s\n",a,b,c,d);

// 2.对象解构赋值
const B = {
    name: "赵本山",
    age: 66,
    xiaopin: function(){
        console.log("hello world")
    }
}
// 开始解构赋值
let {name,age,xiaopin} = B;     // 名字必须对应 对象属性名
console.log("%s\t%s\t%s\n",name,age,xiaopin);
xiaopin();
