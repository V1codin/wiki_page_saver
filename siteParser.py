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
        self.cssNumber = 0

        self.hide = None
        self.show = None

    def getRandomPage(self):
        return self.url + self.randomPage

    def isConvenientImgTag(self, tag):
        # deprecated
        return (
            tag.has_attr("width") and int(tag.get("width")) > 200
            if tag.has_attr("width")
            and not tag.get("width").endswith("%")
            else False
        )

    def imgReducer(self, image):
        # deprecated
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
        # deprecated
        self.cssLink = soup.find("link", sets)["href"]
        return self.cssLink

    def setHeader(self, soup, rowHead):

        for item in rowHead:
            href = item["href"]

            css = str(
                os_handler.urlOpen(
                    url=href, domainName=self.mainPage
                ).read()
            )[2:-1]

            self.cssNumber += 1

            fileKey, fileName = os_handler.writeToFile(
                css,
                "css",
                f"style{self.cssNumber}",
            )
            item["href"] = fileName

        head = soup.new_tag("head")
        head.extend(rowHead)

        return head

    def setImages(self, soup):
        # https://ru.wikipedia.org/wiki/%D0%92%D0%B0%D0%BB%D1%8C%D0%B4%D0%B5%D0%BD%D0%B3%D0%BE
        for image in soup.find_all("img"):

            src = image.get("src")
            link = re.sub(r"^(\/{1,2})", "", src)

            if link.find("static") != -1:
                continue

            """
            srcet = image.get("srcset")
            if not srcet:
                continue
            rowLink = srcet.split(", ")[-1].split()[0]
            link = re.sub(r"^(\/{1,2})", "", rowLink)

            if link.find("static") != -1:
                continue
            """
            extension = link.split(".")[-1]
            if len(extension) > 4:
                continue

            imageName = f"image{len(self.images)}.{extension}"

            url = os_handler.saveImgByUrl(link, imageName)
            if url != None:
                self.images.append(url)
                image["src"] = imageName
                image["srcset"] = [imageName]

    def htmlConstructor(self, soup):
        head = self.setHeader(
            soup, soup.find_all("link", rel="stylesheet")
        )
        soup.head.replace_with(head)

        self.setImages(soup)

        return soup

    def changeCSSLink(self, soup):
        # deprecated
        html = soup.prettify()

        html = re.sub(
            r"<link[^>]+>",
            f"<link rel='stylesheet' href='{self.styleFile}'>",
            html,
        )

        return html

    async def getData(self, url):

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                content = await resp.text()

                self.hide()

                soup = BeautifulSoup(content, "html.parser")
                self.mainLink = self.getMainHref(soup)

                rowArticle = str(soup.find("h1").contents[0])

                article = (
                    rowArticle
                    if rowArticle.count("<") == 0
                    else rowArticle[3:-4]
                )
                os_handler.changeDir(dirName=article)

                """
                old working for one css style!!

                css = str(
                    os_handler.urlOpen(
                        url=self.getCSSHref(soup),
                        domainName=self.mainPage,
                    ).read()
                )[2:-1]

                cssAttrTuple = os_handler.writeToFile(
                    css,
                    "css",
                    "style",
                )

                self.__setattr__(*cssAttrTuple)
                
                rowHtml = self.changeCSSLink(soup)
                """
                rowHtml = self.htmlConstructor(soup)

                htmlAttrTuple = os_handler.writeToFile(
                    rowHtml, "html"
                )

                self.__setattr__(*htmlAttrTuple)
                """
                old image saver
                imgSrc = [
                    self.imgReducer(image=x)
                    for x in soup.find_all(self.isConvenientImgTag)
                ]

                if len(imgSrc) > 0:
                    for i in imgSrc:
                        url, imgName = os_handler.saveImgByUrl(url=i)
                        self.images.append(
                            url
                        )
                """

            browser.openTab(self.mainLink)
            self.show()

            await session.close()

        return

    def looping(self, url, actions: tuple):
        hide, show = actions
        self.hide = hide
        self.show = show
        # url = "https://ru.wikipedia.org/wiki/%D0%A2%D0%B8%D1%85%D0%B0%D1%8F_(%D0%BF%D0%BE%D1%81%D1%91%D0%BB%D0%BE%D0%BA_%D0%B6%D0%B5%D0%BB%D0%B5%D0%B7%D0%BD%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B6%D0%BD%D0%BE%D0%B9_%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D0%B8,_%D0%9F%D0%B5%D1%80%D0%BC%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D1%80%D0%B0%D0%B9)"
        # url = "https://ru.wikipedia.org/wiki/%D0%9C%D1%8E%D0%BD%D1%81%D1%82%D0%B5%D1%80-%D0%97%D0%B0%D1%80%D0%BC%D1%81%D1%85%D0%B0%D0%B9%D0%BC"
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.getData(url))
