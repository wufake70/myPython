/*
ES6 提供了更接近传统语言的写法，引入了 Class（类）这个概念，作为对
象的模板。通过 class关键字，可以定义类。基本上， ES6 的 class可以看作只是
一个语法糖，它的绝大部分功能， ES5 都可以做到，新的 class写法只是让对象
原型的写法更加清晰、更像面向对象编程的语法而已。
知识点：
    1) class声明类
    2) constructor定义构造函数初始化
    3) extends继承父类
    4) super调用父级构造方法
    5) static定义静态方法和属性
    6) 父类方法可以重写
*/

// ES6类 实现的功能 在ES5中 用 构造函数都可以实现
// 构造函数
/*
function Phone(brand,price){
    this.brand = brand;
    this.price = price;
}
Phone.prototype.call = function(){
    console.log('我可以打电话')
}
// 实例化对象
let Huawei = new Phone('Huawei',6555);
Huawei.call()
*/

// class
class Phone{
    
    // 构造方法 名字不能修改
    constructor(brand,price){
        this.brand = brand;
        this.price = price;
    }

    // 成员方法
    callat(){
        console.log('我可以打电话');
    }
}

iphone = new Phone('iphone',8888)
iphone.callat()

