"""
    统一入口类：
        避免在业务层里面导入多个类
"""

from page.page_login import PageLogin
from page.page_order import PageOrder


class PageIn:
    def page_get_pagelogin(self):
        # 将页面对象实例化然后返回
        return PageLogin()

    def page_get_pageorder(self):
        return PageOrder()
