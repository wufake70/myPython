// 生成器函数是 ES6提供的一种异步编程解决方案，语法行为与传统函数完全不同

// 创建生成器函数
function * gen(){
    console.log('hello generator')
}

// 调用执行
let generator = gen();  // 不会执行
console.log(generator)  // Object [Generator] {}
// 调用 next方法 执行该函数
generator.next()


// 生成器函数代码的分隔符 yield
// yield将 函数中 代码块分为了 四块区域，
function * gen2(){      
    console.log('第一块')

    yield   '第二块';
    console.log(`第二块代码`);

    yield   '第三块';
    console.log(`第三块代码`);
    
    yield   '第四块';
    console.log(`第四块代码`);
    
}

// 每调用一次 next方法，就一次执行没一块的内容
// generator = gen2();
// generator.next()
// generator.next()
// generator.next()
// generator.next()

// for...of 遍历
// for(let g of gen2()){g}
for(let g of gen2()){
    console.log(g);
}
