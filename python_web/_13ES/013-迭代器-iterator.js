/**
 * 迭代器 是一种接口，为各种不同的数据结构提供统一的访问机制。
 * 任何数据结构只要部署了 iterator接口(对象的一个属性)，就可以完成遍历操作。
 * 
 * ES6创造了一种新的遍历命令 for...of循环， Iterator接口主要供 for...of消费
 * 原生具备 iterator接口的数据 (可用 for of遍历 )
 *  a) Array
    b) Arguments
    c) Set
    d) Map
    e) String
    f) TypedArray
    g) NodeList
 */

// 声明一个数组
const xiyou = ['唐僧','孙悟空','猪八戒','沙僧'];

// 使用for...of 遍历 
for(let i of xiyou) console.log(i);
// 原理
// 获取数据接口,创建指针对象，指向当前数据结构的起始位置
let iterator = xiyou[Symbol.iterator]();
// 首次 调用 其next方法，指针自动指向第一个元素
console.log(iterator.next())
// 指针往后推移，next方法 返回一个包含value和done属性的对象
console.log(iterator.next())
