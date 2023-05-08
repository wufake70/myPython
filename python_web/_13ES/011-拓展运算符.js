// ... spread拓展运算符 能将数组 转换为逗号分割的 参数序列
const tfboys = ['易烊千玺','王源','王俊凯']

// 声明一个函数
function fun(){
    console.log(arguments)
}

fun(tfboys)         // [Arguments] { '0': [ '易烊千玺', '王源', '王俊凯' ] }
fun(...tfboys)      // [Arguments] { '0': '易烊千玺', '1': '王源', '2': '王俊凯' }
// 相当于 将['易烊千玺','王源','王俊凯'] 转换成 '易烊千玺', '王源', '王俊凯'

// 应用 数组合并
li1 = [1,2,3]
li2 = [4,5,6]
li3 = [...li1,...li2]
console.log(li3)

// 数组克隆
li4 = [...li3]

// 伪数组 转 真数组
li5 = document.querySelectorAll('....')     // 获取节点列表(伪数组)
li6 = [...li5]