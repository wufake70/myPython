"""
1. return可以返回0个，一个，多个返回值
    0个，默认为None值
    多个值时，实际上返回一个tuple
        def fun(a,b,c):
            return a,b,c

        print(type(fun(1,2,3))) # <class 'tuple'>
        print(fun(1,2,3))       # (1, 2, 3)

2. 参数类型
    位置参数：
        例如，下面的函数 add(x, y) 中的 x 和 y 都是位置参数：
        def add(x, y):
            return x + y
        # 调用该函数时，必须按照 add(x, y) 中 x 和 y 的顺序传递参数：
        result = add(1, 2)  # 传递两个位置参数
        print(result)  # 输出 3

    默认参数：
        默认参数是指在函数定义中给参数赋初始值的参数。
        例如，下面的函数 print_info(name, age=18) 中的 name 是位置参数，age 是默认参数：
        def print_info(name, age=18):
            print("Name:", name)
            print("Age:", age)
        # 调用该函数时，可以只传递位置参数，也可以传递位置参数和默认参数：
        print_info("Alice")  # 只传递位置参数
        print_info("Bob", 20)  # 传递位置参数和默认参数

    可变位置参数：
        可变位置参数是指在函数定义中以 * 开头的参数，表示该参数可以接受任意数量的位置参数，并将这些参数以元组的形式传递给函数。
        例如，下面的函数 sum_numbers(*numbers) 中的 *numbers 是可变位置参数：
        def sum_numbers(*numbers):
            result = 0
            for number in numbers:
                result += number
            return result
        # 调用该函数时，可以传递任意数量的位置参数：
        result = sum_numbers(1, 2, 3, 4, 5)  # 传递多个位置参数
        print(result)  # 输出 15

    可变关键字参数：
        可变关键字参数是指在函数定义中以 ** 开头的参数，
        表示该参数可以接受任意数量的关键字参数，并将这些参数以字典的形式传递给函数。
        例如，下面的函数 print_info(name, **kwargs) 中的 **kwargs 是可变关键字参数：
        注意: 关键字 不要与 形参名重复
        def print_info(name, **kwargs):
            print("Name:", name)
            for key, value in kwargs.items():
                print(key + ":", value)
        # 调用该函数时，可以传递任意数量的关键字参数：
        print_info("Alice", age=18, city="Beijing")  # 传递多个关键字参数

        
3. 传参数顺序：位置参数，默认参数，可变位置参数，可变关键字参数
    传入的默认参数，可相互交换位置

4. 在函数内定义变量都为局部变量,不论 其类型 是 字符串，数值，组合数据类型
    ，要想在 函数内 操作全局变量，需要 global声明，否则 都只在函数内有效

    
5.默认参数为 可变对象([],(),{}),函数体内 可操作参数，每次使用默认参数调用函数，默认参数 都会改变
    def func(x=[],y=[6,7]):
        x.append(8)
        y.append(8)
        return (x+y)
    a,b = [1,2],[3,4]
    t=func(x=a)     # 没有传入 y参数，函数结束后 默认参数y 为[6,7,8] 
    t=func(y=b)     # 没有传入 x参数，函数结束后 默认参数x 为[8] 
    print(func(),end=';')

"""

def func(x=[],y=[6,7]):
    x.append(8)
    y.append(8)
    return (x+y)
a,b = [1,2],[3,4]
t=func(x=a)
t=func(y=b)
print(func(),end=';')