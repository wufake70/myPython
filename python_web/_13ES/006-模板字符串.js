// ES6 中引入了新的 声明字符串的方法 模板字符串 `...` 反引号

let str = `hello world`;
console.log(str)

// 新特性
// 内容中可以直接 出现 换行符....
// 之前的 字符串 需要使用双引号 去拼接

let str2 = `\thello\nworld`;
console.log(str2);

// 可以 拼接 变量,格式: ${变量名},之前需要使用 加号 拼接
let str3 = 'javascript';
console.log(`hello ${str3}`);
