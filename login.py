from splinter.browser import Browser

class Login(object):
    def __init__(self):
        self.txtUserName = '******'  #用户名
        self.TextBox2 = '******' #密码
        self.txtSecretCode = ''      #验证码
        self.postData = {
            'yhm':self.txtUserName,
            'mm':self.TextBox2
        }

    def submit(self):
        b = Browser(driver_name="chrome")
        b.visit("http://202.119.206.62/jwglxt/xtgl/login_slogin.html;jsessionid=6252CF2A6FB70A9D25A9B5ADD0A7C116")
        b.fill("yhm", self.txtUserName)
        b.fill("mm", self.TextBox2)
        button = b.find_by_id('dl')
        button.click()
        cookie = 'JSESSIONID' + '=' + b.cookies['JSESSIONID']
        return cookie


# login = Login()
# login.submit()


