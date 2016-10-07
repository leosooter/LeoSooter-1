
from urllib2 import urlopen
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# choose the url to crawl
url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler
soup = BeautifulSoup(urlopen(url), "html.parser")
#print soup

#####  Part 1
print "\nPart1\n"
# Create list shell
link_list = []
#Loop through all links assumes links are inside "a" tag
#To find all "hrefs" on page use- "for link in soup.findAll(True, href=True):"
for link in soup.findAll(True, href=True):
    href = link.get('href')
    link_list.append(link.name)
print link_list
print len(link_list)


##### Part 2
print "\nPart2\n"
listDict = {}

for link in soup('a'):
    href = str(link.get('href'))
    if href in listDict:
        #print href, "is repeat"
        listDict[href] += 1
    else:
        listDict[href] = 1
print listDict
