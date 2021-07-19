import os
from urllib import request
from urllib.parse import urljoin, unquote
from unidecode import unidecode
import re


class OsHandler:
    def changeDir(
        self,
        dirName,
    ):
        defaultDir = os.path.join(
            os.environ["USERPROFILE"], "Desktop", "WikiMages"
        )

        if not os.path.exists(defaultDir):
            os.mkdir(defaultDir)

        os.chdir(defaultDir)

        currentDir = os.getcwd()

        childDirName = re.sub(r"<[^>]*>", "/", dirName)

        if os.listdir(currentDir).count(childDirName) > 0:
            os.chdir(os.path.join(currentDir, childDirName))
        else:
            os.mkdir(os.path.join(os.getcwd(), childDirName))
            os.chdir(os.path.join(currentDir, childDirName))

        return

    def urlOpen(self, url, domainName="http://"):
        link = f"{domainName}{url}"
        try:
            res = request.urlopen(link)
            code = res.getcode()
            return res if code == 200 else None
        except Exception as error:
            print("error: ", error)
            print("error url", url)

    def saveImgByUrl(self, url, imgName):
        if type(url) is not str:
            return

        if self.urlOpen(url) == None:
            return None

        try:
            img = self.urlOpen(url).read()
            out = open(imgName, "wb")
            out.write(img)
            out.close()
            return url
        except Exception as error:
            print("error: ", error)
            print("error url", url)

    def writeToFile(self, str, extension="txt", name="html"):
        fileName = f"{name}.{extension}"
        fileKey = f"{name}File"

        with open(fileName, "w", encoding="utf-8") as out:
            print(str, file=out)
            out.close()

        return (fileKey, fileName)
