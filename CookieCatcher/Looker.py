from urllib import request
from http import cookiejar
from http.cookiejar import CookieJar
topM = open("Top Million.txt", "r")
write = open("output.txt", "w")
websiteList = []

#Gets the website list
for line in topM:

    if ("Hidden profile" in line):
        pass
    else:
        so = ''.join(c for c in line if not c.isdigit())

        websiteList.append(so[1:])

for x in websiteList:
    write.write(x)

print(websiteList)

#Cookie lookup will be initialized at each new website
cj = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj), request.HTTPHandler())
response = opener.open("http://google.com/")
print(cj)
for cookie in cj:
    print (cookie.name)

#Class that will get the info about each website into one node
class collection:

    def __init__(self, website):
        self.website = website


    def getWebsite(self):
        print(self.website)
        return self.website

    def setWebsite(self, website):
        self.website = website

    def getCookies(self):
        print()

#Hashtable that will hold all website nodes
class HashTable:
    def __init__(self):
        self.size = 250000
