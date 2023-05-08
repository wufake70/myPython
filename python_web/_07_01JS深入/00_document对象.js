/*
document对象
    1. document.readyState，返回document加载状态，
        interactive 交互的； complete 完成的

    2.当文档的加载状态改变时，它会触发一个函数，
      该函数会弹出一个警告框显示文档的当前加载状态。
      document.addEventListener("readystatechange",()=>{
        alert(document.readyState)
      })


*/