/**
 * 文件的写入
 * 
 * 
 * 
 */

var fs = require("fs\
")

// console.log(fs);


// 同步文件写入 
// 打开文件
// var fd = fs.openSync("cs01.txt","w")     // 存在返回值 console.log(a)
// 写入内容
// fs.writeSync(fd,"hello world")
// 关闭文件
// fs.close(a)


// 异步 文件写入 
// 异步方法 不可能有返回值
// 多了一个回调函数，两个 参数 err 正常为null、fd
fs.open("cs01.txt", "a",
    (err, fd) => {
        if (!err) { 
            console.log("文件正常打开...");

            //异步写入
            fs.write(fd,"异步写的内容...",
            (err)=>{    // err 正常为 null
                if(!null){
                    console.log("写入成功...");
                }
                else{
                    fs.close(fd)
                }

            })
        }
        else {
            console.log(err);
        }
    })


console.log('结束...');



