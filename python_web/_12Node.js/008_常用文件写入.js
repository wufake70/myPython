/**
 * 
 */

// 异步
var fs = require("fs")
fs.writeFile("cs01.txt", "\n008写入的内容...", {encoding:"utf-8",flag:"a"}, (err) => {

    if(!err) {
        console.log("写入成功...");

    }
    else{
        console.log("写入失败...");
    }
})

// fs.writeFileSync()











