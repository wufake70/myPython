var a = 1

d = new Date()

c = d.getTime()


// 绑定 最常见的 鼠标移动事件
document.onmousemove = function () {            // Document is not focused 文档未聚焦
    d = new Date()
    
    if (d.getTime() > c+1000)
    {
        
        if (document.hasFocus())            // 判断 是否 聚焦。
        {

            try {

                navigator.clipboard.writeText('第'+ a +'次破坏剪贴板')  // Clipboard write was blocked due to lack of user activation. 用户未激活

            }catch{   // 上面的报错 不能捕获。

                console.log('用户未激活。。。')
                return false

            }
            a +=1
            c = d.getTime()
        }
    }
  
}





































