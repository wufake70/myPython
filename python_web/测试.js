// ==UserScript==
// @name         014网课视频
// @namespace    http://tampermonkey.net/
// @version      2.0
// @description  try to take over the world!
// @author       wufake
// @match        https://mooc1.chaoxing.com/mycourse/studentstudy*
// @match        https://studyvideoh5.zhihuishu.com/stuStudy*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=chaoxing.com
// @require      https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.6.0.js
// @run-at       document-start
// @grant        unsafeWindow
// ==/UserScript==


window.config = {
    "StudyPlatform":null,
    "cx":"chaoxing",
    "zhs":"zhihuishu",
    "cx_script":null,
    "zhs_script":null
}

var $ = jQuery
var config = window.config

document.addEventListener("readystatechange",()=>{

    config.StudyPlatform = document.URL.includes(config.cx)? "超星学习通":"智慧树";
    console.log(`网课视频:\t\t\t`,`当前学习平台为 ${config.StudyPlatform}`)

    if (document.readyState === "complete"){
        console.log(`网课视频:\t\t\t`,`文档加载完成`)

        if (config.StudyPlatform === "超星学习通"){
            // 章节目录
            var chapter_sp = $("span.posCatalog_name")
            // 最内层 内联框架
            var ifrm = $("#iframe")
            var ifrm2 = null
            var video = null
            var timer = null

            // 回调地狱 获取 video
            timer = setInterval(()=>{
                if (ifrm.get(0)) {
                    console.log(ifrm)
                    clearInterval(timer)

                    timer = setInterval(()=>{
                        ifrm2 = ifrm[0].contentWindow.document.querySelector("iframe")
                        console.log(ifrm2)
                        console.log(Boolean(ifrm2))
                        if (ifrm2){
                            console.log(ifrm2)
                            clearInterval(timer)

                            timer = setInterval(()=>{
                                video = ifrm2.contentWindow.document.querySelector("video")
                                console.log(video)
                                console.log(Boolean(video))
                                if (video){
                                    console.log(video)
                                    clearInterval(timer)
                                    video.play()
                                }
                            },200)
                        }
                    },200)
                }
                ifrm = $("#iframe")
            },200)

            //
            const p = new Promise((resolve,rejcet)=>{
                timer = setInterval(()=>{
                    if (ifrm.get(0)) {
                        // console.log(ifrm)
                        clearInterval(timer)
                        resolve('已获取第一个 iframe')
                    }
                    ifrm = $("#iframe")
                },50)
            })
            p.then((value)=>{
                console.log(value)
                timer = setInterval(()=>{
                    ifrm2 = ifrm[0].contentWindow.document.querySelector("iframe")
                    if (ifrm2) {
                        // console.log(ifrm2)
                        clearInterval(timer)
                        resolve('已获取第二层 iframe')
                    }
                },50)
            }).then((value)=>{
                setInterval(()=>{
                    console.log(value);
                    video = ifrm2.contentWindow.document.querySelector("video")
                    if(video){
                        clearInterval(timer)
                        video.play()
                        resolve("以获取video并完成事件绑定")
                    }
                },50)
            })



        }else{


        }

    }
})