from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MobileNetworkPage(BaseAction):

    # 首选网络类型
    first_network_button = By.XPATH, "//*[@text='首选网络类型']"

    # 点击 首选网络类型
    def click_first_network(self):
        self.click(self.first_network_button)