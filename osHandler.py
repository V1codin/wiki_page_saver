import os
from urllib import request
from urllib.parse import urljoin
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
        res = request.urlopen(link)
        code = res.getcode()
        return res if code == 200 else None

    def saveImgByUrl(self, url):
        if type(url) is not str:
            return

        res = re.search(r"\/[^\/]+$", url, flags=re.MULTILINE)

        if res:
            startIndex = res.start()

            imgName = url[startIndex + 1 : :]

            assert self.urlOpen(url) != None
            img = self.urlOpen(url).read()
            out = open(imgName, "wb")
            out.write(img)
            out.close()

        return url

    def writeToFile(self, str, extension="txt", name="html"):
        fileName = f"{name}.{extension}"
        fileKey = f"{name}File"

        with open(fileName, "w", encoding="utf-8") as out:
            print(str, file=out)
            out.close()

        return (fileKey, fileName)