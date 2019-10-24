import sys
import os



sys.path.append(os.getcwd())

import pytest

from page.page_login import PageLogin


def data():
    return [("itheimama","123456"),("itheimama","1234567"),("itheima","123456")]


class TestLogin:
    # 初始化
    def setup_class(self):
        # 获取PageLogin对象
        self.login = PageLogin()
        # 点击弹窗
        self.login.page_close_alert()
        # 点击我
        self.login.page_click_me()

        # 点击已有账号 去登录
        self.login.page_click_username_exists()

    # 结束
    def teardown_class(self):
        # 关闭driver驱动对象
        self.login.driver.quit()

    # 测试方法
    # @pytest.mark.parametrize("username,password", [("heima", 123456), ("itheima", 1234567), ("itheima", 123456)])
    @pytest.mark.parametrize("username,password", data())
    def test_login(self, username, password):
        self.login.page_login(username, password)
