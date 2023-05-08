// 可以使用 JavaScript 来监听页面上的复制、剪切和粘贴事件。下面是一个简单的例子，它演示了如何监听页面上的这些事件：

document.addEventListener('copy', (event) => {
    console.log('复制事件触发');
});

document.addEventListener('cut', (event) => {
    console.log('剪切事件触发');
});

document.addEventListener('paste', (event) => {
    console.log('粘贴事件触发');
});
// 上面的代码使用了 addEventListener 方法来