//手机
// 构造函数
function Phone(brand, price) {
    this.brand = brand;
    this.price = price;
}
Phone.prototype.call = function () {
    console.log('我可以打电话');
}
// 继承
function SmartPhone(brand, price, color) {
    Phone.call(this, color) // 继承了 brand,price
    this.color = color;
}
// 设置 子类构造函数的原型
SmartPhone.prototype = new Phone();

let chuizi = new SmartPhone('锤子',2500,'red');
chuizi.call();