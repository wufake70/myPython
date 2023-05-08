from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from datetime import datetime
import time,os,re

def init():           # 程序异常时 重新执行该文件
    cur_act = driver.current_activity
    # print(cur_act)
    # print(act_li)
    
    if cur_act in act_li:
        if cur_act == act_li[0]:        # 课程章节详情页面
             os.popen(r'python ./测试04_学习通刷题.py')
             print('1重新执行该程序......')
             exit()
        elif cur_act == act_li[1]:      # 答题界面
            driver.back()
            os.popen(r'python ./测试04_学习通刷题.py')
            print('2重新执行该程序......')
            exit()
        elif cur_act == act_li[2]:      # 火星txt搜题界面
            driver.find_element_by_id('com.fenbi.android.souti:id/input_clear').click()
            driver.press_keycode(187)
            time.sleep(0.5)
            driver.press_keycode(187)
            os.popen(r'python ./测试04_学习通刷题.py')
            print('3重新执行该程序......')
            exit()
        elif cur_act == act_li[3]:      # 搜题结果界面
            driver.back()
            driver.press_keycode(187)
            time.sleep(0.5)
            driver.press_keycode(187)
            os.popen(r'python ./测试04_学习通刷题.py')
            print('4重新执行该程序......')
            exit()


# 火星搜题
def sear_title(title:str):
    driver.press_keycode(187)
    time.sleep(0.3)
    driver.press_keycode(187)    # 切屏
    driver.find_element_by_id("com.fenbi.android.souti:id/edit_text").send_keys(title.split(']')[1])
    driver.find_element_by_xpath("//*[@text='搜索']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@text='复制答案']").click()
    driver.back()
    driver.press_keycode(187)
    time.sleep(0.3)
    driver.press_keycode(187)
    
    return driver.get_clipboard_text()
    

def Hand_Answers(a:str,b:str):
    # a为返回答案
    if "单选" in b:
        b = 1
        if (len(a) == 1) and (a in "abcdABCD"):     # 只有一个字母
            return {'tit_type':b,'an_type':0,'answer':a.capitalize()} # 0 表示字母
        elif '_' not in a:
            for i in 'abcdABCD':                    # 文字 or 字母+文字
                if i == a[0]: 
                    return {'tit_type':b,'an_type':0,'answer': i.capitalize()}
           
            for ii in ',，、\'‘’"“”':
                if ii in a:
                    a = a.split(ii)
                    a = [i.replace('.','') for i in a]
                    a = [i.replace('。','') for i in a]
                    return {'tit_type':b,'an_type':0,'answer':a} 
                
                return {'tit_type':b,'an_type':0,'answer':a.replace('\n','').replace('。','').replace('.','')} 
                        
        else:
            return None

    elif "多选" in b:
        b = 2
        if '_' in a:
            return None
        else:
            return {'tit_type': 2,'answer': a}

    else:
        b = 3   # 判断题
        if (len(a) == 1) and (a in "abcdABCD"):
            return {'tit_type':b,'an_type':0,'answer':a} # 0 表示字母
        elif '_' not in a:
            for i in '对正√✓✔√✓✔':
                if i in a:
                    return {'tit_type':b,'an_type':0,'answer':'A'} # 1 表示文字
            return {'tit_type':b,'an_type':0,'answer':'B'} # 1 表示文字
            
        else:
            return None

def aotu_click(obj:dict,a:int,c=None):
    # obj 处理搜索结果后的数据 
    if(obj):
        if not (obj['tit_type'] == 2):  # 单选、判断
            print("答案为:%s" %obj['answer']) 
            write_log("答案为:%s" %obj['answer'])
            if c:       # 提交页面 的 特例
                options_ = driver.find_elements_by_xpath("//*[@text='A']/../../*[@class='android.view.View']/*[@index='0']")
                options = [i.text for i in options_]
                titles = [i.text for i in c]
                counts = 0
                for i in titles:
                    if '判' in i: counts +=2
                    else: counts +=4

                if counts < len(options):
                    for i in range(len(options) - counts): 
                        options_.pop(0)
                    if len(options_) == 4:
                        for ii in "ABCD":
                            if obj['answer'] == ii: 
                                a = "ABCD".index(ii)
                                e_loca0 = options_[a].location
                                os.system("adb shell input tap %s %s" % (e_loca0['x']+10,e_loca0['y']+20))
                                return

                if type(obj['answer']) == str:
                    try:                # 可能无法匹配
                        
                        
                        e_loca0 = driver.find_elements_by_xpath("//*[@class='android.widget.ListView']//*[@text='%s']" % obj['answer'])[a].location
                        os.system("adb shell input tap %s %s" % (e_loca0['x']+10,e_loca0['y']+20))
                    except:
                        print('该单选题未完成.......')
                        write_log('该单选题未完成.......')
                    
                else:
                    print('该单选题未完成.......')
                    write_log("该单选题未完成......")

            else:       # 提交页面 的 特例
                if type(obj['answer']) == str:
                    try:                # 可能无法匹配
                        e_loca0 = driver.find_elements_by_xpath("//*[@class='android.widget.ListView']//*[@text='%s']" % obj['answer'])[a].location
                        os.system("adb shell input tap %s %s" % (e_loca0['x']+10,e_loca0['y']+20))
                    except:
                        print('该单选题未完成.......')
                        write_log('该单选题未完成.......')
                else:
                    l = len(obj['answer'])
                    for i in obj['answer']:
                        obj['answer'][obj['answer'].index(i)] = i.replace('\n','')
                    try:                # 可能无法匹配
                        if l == 2: e_loca0 = driver.find_element_by_xpath('//*[contains(@text,"%s")]/.[contains(@text,"%s")]' %(obj['answer'][0],obj['answer'][1])).location
                        if l == 3: e_loca0 = driver.find_element_by_xpath('//*[contains(@text,"%s")]/.[contains(@text,"%s")]/.[contains(@text,"%s")]' %(obj['answer'][0],obj['answer'][1],obj['answer'][2])).location
                        if l == 4: e_loca0 = driver.find_element_by_xpath('//*[contains(@text,"%s")]/.[contains(@text,"%s")]/.[contains(@text,"%s")]/.[contains(@text,"%s")]' %(obj['answer'][0],obj['answer'][1],obj['answer'][2],obj['answer'][3])).location
                        os.system("adb shell input tap %s %s" % (e_loca0['x']+10,e_loca0['y']+20))
                    except:
                        print('该单选题未完成.......')
                        write_log('该单选题未完成.......')
                    


        else:       # 多选
            for i in obj:
                print("答案为:%s    *******代码结束后请手动完成********" %obj['answer'].replace('\n',''))
                write_log("答案为:%s    *******代码结束后请手动完成********" %obj['answer'].replace('\n',''))
                
    else:
        print("答案为: 暂无")
        write_log("答案为: 暂无")

# 提交 或 保存
def submit_save():
    driver.swipe(500,1600,500,1000,200)
    driver.swipe(500,1600,500,1000,200)

    submit_btn = driver.find_element_by_xpath("//*[@text='提交']")
    s_b_loca = submit_btn.location
    time.sleep(0.1)
    os.system("adb shell input tap %s %s" %(s_b_loca['x']+10,s_b_loca['y']+20))
    if '未做完' in driver.page_source:
        e = driver.find_element_by_xpath("//*[@text='取消']").location
        os.system("adb shell input tap %s %s" %(e['x']+10,e['y']+20))
        e = driver.find_element_by_xpath("//*[@text='保存']").location
        os.system("adb shell input tap %s %s" %(e['x']+10,e['y']+20))
        e = driver.find_element_by_xpath("//*[@text='确定']").location
        os.system("adb shell input tap %s %s" %(e['x']+10,e['y']+20))
        print("该小节已保存......")
        write_log("该小节已保存......")
    else:
        e = driver.find_element_by_xpath("//*[@text='确定']").location
        os.system("adb shell input tap %s %s" %(e['x']+10,e['y']+20))
        print("该小节已完成......")
        write_log("该小节已完成......")

# 日志记录
def write_log(a:str):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_path = os.getcwd() + '\\appium\测试学习通刷题日志.txt'
    if os.path.exists(file_path):
        pass
    else:file_path = os.getcwd() + '\\测试学习通刷题日志.txt'
    with open(file_path,'a+',encoding='utf-8') as fp:
        fp.write('\n%s:\t' %now)
        fp.write(a)



if __name__ == "__main__":

    pkg_li = [
        'com.chaoxing.mobile',
        'com.fenbi.android.souti',
    ]
    act_li = [
        'com.chaoxing.fanya.aphone.ui.course.StudentCourseActivity',                        # 课程章节详情页面
        'com.chaoxing.fanya.aphone.ui.chapter.detail.ui.ChapterDetailActivity',             # 答题界面
        'com.fenbi.android.module.souti.search.search.TextSearchActivity',                  # 火星txt搜题界面
        'com.fenbi.android.module.souti.solution.textsearch.TextSearchSolutionActivity',    # 搜题结果界面
    ]

    info = {
        "platformName" : "android",
        "platformVersion" : "11.0",
        "deviceName" : "815c1faf",
        # "deviceName":"192.168.0.39:5668",
        # "udid":"192.168.0.39:5668",

        # "appPackage":"com.chaoxing.mobile",
        # "appActivity":".main.ui.MainTabActivity",    
            
        "noReset":True,

        "unicodeKeyboard": False,
        "resetKeyboard": False
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
    os.system("adb shell ime set com.android.adbkeyboard/.AdbIME")
    driver.implicitly_wait(6)
    t_a = TouchAction(driver)

    try:
        while True:
            task_point_li1 = []
            task_point_li2 = []
            # 获取当前界面 章节信息
            task_point_li1 = driver.find_elements_by_xpath("//*[@resource-id='com.chaoxing.mobile:id/content']/*")
            print(len(task_point_li1))
            
            if re.match('\d{1,2}.\d{1,2}',task_point_li1[0].text) is None:
                # 判断 任务点信息
                if (re.match('\d',task_point_li1[0].text)and(len(task_point_li1[0].text)==1)) or (task_point_li1[0].text == ''):
                    pass
                else:
                    task_point_li1.pop(0),print('去除第一个......')
                if not(len(task_point_li1)%3 == 0):
                    for a in range(len(task_point_li1)%3):
                        task_point_li1.pop(-1),print('去除最后一个......')
        
            if re.match('\d{1,2}.\d{1,2}',task_point_li1[1].text) is None: 
                print('去除前两个......')
                task_point_li1.pop(0)
                task_point_li1.pop(0)
            elif re.match('\d{1,2}.\d{1,2}',task_point_li1[-2].text) is None:
                print('去除后两个.....')
                task_point_li1.pop(-1)
                task_point_li1.pop(-1)
            
            print(len(task_point_li1))

            # 将获取到的章节信息 格式化 存储为 字典
            ['' if not (i%3 == 0) else task_point_li2.append({
                                'num':task_point_li1[i].text,
                                'order':task_point_li1[i+1].text,
                                'title':task_point_li1[i+2].text,
                                'location':task_point_li1[i+2].location
                                }) for i in range(len(task_point_li1))]

            for ii in range(len(task_point_li2)-1):
                # 2 没看视频、没做题
                write_log('\n')
                str_1 = "\n%s %s" % (task_point_li2[ii]['order'],task_point_li2[ii]['title'])
                print(str_1)
                write_log(str_1.replace('\n',''))

                # 判断任务点 完成情况
                if not (task_point_li2[ii]['num'] == ''):  

                    try:
                        e_li = [i for i in driver.find_elements_by_xpath("//*[@resource-id='com.chaoxing.mobile:id/tv_icon']")]
                        t_a.tap(e_li[ii]).perform()
                    except:
                        print("再点一次......")
                        # driver.get_screenshot_as_file(os.getcwd() + "\\appium\\报错图%s.png" %(datetime.now().strftime('%H_%M_%S')))
                        # 使用坐标点击
                        # print("%s %s" %(task_point_li2[ii]['location']['x'],task_point_li2[ii]['location']['y']))
                        # t_a.tap(None,task_point_li2[ii]['location']['x'],task_point_li2[ii]['location']['y']).perform() # 不稳定
                        driver.tap([(task_point_li2[ii]['location']['x']+10,task_point_li2[ii]['location']['y']+10)],200)

                    try:
                        # 做题界面
                        driver.find_element_by_xpath("//android.support.v7.app.ActionBar.Tab[@content-desc='章节测验']").click()
                        e1 = driver.find_element_by_xpath("//*[contains(@text,'完成')]").text
                    except:
                        print("没点中.....")
                        driver.tap([(task_point_li2[ii]['location']['x']+10,task_point_li2[ii]['location']['y']+10)],200)
                        driver.find_element_by_xpath("//android.support.v7.app.ActionBar.Tab[@content-desc='章节测验']").click()
                        e1 = driver.find_element_by_xpath("//*[contains(@text,'完成')]").text

                    # 判断是否 完成
                    if "未" in e1:
                        # 开始答题
                        e = driver.find_element_by_xpath("//*[@text='由此作答']")
                        e2 = driver.find_element_by_xpath("//*[@text='章节测验']")
                        driver.scroll(e,e2,800)
                        if '未完成' in driver.page_source: driver.scroll(e,e2,1000)
                        
                        title_li = []
                        finish_count = 0        # 计数器,完成搜题并点击的次数
                        for i in range(5):
                            # 当前页面题目数量
                            t1 = driver.find_elements_by_xpath("//android.view.View[contains(@text,'.[')]/../*[contains(@text,'题]')]")
                            ['' if i.text in title_li else title_li.append(i.text) for i in t1]
                            if ('提交' in driver.page_source) and (len(t1) == 1):
                                if finish_count == 0:
                                    print(title_li[i])
                                    write_log(title_li[i])
                                    result = sear_title(title_li[i])
                                    # print(result)
                                    obj = Hand_Answers(result,title_li[i])
                                    aotu_click(obj,0)
                                    finish_count += 1
                                    break
                                else:
                                    print(title_li[i])
                                    write_log(title_li[i])
                                    result = sear_title(title_li[i])
                                    # print(result)
                                    obj = Hand_Answers(result,title_li[i])
                                    aotu_click(obj,0,t1)
                                    finish_count += 1
                                    break

                            elif ('提交' in driver.page_source) and (len(t1) == 2):
                                if finish_count == 0:
                                    print(title_li[0])
                                    write_log(title_li[0])
                                    result = sear_title(title_li[0])
                                    # print(result)
                                    obj = Hand_Answers(result,title_li[0])
                                    aotu_click(obj,0,t1)
                                    finish_count += 1

                                elif finish_count == 1:
                                    print(title_li[1])
                                    write_log(title_li[1])
                                    result = sear_title(title_li[1])
                                    # print(result)
                                    obj = Hand_Answers(result,title_li[1])
                                    aotu_click(obj,0,t1)
                                    finish_count += 1

                                elif finish_count == 2:
                                    print(title_li[2])
                                    write_log(title_li[2])
                                    result = sear_title(title_li[2])
                                    # print(result)
                                    obj = Hand_Answers(result,title_li[2])
                                    aotu_click(obj,0,t1)
                                    finish_count += 1

                                elif finish_count == 3:
                                    print(title_li[3])
                                    write_log(title_li[3])
                                    result = sear_title(title_li[3])
                                    # print(result)
                                    obj = Hand_Answers(result,title_li[3])
                                    aotu_click(obj,0,t1)
                                    finish_count += 1
                                    
                                print(title_li[-1])
                                write_log(title_li[-1])
                                result = sear_title(title_li[-1])
                                # print(result)
                                obj = Hand_Answers(result,title_li[-1])
                                aotu_click(obj,1,t1)
                                finish_count += 1
                                break
                            elif ('提交' in driver.page_source) and (len(t1) == 3):
                                print(title_li[-2])
                                write_log(title_li[-2])
                                result = sear_title(title_li[-2])
                                # print(result)
                                obj = Hand_Answers(result,title_li[i])
                                aotu_click(obj,1,t1)
                                finish_count += 1
                                print(title_li[-1])
                                write_log(title_li[-1])
                                result = sear_title(title_li[-1])
                                # print(result)
                                obj = Hand_Answers(result,title_li[i])
                                aotu_click(obj,2,t1)
                                finish_count += 1
                                break

                            if len(title_li) == finish_count: break     # 跳出答题页面
                            # 搜答案
                            print(title_li[i])
                            write_log(title_li[i])
                            result = sear_title(title_li[i])
                            # print(result)
                            obj = Hand_Answers(result,title_li[i])
                            aotu_click(obj,0)
                            finish_count += 1

                            # 题目页面 滑动
                            e0 = driver.find_elements_by_xpath("//*[contains(@text,'.[')]")[1].location
                            e1 = driver.find_elements_by_xpath("//*[contains(@text,'题]')]")[0].location
                            p = driver.page_source
                            driver.swipe(e0['x']/2,e0['y'],e0['x']/2,e1['y'],1400)
                            if p == driver.page_source: driver.swipe(e0['x']/2,e0['y'],e0['x']/2,e1['y'],1400)

                        # 提交 或 保存
                        submit_save()

                        act = driver.current_activity
                        driver.back()
                        if act == driver.current_activity: driver.press_keycode(3)
                        
                    else:   # 已完成
                        act = driver.current_activity
                        driver.back()
                        if act == driver.current_activity: driver.press_keycode(3)

            try:
                # 滑动章节页面
                e_li2 = driver.find_elements_by_xpath('//*[@resource-id="com.chaoxing.mobile:id/tv_title"]')
                driver.scroll(e_li2[-2],e_li2[0],4000)
                if "已经到底了" in driver.page_source: print("程序结束.......");break
            except:
                init()
                
    except:
        init()
        


