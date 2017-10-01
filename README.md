# Jwgl
实现教务系统的成绩查询以及加权平均分和加权绩点计算（中国矿业大学）
## 首先使用splinter.browser进行自动登录
![image](https://github.com/hertless2333/Jwgl/blob/master/image/login.jpg)
## 然后拿到登录的cookie
```
cookie = 'JSESSIONID' + '=' + b.cookies['JSESSIONID']
```
## 对查询成绩的页面进行抓取
```
r = s.post(url, headers = headers, data=postData)
```
## 最后计算得到结果如下
![image](https://github.com/hertless2333/Jwgl/blob/master/image/cal1.jpg)
![image](https://github.com/hertless2333/Jwgl/blob/master/image/cal2.jpg)
