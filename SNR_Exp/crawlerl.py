import re
import sys
import time
import pandas as pd
import requests
from datetime import datetime
import csv

cookie = '_T_WM=89907987615; XSRF-TOKEN=f3ccb6; WEIBOCN_FROM=1110006030; MLOGIN=0; mweibo_short_token=3a2652d97a; M_WEIBOCN_PARAMS=lfid=102803&luicode=20000174&uicode=20000174'  # 微博 cookie

dataNumber = 300  # 爬取的数据量
allData = []
num = 1
dictTrans = {}
dictComm = {}
names = ""
time2 = time.perf_counter()


# 用于检查文本是否为中文字符
def is_chinese(text):
    for ch in text:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


# 爬虫程序,可以运行

def crawler(url, page):
    global allData  # 声明全局变量allData，用于存储爬取到的数据
    global num  # 声明全局变量num，用于记录爬取到的数据条数
    global time2  # 声明全局变量time2，用于计算程序运行时间
    for i in range(page):  # 遍历指定页数范围
        print(f"开始爬取{names}榜单第{i + 1}页")  # 打印当前爬取的页面信息
        res = requests.get("{}&page={}".format(url, i))  # 发送请求获取页面数据
        data = res.json()['data']['statuses']  # 解析页面数据，提取微博列表
        for singleMess in data:  # 遍历微博列表
            try:
                id = singleMess['user']['id']  # 获取用户ID
                messageid = singleMess['id']  # 获取微博ID
                mid = singleMess['mid']  # 获取微博mid
                username = singleMess['user']['screen_name']  # 获取用户名
                messagetime = singleMess['created_at']  # 获取发布时间
                messagetime = getStandardTime(messagetime)  # 将发布时间转换为标准格式
                message = singleMess['text']  # 获取微博内容
                if not is_chinese(message):  # 如果内容不是中文,则舍弃当前数据
                    print(f"非中文内容: {message}")
                    continue

                like = singleMess['attitudes_count']  # 获取点赞数
                transmit = singleMess['reposts_count']  # 获取转发数

                followers = singleMess['user']['followers_count']  # 获取粉丝数
                read_count = singleMess['number_display_strategy']['display_text']  # 获取阅读数
                int_like = int(like)  # 将点赞数转换为整数
                int_transmit = int(transmit)  # 将转发数转换为整数
                inter = int_like + int_transmit  # 计算点赞数和转发数的和

                transpond = []  # 初始化转发者列表
                halfData = []  # 初始化半完整数据列表
                commentNum = singleMess['comments_count']  # 获取评论数
                data = [commentNum, transmit, like]  # 将评论数、转发数和点赞数存入data列表
                if commentNum != 0 or transmit != 0:  # 如果评论数或转发数不为0
                    if commentNum != 0:  # 如果评论数不为0
                        halfData, commentNum = getCommentInfo(id, mid)  # 获取评论信息
                        data[0] = commentNum  # 更新评论数
                    if transmit != 0:  # 如果转发数不为0
                        transpond, transmit = getTranspondInfo(mid)  # 获取转发信息
                        data[1] = transmit  # 更新转发数
                    singleData = [num, messagetime, id, username, messageid, message, 1, followers, read_count,
                                  inter]  # 构建单条微博数据
                    if halfData is not None:  # 如果半完整数据不为空
                        for i in halfData:  # 遍历半完整数据
                            fullData = singleData + i + data  # 拼接完整数据
                            allData.append(fullData)  # 将完整数据添加到allData列表中
                            progress = ((len(allData) + 1) / dataNumber) * 100  # 计算进度百分比
                            print("\r进度： {}%: ".format(progress if progress <= 100 else 100), end="")  # 

                            # 打印进度信息
                        if len(allData) > dataNumber:  # 如果爬取到的数据条数超过设定值
                            writeToExcelAndTxt()  # 将数据写入Excel和txt文件
                            print(f"运行耗时{time.perf_counter() - time2}")  # 打印程序运行时间
                            sys.exit()  # 退出程序
                    if transpond is not None:  # 如果转发者列表不为空
                        for i in transpond:  # 遍历转发者列表
                            fullData = singleData + i + data  # 拼接完整数据
                            allData.append(fullData)  # 将完整数据添加到allData列表中
                            progress = ((len(allData) + 1) / dataNumber) * 100  # 计算进度百分比
                            print("\r进度： {}%: ".format(progress if progress <= 100 else 100), end="")  # 打印进度信息
                        # print(f"正在爬取第{len(allData)}条数据")
                        if len(allData) > dataNumber:  # 如果爬取到的数据条数超过设定值
                            writeToExcelAndTxt()  # 将数据写入Excel和txt文件
                            print(f"运行耗时{time.perf_counter() - time2}s")  # 打印程序运行时间
                            sys.exit()  # 退出程序
                num += 1  # 更新数据条数
                # else:
                #      NoneData=[num,messagetime,id,username,messageid,message,0,'null',0,'null',0,'null',0,commentNum,transmit,like]
                #      allData.append(NoneData)
                #      print(f"正在爬取第{len(allData)}条数据")
                #      num += 1
                #      if len(allData) > dataNumber:
                #          writeToExcel()
                #          sys.exit()
            except Exception as e:  # 如果发生异常
                # print("")
                print("crawler函数的异常")
                print(f"\r微博获取{e}", end="")  # 打印异常信息
                if len(allData) > dataNumber:  # 如果爬取到的数据条数超过设定值
                    writeToExcelAndTxt()  # 将数据写入Excel和txt文件
                    print(f"运行耗时{time.perf_counter() - time2}")  # 打印程序运行时间
                    sys.exit()  # 退出程序


# 获取转发信息
def getTranspondInfo(id):
    global allData  # 声明全局变量allData
    global num  # 声明全局变量num
    global cookie  # 声明全局变量cookie
    global time2  # 声明全局变量time2
    headers = {  # 设置请求头
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "cookie": cookie
    }
    url = 'https://m.weibo.cn/api/statuses/repostTimeline?id={}&page=1'.format(id)  # 构造请求URL
    res = requests.get(url, headers=headers)  # 发送GET请求
    microblog = []  # 初始化微博列表
    trans_num = 0  # 初始化转发数
    try:
        data = res.json()['data']  # 解析JSON数据
        page = data['max']  # 获取最大页数
        current_page = 1  # 初始化当前页数
        total_number = data['total_number']  # 获取总转发数
        transpondInfo = data['data']  # 获取转发信息
        while trans_num < total_number - 1:  # 当转发数小于总转发数时循环
            if current_page != 1:  # 如果当前页数不为1
                res = requests.get(url, headers=headers)  # 重新发送GET请求
                data = res.json()['data']  # 解析JSON数据
                total_number = data['total_number']  # 更新总转发数
                transpondInfo = data['data']  # 更新转发信息
            else:
                pass
            for single_info in transpondInfo:  # 遍历转发信息
                ReInfo = re.split("//<a href='.*?>@", single_info['text'])  # 分割文本，提取用户名
                Retext = single_info['text']  # 获取转发内容
                like = single_info['attitudes_count']  # 获取点赞数
                mid = single_info['mid']  # 获取微博ID
                Retext_id = single_info['id']  # 获取转发ID
                user_id = single_info['user']['id']  # 获取用户ID
                user_name = single_info['user']['screen_name']  # 获取用户名
                user_messagetime = single_info['created_at']  # 获取发布时间
                commentNum = single_info['comments_count']  # 获取评论数
                user_messagetime = getStandardTime(user_messagetime)  # 将发布时间转换为标准格式
                transpond_flag = 2  # 设置转发标志为2
                transmit = single_info['reposts_count']  # 获取转发数
                # print(transmit)
                # Retext=ReInfo[0]
                user_comment = [user_messagetime, user_id, user_name, Retext_id, Retext, transpond_flag]  # 构建用户评论列表
                microblog.append(user_comment)  # 将用户评论添加到微博列表中
                if commentNum != 0 or transmit != 0:  # 如果评论数或转发数不为0
                    comment = 0  # 初始化评论数
                    transmit_micor = 0  # 初始化转发数
                    commentData = []  # 初始化评论数据列表
                    transpond = []  # 初始化转发数据列表
                    data = [commentNum, transmit, like]  # 构建数据列表
                    if commentNum != 0:  # 如果评论数不为0
                        if dictComm.get(Retext) is None:  # 如果字典中没有该转发内容
                            commentData, comment = getCommentInfo(mid, Retext_id)  # 获取评论数据和评论数
                            dictComm[Retext] = 1  # 将转发内容添加到字典中
                            data[0] = comment  # 更新评论数
                    if transmit != 0:  # 如果转发数不为0
                        if dictTrans.get(Retext) is None:  # 如果字典中没有该转发内容
                            transpond, transmit_micor = getTranspondInfo(mid)  # 获取转发数据和转发数
                            dictTrans[Retext] = 1  # 将转发内容添加到字典中
                            data[1] = transmit_micor  # 更新转发数
                    singleData = [num, user_messagetime, user_id, user_name, Retext_id, Retext, 2]  # 构建单条数据列表
                    if commentData is not None:  # 如果评论数据不为空
                        for i in commentData:  # 遍历评论数据
                            if dictComm.get(i[5]) is None:  # 如果字典中没有该转发内容
                                fullData = singleData + i + data  # 构建完整数据列表
                                allData.append(fullData)  # 将完整数据添加到总数据列表中
                                progress = ((len(allData) + 1) / dataNumber) * 100  # 计算进度
                                print("\r进度： {}%: ".format(progress if progress <= 100 else 100), end="")  # 打印进度
                    if len(allData) > dataNumber:  # 如果总数据量大于设定的数据量
                        writeToExcelAndTxt()  # 写入Excel和TXT文件
                        print(f"运行耗时{time.perf_counter() - time2}s")  # 打印运行时间
                        sys.exit()  # 退出程序
                    if transpond is not None:  # 如果转发数据不为空
                        for i in transpond:  # 遍历转发数据
                            if dictTrans.get(i[5]) == None:  # 如果字典中没有该转发内容
                                fullData = singleData + i + data  # 构建完整数据列表
                                allData.append(fullData)  # 将完整数据添加到总数据列表中
                                progress = ((len(allData) + 1) / dataNumber) * 100  # 计算进度
                                print("\r进度： {}%: ".format(progress if progress <= 100 else 100), end="")  # 打印进度
                        if len(allData) > dataNumber:  # 如果总数据量大于设定的数据量
                            writeToExcelAndTxt()  # 写入Excel和TXT文件
                            print(f"运行耗时{time.perf_counter() - time2}s")  # 打印运行时间
                            sys.exit()  # 退出程序
                    if comment != 0 or transmit_micor != 0:  # 如果评论数或转发数不为0
                        num += 1  # 更新计数器
                trans_num += 1  # 更新转发数
                time.sleep(0.5)  # 暂停0.5秒
            if current_page <= page:  # 如果当前页数小于等于最大页数
                current_page += 1  # 更新当前页数
                url = 'https://m.weibo.cn/api/statuses/repostTimeline?id= {}&page={}'.format(id, current_page)  # 更新URL
            else:
                break
        return microblog, trans_num
    except Exception as e:
        # print("transpondInfo:")
        # print(transpondInfo)
        # print("getTranspondInfo函数的异常")
        print(f"\r转发{e}", end="")
        return microblog, trans_num


# 获取评论信息
def getCommentInfo(id, mid):
    global cookie  # 声明全局变量cookie
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
        "cookie": cookie
    }
    microblog = []  # 初始化微博列表
    comment_num = 0  # 初始化评论数
    try:
        url = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id_type=0'.format(id, mid)  # 构造请求URL
        while True:
            res = requests.get(url, headers=headers)  # 发送GET请求
            data = res.json()['data']  # 解析JSON数据
            max_id = data['max_id']  # 获取下一页评论的max_id
            max_str = 'max_id=' + str(max_id)
            # max_id = 30
            user_info = data['data']  # 获取用户评论信息
            for single_info in user_info:
                Retext = single_info['text']  # 获取评论内容
                Retext_id = single_info['id']  # 获取评论ID
                user_id = single_info['user']['id']  # 获取用户ID
                user_name = single_info['user']['screen_name']  # 获取用户名
                user_messagetime = single_info['created_at']  # 获取评论时间
                user_messagetime = getStandardTime(user_messagetime)  # 将评论时间转换为标准格式
                comment_flag = 1  # 设置评论标志为1
                # 评论时间 用户ID 用户名 评论内容 评论标志
                user_comment = [user_messagetime, user_id, user_name, Retext_id, Retext, comment_flag]  # 构建用户评论列表
                microblog.append(user_comment)  # 将用户评论添加到微博列表中
                comment_num += 1  # 评论数加1
                time.sleep(0.5)  # 暂停0.5秒
            #get_next()
            if max_id != 0:  # 如果还有下一页评论
                url = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id={}&max_id_type=0'.format(id, mid,
                                                                                                        max_id)  # 更新URL
            else:
                break  # 没有下一页评论，跳出循环
        return microblog, comment_num  # 返回微博列表和评论数
    except Exception as e:
        print(f"\r评论{e}", end="")  # 打印异常信息
        return microblog, comment_num  # 返回微博列表和评论数


def cleanData(df):
    message = []  # 创建一个空列表，用于存储处理后的发文/转发内容
    comment = []  # 创建一个空列表，用于存储处理后的转发/评论内容
    for item, item2 in zip(df['发文/转发内容'], df['转发/评论内容']):
        scriptRegex = "]*?>[\\s\\S]*?<\\/script>"  # 定义一个正则表达式，用于匹配script标签
        styleRegex = "<style[^>]*?>[\\s\\S]*?<\\/style>"  # 定义一个正则表达式，用于匹配style标签
        htmlRegex = "<[^>]+>"  # 定义一个正则表达式，用于匹配HTML标签
        spaceRegex = "\\s*|\t|\r|\n"  # 定义一个正则表达式，用于匹配空白字符
        item = re.sub(scriptRegex, '', str(item))  # 去除网址
        item = re.sub(styleRegex, '', str(item))  # 去除样式
        item = re.sub(htmlRegex, '', str(item))  # 去除HTML标签
        item = re.sub(spaceRegex, '', str(item))  # 去除空白字符
        item = re.sub('网页链接', '', str(item))  # 去除“网页链接”字样
        item2 = re.sub(scriptRegex, '', str(item2))  # 对转发/评论内容进行相同的处理
        item2 = re.sub(styleRegex, '', str(item2))
        item2 = re.sub(htmlRegex, '', str(item2))
        item2 = re.sub(spaceRegex, '', str(item2))
        item2 = re.sub('网页链接', '', str(item2))
        message.append(item)  # 将处理后的内容添加到message列表中
        comment.append(item2)  # 将处理后的内容添加到comment列表中
    df['发文/转发内容'] = message  # 将处理后的内容赋值给原始数据框的对应列
    df['转发/评论内容'] = comment  # 将处理后的内容赋值给原始数据框的对应列


def getStandardTime(time):
    GMT_FORMAT = '%a %b %d %H:%M:%S +0800 %Y'  # 定义GMT时间格式
    time = str(datetime.strptime(time, GMT_FORMAT)).split()  # 将输入的时间字符串转换为标准时间格式，并分割为日期和时间部分
    simpleDate = time[0].split("-")  # 分割日期部分，获取年、月、日
    specData = time[1].split(":")  # 分割时间部分，获取时、分、秒
    year = simpleDate[0]  # 获取年份
    month = simpleDate[1]  # 获取月份
    day = simpleDate[2]  # 获取日期
    hour = specData[0]  # 获取小时
    min = specData[1]  # 获取分钟
    second = specData[2]  # 获取秒钟
    return "{}年{}月{}日{}时{}分{}秒".format(year, month, day, hour, min, second)  # 返回格式化后的时间字符串


# 写入excel和txt
def writeToExcelAndTxt():
    print("爬取完成，正在写入Excel和记事本")
    global names
    global allData
    data = pd.DataFrame(allData)  # 将数据转换为DataFrame格式
    data.columns = ['序号', '发文/转发时间(2022年1月1日至今)', '发文/转发用户ID', '发文/转发用户昵称',
                    '发文/转发内容ID', '发文/转发内容', '发文/转发标识', '发文用户粉丝数', '发文用户阅读数', '发文用户互动数',
                    '转发/评论时间(2022年1月1日至今)', '转发/评论用户ID', '转发/评论用户昵称',
                    '转发/评论ID', '转发/评论内容', '转发/评论标识',
                    '评论数', '转发数', '点赞数'
                    ]  # 设置列名,新加粉丝数、阅读数、互动数
    cleanData(data)  # 清洗数据
    data.to_csv(r'.\{}.txt'.format(names), header=None, index=None, sep=' ', mode='w')  # 将数据写入txt文件
    print("写入记事本")
    writer = pd.ExcelWriter('./{}.xlsx'.format(names))  # 创建Excel写入器
    data.to_excel(writer, sheet_name='cx', index=False)  # 将数据写入Excel的cx工作表
    writer.save()  # 保存Excel文件
    writer.close()  # 关闭Excel写入器
    print("写入Excel")


def start():
    urls = [
        # 'https://m.weibo.cn/api/feed/trendtop?containerid=102803_ctg1_5188_-_ctg1_5188',  ## 汽车
        # 'https://m.weibo.cn/api/feed/trendtop?containerid=102803_ctg1_1588_-_ctg1_1588',  ## 美妆
         'https://m.weibo.cn/api/feed/trendtop?containerid=102803_ctg1_4288_-_ctg1_4288',  ## 明星
        # 'https://m.weibo.cn/api/feed/trendtop?containerid=102803_ctg1_2088_-_ctg1_2088',  ## 科技
        # 'https://m.weibo.cn/api/feed/trendtop?containerid=102803_ctg1_4988_-_ctg1_4988',  ## 摄影
        #  'https://m.weibo.cn/api/feed/trendtop?containerid=102803_ctg1_4888_-_ctg1_4888',  ## 游戏
        # 'https://m.weibo.cn/api/feed/trendtop?containerid=102803_ctg1_2688_-_ctg1_2688',  ## 美食
        # 'https://m.weibo.cn/api/feed/trendtop?containerid=102803_ctg1_2588_-_ctg1_2588',  ## 旅行
    ]
    urlsname = [
        # '汽车',
        # '美妆',
         '明星',
        # '科技',
        # '摄影',
        # '游戏',
        # '美食',
        # '旅行',
    ]
    global names
    names = urlsname[0]
    crawler(urls[0], sys.maxsize)


if __name__ == '__main__':
    start()
