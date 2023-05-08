/**
 * buffer 缓冲区
 *      - buffer的结构和数组很像，操作方法也类似
 *      - 数组中不能存储二进制的文件(音乐、视频)，但buffer可以
 *      - buffer中 存储的都是二进制数据，但显示时以十六进制显示
 *      - buffer的大小 一旦确定 不能修改
 *  */


var buf = Buffer.from("9999");
console.log(buf.length)     // 占用内存大小

// 创建一个 10个字节 buffer
var buf2 = Buffer.alloc(10);
console.log(buf2.length)

buf2[0] = 257       // 所存储的元素大小 不超过 255
buf2[1] = 255
buf2[10] = 255

console.log(buf2[0],'\n',buf2[1],'\n',buf2.length)

// 使用tostring方法 将缓冲区的数据转换为 字符串
var buf3 = Buffer.from("你好 node.js")
console.log(buf3.toString()) 
