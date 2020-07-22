import re
from urllib.request import urlopen

site = urlopen("https://egoistokur.com/")

html = str(site.read())

print(len(re.findall("roman",html)))