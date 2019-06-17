from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class FirstNetworkPage(BaseAction):
    # 2g
    network_2g_button = By.XPATH, "//*[@text='2G']"

    # 3g
    network_3g_button = By.XPATH, "//*[@text='3G']"

    # 点击 2g
    def click_2g(self):
        self.click(self.network_2g_button)

    # 点击 3g
    def click_3g(self):
        self.click(self.network_3g_button)

