# _*_coding :utf-8 _*_
# @Time :2022/8/8 18:55
# @File : 17_进程和线程
# @Project : python_ubuntu_progress

import time
import multiprocessing

# 进程 是系统资源的 最小单位，
# 线程 是CPU 调度 的最小单位。


"""
def now_t():
    return time.ctime()
    

def func():
    print('内部--开始', now_t())
    time.sleep(3)
    print('内部--结束', now_t())


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=func)       # 实例化 一个多进程 对象
    p1.start()                                      # 开启 该进程
    print('外部--开始', now_t())
    time.sleep(3)
    print('外部--结束', now_t())
    
多线程模块 类似 多进程模块。
    
注意： 1.Python里的 多进程 是并发执行的(分配 时间片)，只不过 时间片很小 ，切换执行 的时间 很快，很像同时进行一样。
        所以 以上代码 运行时间 总共三秒
        
       2.if __name__ == '__main__'的意思是： 
       当.py文件被直接运行时，if __name__ == '__main__'之后 的代码块将被运行；
       当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
       
       3.multiprocessing.Process(target=func, args=(x,)  
        向目标函数 传参数 元祖形式 单个参数(x,)
        
       4.把 不是 创建类、函数的代码 都写在  if __name__ == '__main__': 后面。
       5.并行 只是 Python层面的，电脑实际上 是 并发的。
       6.每个进程拥有 自己的地址空间，内存，数据栈
       7.各个进程相互独立，互不影响。
       8.多进程 适合 计算密集型 (需要在用大量的 CPU资源)
       
       9.线程 不占用 额外的 系统资源(进程内)
       10.多线程适合 IO密集型的场景(频繁的进行数据收发)，
         Python的 多线程 会自动切换到非阻塞的线程上去。
         如: 多线程下载
        
       11.# 线程 是在 进程内 运行的，消耗进程内 资源

"""




























