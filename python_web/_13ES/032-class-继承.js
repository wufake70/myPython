// class 继承 同构造函数继承 一样

// 父类
class Phone{
    constructor(brand,price){
        this.brand = brand;
        this.price = price;
    }
    callat(){
        console.log('我可以打电话');
    }
}
// 子类
class SmartPhone extends Phone{
    constructor(brand,price,color){
        super(brand,price);     // 继承父类的 constructor
        this.color = color;
    }
    // 子类新方法
    photo(){
        console.log("拍照");
    }
}

let 小米 = new SmartPhone('小米',8888,'red')
小米.callat();
小米.photo()