import asyncio
import aiohttp

"""
import os
from urllib import request
from urllib.parse import urljoin
"""

import re
from bs4 import BeautifulSoup, SoupStrainer
from browserHandler import Browser
from osHandler import OsHandler

from console import console

# myUrl = "https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D0%BD%D0%B1%D0%BB%D0%B0%D0%BD"


browser = Browser()
os_handler = OsHandler()


class Parser:
    def __init__(self):

        self.images = []
        self.url = "https://ru.wikipedia.org"
        self.mainPage = "https://ru.wikipedia.org"
        self.randomPage = "/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
        # self.randomPage = "/wiki/Special:Random"
        self.mainLink = ""

    def getRandomPage(self):
        return self.url + self.randomPage

    def isConvenientImgTag(self, tag):
        return (
            tag.has_attr("width") and int(tag.get("width")) > 200
            if tag.has_attr("width")
            and not tag.get("width").endswith("%")
            else False
        )

    def imgReducer(self, image):
        srcet = image.get("srcset")

        if bool(srcet) is not False:
            urls = list(
                filter(
                    lambda item: item.endswith("2x"),
                    srcet.split(",")
                    if "," in srcet
                    else srcet.split("\\\\"),
                )
            )
            return urls[0][3:-3].strip() if len(urls) > 0 else []

        return image.get("src")[2::].strip()

    def getMainHref(self, soup, sets={"rel": "canonical"}):
        self.mainLink = soup.find("link", sets)["href"]
        return self.mainLink

    def getCSSHref(self, soup, sets={"rel": "stylesheet"}):
        self.cssLink = soup.find("link", sets)["href"]
        return self.cssLink

    def setHeader(self, arr):
        cssLinks = [
            item for item in arr if item["rel"][0] == "stylesheet"
        ]

        for x in range(len(arr)):
            if x < len(cssLinks):

                arr[x].replace_with(cssLinks[x])
            else:
                arr[x].decompose()
        console.log(arr)
        """
        cssLinks = [
            item["href"]
            for item in arr
            if not item.find("stylesheet")
        ]

        console.log("cssLinks: ", cssLinks)
        """
        """
        cssLinks = [
            item for item in arr if not item.find("stylesheet")
        ]
        """

        # return cssLinks

    def changeCSSLink(self, soup):
        html = soup.prettify()

        cssLinks = self.setHeader(soup.findAll("link"))
        """
        head = soup.find("head").contents[:3]
        head.append(
            f"<link rel='stylesheet' href='{self.styleFile}'>"
        )
        console.log("head: ", head)
        """
        html = re.sub(
            r"<link[^>]+>",
            f"<link rel='stylesheet' href='{self.styleFile}'>",
            html,
        )

        """
        html = re.sub(
            r"<link[^>]+>",
            f"<link rel='stylesheet' href='{self.styleFile}'>",
            html,
        )
        """

        return html

    async def getData(self, url):

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                content = await resp.text()

                soup = BeautifulSoup(content, "html.parser")

                browser.openTab(self.getMainHref(soup))

                rowArticle = str(soup.find("h1").contents[0])
                article = (
                    rowArticle
                    if rowArticle.count("<") == 0
                    else rowArticle[3:-4]
                )
                os_handler.changeDir(dirName=article)

                rowCss = str(
                    os_handler.urlOpen(
                        url=self.getCSSHref(soup),
                        domainName=self.mainPage,
                    ).read()
                )[2:-1]
                css = rowCss

                cssAttrTuple = os_handler.writeToFile(
                    css,
                    "css",
                    "style",
                )
                self.__setattr__(*cssAttrTuple)

                rowHtml = self.changeCSSLink(soup)

                htmlAttrTuple = os_handler.writeToFile(
                    rowHtml, "html"
                )

                self.__setattr__(*htmlAttrTuple)

                imgSrc = [
                    self.imgReducer(image=x)
                    for x in soup.find_all(self.isConvenientImgTag)
                ]

                if len(imgSrc) > 0:
                    for i in imgSrc:
                        self.images.append(
                            os_handler.saveImgByUrl(url=i)
                        )
            await session.close()
        return

    def looping(self, url):
        # url = "https://ru.wikipedia.org/wiki/%D0%A2%D0%B8%D1%85%D0%B0%D1%8F_(%D0%BF%D0%BE%D1%81%D1%91%D0%BB%D0%BE%D0%BA_%D0%B6%D0%B5%D0%BB%D0%B5%D0%B7%D0%BD%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B6%D0%BD%D0%BE%D0%B9_%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D0%B8,_%D0%9F%D0%B5%D1%80%D0%BC%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D1%80%D0%B0%D0%B9)"
        # url = "https://ru.wikipedia.org/wiki/%D0%9C%D1%8E%D0%BD%D1%81%D1%82%D0%B5%D1%80-%D0%97%D0%B0%D1%80%D0%BC%D1%81%D1%85%D0%B0%D0%B9%D0%BC"
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.getData(url))
