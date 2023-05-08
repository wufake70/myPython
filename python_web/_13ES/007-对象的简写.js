// ES6允许在大括号里，直接写入变量和函数，作为对象的属性和方法。

let name = '尚硅谷',
    change = function(){
        console.log(`我们可以改变你！！！`);
    }

const A = {
    name,   // 等效于 name: name,
    change,
    advanced(){     // 直接声明函数
        console.log(`提高技能`);    
    },
    age: 99
}
console.log(`${A.name}\t${A.age}`);
A.change();
A.advanced();
