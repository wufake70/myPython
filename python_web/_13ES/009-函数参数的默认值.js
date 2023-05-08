// ES6 允许给函数参数复初始值
// 1.形参初始值，规范: 默认参数一般放在 最后
const add = (a=0,b=0,c=10)=> a+b+c;
console.log(add());

// 与解构赋值结合,要先传入 对象
function connect({host='127.0.0.1',username,password}){
    console.log(`主机: ${host}\n用户: ${username}\n密码: ${password}`);
}
connect({
    host: 'localhost:port',
    username: 'root',
    password: 'qwe123'
})
