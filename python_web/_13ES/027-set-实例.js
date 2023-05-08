// 1.数组去重
let arr = [1,1,3,2,2,5,3,4];
let set = new Set(arr);
// 支持 拓展运算符，转换为数组
arr = [...set];
console.log(`${arr}\t${typeof(arr)}`)

// 2.交集
let arr1 = [1,1,3,2,2,5,3,4,89,77];
let arr2 = [1,1,3,2,2,5,3,4,7,6,9];

let arr3 = [...new Set(arr1)].filter((elem)=>arr2.includes(elem))
console.log('交集 %s',arr3)

// 3.并集
let arr4 = [...new Set([...new Set(arr1),...new Set(arr2)])]
console.log('并集 %s',arr4)

// 4.差集,arr1与arr2的差集
let arr5 = [...new Set(arr1)].filter((elem)=> !(arr2.includes(elem)))
console.log('差集 %s',arr5)
