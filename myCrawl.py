import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

seedPage = 'http://www.inkredo.in'

#response = requests.get(seedPage)
#pageContent = str(BeautifulSoup(response.content, 'html.parser'))


visited = dict()
maxDepth = 2
targetPage = 'http://www.inkredo.in/careers.html'

def visitPage(url, depth):
	
	#terminating condition
	if depth>maxDepth:
		return
	
	# to prevent visiting same link again
	if url in visited:
		return
	
	print(url)
	visited[url] = True
	
	if url == targetPage:
		print('deapth of target page is :',depth)
		return
	
	#for every link found in current page call the same function
	try:
		html_page = urlopen(url)
		soup = BeautifulSoup(html_page, 'html.parser')
		
		
		for link in soup.findAll('a'):
			nextLink = link.get('href')
			
			#concatenate sublinks
			if nextLink[0] == '/':
				visitPage(seedPage+nextLink, depth+1)

			else:
				visitPage(nextLink, depth+1)
	except:
		print('exception '+url)


visitPage(seedPage, 0)

