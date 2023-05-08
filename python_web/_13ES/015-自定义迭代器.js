
// 自定义一个迭代器 遍历对象内的数组

// 声明一个对象
const banji = {
    name: '终极一班',
    students: [
        '小明',
        '小红',
        '小王',
        '小梁',
    ],
    [Symbol.iterator](){ // 迭代器 接口
        let index = 0,
            _this = this;   // 保存 banji对象
        return {
            next: function(){
                if (index < _this.students.length){
                    let result = {value:_this.students[index],done: false}
                    index++;
                    return result
                }else{
                    return {value:undefined ,done: true};
                }
            }
        }
    }
}

