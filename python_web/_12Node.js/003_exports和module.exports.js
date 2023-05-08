/**
 * exports.xxx 和module.exports.xx 都可向外 导出变量
 * 
 * 但是 exports = {
 *  name: "hi",
    age: 66,
    Sayhi: function() {
        console.log("hi node.js")
    }
 * }   不行，此操作 是 修改 exports 指向的 对象
 */

exports.name = "波多野结衣"
exports.age = 38
exports.Sayhi = function()
{
    console.log('hello node.js')
}
module.exports = {
    name: "hi",
    age: 66,
    Sayhi: function() {
        console.log("hi node.js")
    }
}


