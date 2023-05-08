//
// 模拟获取 用户数据 订单数据 商品数据
function getUsers(){
    setTimeout(()=>{
        let data = '用户数据';
        generator.next(data);   // 将 数据传入 对应yield代码块
    },1000)
}

function getData(){
    setTimeout(()=>{
        let data = '订单数据';
        generator.next(data);   // ....
    },1000)
}

function getGoods(){
    setTimeout(()=>{
        let data = '商品数据';
        generator.next(data)
    },1000)
}

function * gen(){
    let users = yield getUsers();
    console.log(users);

    let data = yield getData();
    console.log(data)

    let goods = yield getGoods();
    console.log(goods)
}

let generator = gen();
generator.next()