/**
 * 大文件 使用流式文件写入...
 * 
 */

var fs = require("fs")

// 创建一个可写流
var ws = fs.createWriteStream("cs01.txt",{flags:"a"})

ws.once("open",()=>{
    console.log("流打开了");
})
ws.once("close",()=>{
    console.log("流关闭了...");
})

// 可以一直写入 内容
// 异步操作
ws.write("\n可写流写入的内容....")
ws.write("\n可写流写入的内容....")
ws.write("\njfa;iuepkagj;ogkto;qthtakfyaiurkh\dfjkapotihahgjprkahi\afkheopt;qhgru[tgaf;jh;a;h")

// 关闭流
ws.end()




