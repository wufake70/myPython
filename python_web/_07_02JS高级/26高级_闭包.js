
// 闭包 是如何 产生的?  当嵌套函数 中 引用了外部函数的变量时 就产生 闭包。

function fun1() {
    var a = 999,
        b = 888;

    function fun2(){        // 闭包函数，产生了闭包
        console.log(a);     // 引用 外部函数的 变量
        console.log(b);

    }

    return fun2;
}

var fun3 = fun1() // 外部函数 要调用

fun3()

// 常见闭包 1， 将内部函数 作为 外部函数的 返回值 返回

function fun4(){
    var a = 0;

    function fun5(){    // 产生了 一个闭包函数
        a++;
        console.log(a);
    }

    return fun5;    // 将内部函数 作为 外部函数的 返回值 返回
}

var F1 = fun4();    // 将F1 指向 闭包函数对象，函数的局部变量 不会消失        
F1()    //输出 1，第一次 调用闭包函数
F1()    //输出 2，第二次 调用



// 常见闭包 2，

function showmsg(msg,time){
    setTimeout(()=>{    // 产生了闭包
        console.log(msg);   // 引用外部函数的 变量

    },time)
}
showmsg("hello world", 3000)


// 闭包的作用
/**
 * 在 函数 执行完后，局部变量就会自动消失..
 * 1.闭包作用就是 延长局部变量 生命周期
 * 2.可在函数外部 操作 函数内部的变量
 */


// 闭包的应用 js模块化

// 闭包的缺点，内存一直被占用
/**
 * 内存溢出: 当程序所需的内存 超过 剩余的内存时，就会出..... 
 * 例如:
 * var obj = {}
 * for(var i=0;i<10000000;i++){
 *  obj[i] = new Array(10000000);
 * }
 * 
 * 内存泄露: 占用的内存 没有被及时释放(闭包)....
 * 内存泄露过渡 就会导致 内存溢出
 * 
 */











