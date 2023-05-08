/*
rest 参数与spread拓展运算符 在ES6中已经引入，
不过ES6中只针对于数组，
ES9中 为对象提供了 向数组一样的 rest参数和拓展运算符；
*/

// 将对象中 多余的参数 全部放在 user属性名内 (user 指向 新的对象)
function connect({ host, port, ...user }) {
    console.log(`${host}\n${port}\n${Object.values(user)}`);
}

connect({
    host: 'localhost',
    port: 3306,
    username: 'wugeek',
    password: 'qwe123',
    type: 'master'
})