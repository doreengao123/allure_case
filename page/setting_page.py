from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):
    # 更多
    more_button = By.XPATH, "//*[@text='更多']"

    # 显示
    display_button = By.XPATH, "//*[@text='显示']"

    # 点击 更多
    def click_more(self):
        self.click(self.more_button)

    # 点击 显示
    def click_display(self):
        self.click(self.display_button)
