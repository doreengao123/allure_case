from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MorePage(BaseAction):
    # 移动网络
    mobile_network_button = By.XPATH, "//*[@text='移动网络']"

    # 点击 移动网络
    def click_mobile_network(self):
        self.click(self.mobile_network_button)
