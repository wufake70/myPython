// 创建 toast 容器
const toastContainer = document.createElement('div');
toastContainer.id = 'toast-container';
document.body.appendChild(toastContainer);

// 添加样式
/**
  \n 换行符不会在这里起作用。
   如果你想让 toast 函数中的 msg 参数支持 \n 换行符，
   你需要在 CSS 样式中为 .toast 元素添加 white-space: pre-wrap; 
   样式，以便正确显示多行文本：
 */
const style = document.createElement('style');
style.textContent = `
#toast-container {
    position: fixed;
    bottom: 40%;
    left: 50%;
    transform: translateX(-50%);
    z-index: 9999;
  }

.toast {
  white-space: pre-wrap;
  background-color: #333;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  margin-top: 10px;
}
`;
document.head.appendChild(style);

// 创建 toast 函数
function toast(msg, tduration) {
    // 创建 toast 元素
    const toast = document.createElement('div');
    toast.className = 'toast';
    // html中 \n不能换行
    toast.textContent = msg;

    // 将 toast 添加到容器中
    toastContainer.appendChild(toast);

    // 在一段时间后删除 toast
    setTimeout(() => {
        toastContainer.removeChild(toast);
    }, tduration);
}


// 测试
toast('Hello, World!', 3000);