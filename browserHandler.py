import webbrowser

CHROME_PATH = "C:/Users/Kirill/AppData/Local/Google/Chrome/Application/chrome.exe"


class Browser:
    def __init__(self, browserPath=CHROME_PATH, browserName="chrome"):
        self.browserPath = browserPath
        self.browserName = browserName
        self.initNewDefaultBrowser()

    def initNewDefaultBrowser(self):
        webbrowser.register(
            self.browserName,
            None,
            webbrowser.BackgroundBrowser(self.browserPath),
        )
        return

    def openTab(self, url):
        webbrowser.get(self.browserName).open_new_tab(url)
        return

