/**
 * 可以使用“arguments”对象来访问传递给函数的可变数量的参数。
 *  “arguments”对象是一个类似数组的对象，其中包含传递给函数的参数。
 * 与形参 无关 
 */


function sum(a){

    var s=0;
    for(var i=0;i<arguments.length;i++){
        s += arguments[i];
        if (i==arguments.length-1) console.log(s),console.log(arguments),console.log(a);
    }
}
sum(1,2,3,4,5)