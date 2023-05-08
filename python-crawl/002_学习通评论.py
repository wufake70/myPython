# _*_coding :utf-8 _*_
# @Time :2022/10/8 20:48
# @File : 002_
# @Project : python-crawl
import json
import pprint
import requests

def fun(value):
    # 获取 学习通的课题讨论，全部评论(内含动态加载)
    url = 'https://groupweb.chaoxing.com/course/topicDiscuss/51de7583de4a03adca2dfe83e801ba76' \
          '/aca03a5a8c534c81b8f87240d1376ef0_topicDiscuss/getReplyList?order=1&kw=&lastValue='+value

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
        "Referer": "https://groupweb.chaoxing.com/",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://groupweb.chaoxing.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Cookie": "fid=29385; lv=4; _uid=202644922; uf=da0883eb5260151ec2421b81641f1f22666bb340f9bcbb08fc8262cbd8093e25adb8a61529dc093e4a10871310cdefad6072530a316e7a7e88b83130e7eb4704649a629b576a377ab9a0fbca4fa47fbd4129e2925200b376ea07904cc6d577feb7be6a7fd388f553e7fafd565af53bf2; _d=1664926928892; UID=202644922; vc=A69AB3ACFF121D3B73775D21D8113CE8; vc2=07676F20B154AC0CF9D8461075748420; vc3=fCpv9cRFP5QUr1FzZmwPmK%2Bgv68aMUMAzoFXfys4Fzwq4S%2FTExvpJkyMZS0N0Y7wp9X5qub1dxad6MlWU5kBosvy75axi1qpnWW7AhFZh235gnG5BByKPBaWFojEOq%2Fu2avGHZ0L%2FZIixGHOi0Gbt1vB5%2BwkaA4I0EA6hCCN4GY%3D96b532844cbecf6b4fadf6fb0747bb06; xxtenc=43b8860ad285905a1eebbb1dda40f743; DSSTASH_LOG=C_38-UN_28100-US_202644922-T_1664926928894; _industry=9; web_im_hxToken=YWMtdQ8bVkcGEe25ekHy%5fbvns6KlE4D%2d6RHksYgJxSsb8jIT2%5fYQHmcR7JA3HdOUd%2d3lAwMAAAGDt5zqpTht7EBSHde8ov%5f0732kN5sOfpJEaQ68dtrVTe0K9ASZs85NnA; web_im_tid=133546776; web_im_pic=http%3a%2f%2fphoto%2echaoxing%2ecom%2fp%2f202644922%5f80; web_im_name=%u9648%u4eae; KI4SO_SERVER_EC=RERFSWdRQWdsckNwckxwM2pXeFFSVFp1SmgyWjBpMUxXWnY1bTZWRkJkT0FZZThlVlpoY2JGTjIr%0AMUl6dnV5SERtU2djWlRjU2NTVQp1NG13bWtscWxRRjJXK3FTUXlMU0U2QmhUMy9FbGVVN3dlclJt%0ARDFtdWE0OVd4bXBHSTZoQ1dxczczNElsTkZJNWg5V2xJS2NHa2xPCjhKbkRyZHlUR0VtZFd5Z1F3%0AdU5kY1VEUWlPR2o5UE5OU3pNajNvY29hcU12bVBycExsckV6TWJLYkEvdFhVaTgwMTYzRHRKZUd2%0ARUgKaW55cFE3ZW1aNW9oUGRsVWp6SHVORHFmVXE1ZE4veGZpTjlqRkxtNHhqSllPL3Q1STBLbUxW%0ASTBDK0ZjdUlETU1FSFVXTERSeUlKOApmdjFZd21mc0o4YndwZDBQTTN1VGh6VmJrblFqRXNucjB4%0ANmxoQXFUK1VoWHVsWDRxdTNZY0VYODkzQmIxeEIvZ1F1NCtMaUF6REJCCjFGaXcwY2lDZkg3OVdN%0ASm43Q2ZHOEtYZEQ5S0Y0RlI4bFpQcy9nQ2dHcHc2MTVQandySXhEY1BUSFZucEx4ZGxYWU0yNmJz%0Aa1RDaWYKQnpFPT9hcHBJZD0xJmtleUlkPTE%3D; _tid=133546776; sso_puid=202644922; thirdRegist=0; JSESSIONID=223969CC4CFF35791290CD8D86918DEC.NoteService; route=92194d6013924571a79e64c21735f920",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
    }

    print('开始发送请求......')
    response = requests.get(url, headers=headers).text

    print('解析数据')
    text_obj = json.loads(response)
    pprint.pprint(text_obj['datas'])

    # 动态加载的 参数
    try:
        return text_obj['poff']['lastValue']  # 获取不到的值 ,报错，返回None
    except:
        print('这已经是最后一个了')


if __name__ == "__main__":
    a = 'null'
    while a:  # 最后一个值 为None，停止循环
        # print(a)
        a = str(a)
        a = fun(a)

    # 注意: 当发送请求后 程序会被阻塞(i/o阻塞)，会等待 接收数据包





