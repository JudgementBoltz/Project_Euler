from bs4 import BeautifulSoup
import requests
import re
#been getting bored with the copy paste data dumps
#so thought i'd play around with some webscraping on this problem
html = requests.get("https://projecteuler.net/problem=13").text
soup = BeautifulSoup(html, 'html5lib')

#pulls the data from the div tag, I specified by style just because everything was in that div
numbers = [div for div in soup('div') if div.get('style') == "font-family:'courier new';font-size:10pt;text-align:center;"]
#turned the bs4 object to a string so I could manipulate and parse 
numbers = str(numbers[0])
#made the string a list split at each break tag
numbers = numbers.split('<br/>')
#the last element of the list was a close div tag so just deleted it here
del numbers[-1]
#regex magicks to parse out the opening div tag in the first list element
numbers[0] = re.sub('<[^>]+>','',numbers[0])

#there was a bunch of leftover "\n" so got rid of them here and made all elements long integer types
for n in range(len(numbers)):
    numbers[n] = long(numbers[n][1:])

#made the answer a string so I could print just the first 10 digits
number = str(sum(numbers))
print number[:10]