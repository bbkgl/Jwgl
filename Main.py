import requests
import json
import xlwt
from login import Login

s = requests.session()  #测试获取cookies
login = Login()

url = 'http://202.119.206.62/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N305005&queryModel.showCount=100&queryModel.currentPage=1&queryModel.sortName=&queryModel.sortOrder=asc&time=0'

excel = xlwt.Workbook()  #创建excel对象
sheet1 = excel.add_sheet('Chegji', cell_overwrite_ok=True)

postData = {
    # 'xnm': "2016",  #学年开始的年份
    # 'xqm': "12",    #对应第几学期，3表示第一学期，12是第二学期
}

headers = {
    'cookie': login.submit(),   #cookie值是临时获得生成的
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

r = s.post(url, headers = headers, data=postData)
# cookies=requests.utils.dict_from_cookiejar(r.cookies)   #获取cookie的方式
# print(cookies)
js = json.loads(r.text)
sheet1.write(0, 0, '科目')
sheet1.write(0, 1, '成绩')
sheet1.write(0, 2, '学分')
sheet1.write(0, 3, '绩点')
print(js['items'][0]['xm'], js['items'][0]['bj'])
print("所有科目共有{}条记录".format(len(js['items'])))
count = 0
jqCj = []
tplt = "{:^6}\t{:^6}\t{:^6}\t{:^20}"
print(tplt.format( "学分", "成绩", "绩点", "科目"))
for infor in js['items']:
    if infor['kcxzmc'] != "通识教育公选课" and infor['kcxzmc'] != "素质教育课":
        if infor['cj'] == '良好':
            infor['cj'] = 80
        elif infor['cj'] == '优秀':
            infor['cj'] = 90
        print(tplt.format( infor['xf'], infor['cj'], infor['jd'], infor['kcmc']))
        jqCj.append([float(infor['xf']), float(infor['cj']), float(infor['jd'])])
    sheet1.write(count, 0, infor['kcmc'])
    sheet1.write(count, 1, infor['cj'])
    sheet1.write(count, 2, infor['xf'])
    sheet1.write(count, 3, infor['jd'])
    count += 1

def jiaQuan(list):
    allGrade = 0
    allJd = 0
    allXf = 0
    for kc in list:
        allGrade += kc[0] * kc[1]
        allJd += kc[0] * kc[2]
        allXf += kc[0]
    print("加权平均分{:.2f}".format(allGrade/allXf))
    print("加权绩点{:.2f}".format(allJd/allXf))
print("\n除选修外的科目共{}条".format(len(jqCj)))
jiaQuan(jqCj)
excel.save('Chengji-Zoujiakun.xls')