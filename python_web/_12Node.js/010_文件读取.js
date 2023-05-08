/**
 * 
 */

var fs = require("fs")


// 简单文件读取
fs.readFile("cs01.txt",{flag:"r"},(err,data)=>{      // 异常优先,data 是buffer对象,调用toString方法 即可输出字符串
    if(!err){
        console.log(data.toString());

        fs.writeFile('cs02.txt',data,(err)=>{
            if(!err){
                console.log("写入成功....");
            }
        })

    }
})







