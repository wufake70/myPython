let str = 'hello world'
const str1 = new String(str);

// 输出字符串内容
console.log(str1.valueOf())

// 使用 for...of遍历字符串
for(let i of str1) console.log(i);