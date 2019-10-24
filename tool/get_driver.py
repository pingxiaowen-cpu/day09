"""
    采用类方法的原因：
        保证多个页面获取的是同一个驱动对象driver
"""
from appium import webdriver
import page


class GetDriver:
    driver = None
    package = page.app_appPackage
    activity = page.app_appActivity

    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 定义空字典
            desired_caps = {}
            # 指定平台名称 必须写对
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            # 不能为空，可以随便写
            desired_caps['deviceName'] = 'emulator-5554'
            # # 包名/---下面的方法需要传参
            # desired_caps['appPackage'] = package
            # # 启动名
            # desired_caps['appActivity'] = activity
            # 包名/---下面的可以不用传参
            desired_caps['appPackage'] = GetDriver.package
            # 启动名
            desired_caps['appActivity'] = GetDriver.activity
            # 声明手机驱动对象
            cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls.driver

    # 关闭driver
    @classmethod
    def close_driver(cls):
        if cls.driver:  # ---判断不为空，则关闭
            cls.driver.quit()
            # 必须置空，----大坑！！！！！！！！！！！！！！！！！！！！
            cls.driver = None  # 将内存地址置空


if __name__ == '__main__':
    # 确实关了，但是内存地址没有注销
    print(GetDriver.get_driver())
    GetDriver.close_driver()
    print(GetDriver.get_driver())
