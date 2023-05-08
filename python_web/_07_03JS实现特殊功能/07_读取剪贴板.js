navigator.clipboard.readText().then(

    clipText => document.querySelector(".cliptext").innerText = clipText)

// 注意事项: 火狐 需在 about:config页面将 dom.events.asyncClipboard.readText 设置为true



