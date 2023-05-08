/**
 * 适合 读取大文件
 */
var fs = require("fs")


// 流式文件读取
var rs = fs.createReadStream('cs02.txt')
// 监听流的打开...
rs.once("open",()=>{
    console.log("流大开了...");
})

// 每次打开 都会自动关闭(监听每次打开)
rs.on("data",(data)=>{
    console.log(data.length)        // 文件大小
    console.log(data.toString())
})


var ws = fs.createWriteStream('cs03.txt')
// 将可读流数据 写入可写流中。。。
rs.pipe(ws)











