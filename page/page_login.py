from base.base import Base
from page import login_close_alert, login_me, login_username_exists, login_username, login_pwd, login_btn


class PageLogin(Base):
    # 关闭 弹窗
    def page_close_alert(self):
        self.base_click(login_close_alert)

    # 点击 我
    def page_click_me(self):
        self.base_click(login_me)

    # 点击 已有账号，去登录
    def page_click_username_exists(self):
        self.base_click(login_username_exists)

    # 输入 用户名
    def page_input_username(self,username):
       self.base_input(login_username,username)

    # 输入 密码
    def page_input_password(self,password):
        self.base_input(login_pwd,password)

    # 点击 登录按钮
    def page_click_login_btn(self):
        self.base_click(login_btn)

    # 组合业务方法----在测试用例中直接调用这个方法
    def page_login(self,username,password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
