from selenium import webdriver


class WebdriverFactory:
    @staticmethod
    def getWebdriver(browserName):
        if browserName == "firefox":
            return webdriver.Firefox()
        elif browserName == "chrome":
            return webdriver.Chrome()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()