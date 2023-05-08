
const school = {
    name: "尚硅谷",
    cities: ['北京','上海','深圳'],
    course: ['前端','java','大数据','运维']
}

console.log(`获取所有的键名: %s`,Object.keys(school))
console.log(`获取所有的值: ${Object.values(school)}`)

// entries方法 返回 大数组，属性名、对应属性值 放在同一个数组里
console.log(Object.entries(school))

// 创建 map
const m = new Map(Object.entries(school))
console.log(m.get('name'))