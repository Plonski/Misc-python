__author__ = 'Thomas'

topM = open("Top Million.txt", "r")
write = open("output.txt", "w")
websiteList = []

for line in topM:

    if ("Hidden profile" in line):
        pass
    else:
        so = ''.join(c for c in line if not c.isdigit())

        websiteList.append(so[1:])

for x in websiteList:
    write.write(x)

print(websiteList)
'''
for x in santizedlist:
    try:
        write.writeline(x)
    except:
        print("done")
#print(websiteList)
'''