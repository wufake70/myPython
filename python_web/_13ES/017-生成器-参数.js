//

function * gen(arg){
    console.log(arg);
    
    let one = yield 1;
    console.log(one)
    
    let two = yield 2;
    console.log()

    yield 3;
}
// 获取迭代器对象
let generator = gen('hello world');
generator.next()
// next方法传入参数，并赋给对应的yield语句
generator.next('参数二')    // 传入第二个参数
generator.next('参数三')    // 。。。
