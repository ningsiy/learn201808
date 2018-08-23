# 爬取双色球数据 Ywx

import urllib
import ssl
import csv
from urllib import request
from bs4 import BeautifulSoup


class GetBorrowInfo:
    def __init__(self, url):
        self.url = url
        self.html = ''
        self.tow_color_data = []
        self.path = './tow_color_data.csv'

    """请求页面"""
    def get_html(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        context = ssl._create_unverified_context()
        request = urllib.request.Request(self.url, headers=header)
        response = urllib.request.urlopen(request, context=context)
        self.html = response.read().decode('UTF-8')
        # print(self.html)

    """解析并获取数据"""
    def get_data(self):
        soup = BeautifulSoup(self.html, 'html.parser')

        """获取总数"""
        lottery = soup.find_all('tr')
        print(len(lottery))
        """获取数据"""
        lo_date = []           # 开奖日期
        lo_period = []         # 期号
        lo_red1 = []           # 红球1
        lo_red2 = []           # 红球2
        lo_red3 = []           # 红球3
        lo_red4 = []           # 红球4
        lo_red5 = []           # 红球5
        lo_red6 = []           # 红球6
        lo_blue = []           # 蓝球
        lo_money = []          # 销售额
        lo_first = []          # 一等奖
        lo_second = []         # 二等奖
        for date in lottery:
            td = date.find_all('td')
            if len(td) > 1:
                lo_date.append(td[0])
                lo_period.append(td[1])

                # 获取中奖号码
                em = date.find_all('em')
                lo_red1.append(em[0])
                lo_red2.append(em[1])
                lo_red3.append(em[2])
                lo_red4.append(em[3])
                lo_red5.append(em[4])
                lo_red6.append(em[5])
                lo_blue.append(em[6])

                # 获取销售额、一等奖注数、二等奖注数
                strong = date.find_all('strong')
                lo_money.append(strong[0])
                lo_first.append(strong[1])
                lo_second.append(strong[2])
        # print(len(lo_second))

        """组装数据信息"""
        # index = 0
        for index in range(0, len(lo_date)):
            data = [
                lo_date[index].text.replace(' ', ''),
                lo_period[index].text.replace(' ', ''),
                lo_red1[index].text.replace(' ', ''),
                lo_red2[index].text.replace(' ', ''),
                lo_red3[index].text.replace(' ', ''),
                lo_red4[index].text.replace(' ', ''),
                lo_red5[index].text.replace(' ', ''),
                lo_red6[index].text.replace(' ', ''),
                lo_blue[index].text.replace(' ', ''),
                lo_money[index].text.replace(' ', ''),
                lo_first[index].text.replace(' ', ''),
                lo_second[index].text.replace(' ', ''),
            ]
            self.tow_color_data.append(data)
            # index += 1

            # 防止列表下表溢出
            # if index >= len(name_txt):
            #     break
        print(len(self.tow_color_data))

    """写入文件"""
    def create_file(self, header=['开奖日期', '期号', '红球1', '红球2', '红球3', '红球4', '红球5', '红球6',
                                  '蓝球','销售额(元)','一等奖注数','二等奖注数']):

        with open(self.path, 'w', newline='', encoding='utf-8-sig') as file:
            write_file = csv.writer(file, 'excel')
            if header is not None:
                write_file.writerow(header)
            for row_data in self.tow_color_data:
                write_file.writerow(row_data)
            print("数据写入文件成功！" + self.path)


if __name__ == '__main__':

    page = 2

    for p in range(1, page+1):
        url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' + str(p) + '.html'
        borrow = GetBorrowInfo(url)
        borrow.get_html()
        borrow.get_data()
        if p == page:
            borrow.create_file()


