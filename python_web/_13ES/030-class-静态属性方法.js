// javascript 静态属性、方法 只属于 构造函数对象，不属于 实例对象

class Phone{
    // 静态属性
    static name = '手机';
    static callat(){
        console.log('我是静态方法');
    }
    
    constructor(){
        
    }
}
const p = new Phone;
console.log(Phone.name);
Phone.callat()
console.log(p.name)
