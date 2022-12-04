# import module
import requests
from bs4 import BeautifulSoup
from flask import Flask, request

HEADERS = ({'User-Agent':
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
			AppleWebKit/537.36 (KHTML, like Gecko) \
			Chrome/90.0.4430.212 Safari/537.36',
			'Accept-Language': 'en-US, en;q=0.5'})
# user define function
# Scrape the data
def getdata(url):
	r = requests.get(url, headers=HEADERS)
	return r.text


def html_code(url):

	# pass the url
	# into getdata function
	htmldata = getdata(url)
	soup = BeautifulSoup(htmldata, 'html.parser')

	# display html code
	return (soup)


def get_reviews_url(soup):
	return 'https://www.amazon.in' + soup.find(class_='a-link-emphasis a-text-bold').get('href')


app = Flask(__name__)
@app.route('/', methods = ['POST'])

def get_reviews():
	url = request.get_json()['url']

	# soup = html_code(url)
	# url = get_reviews_url(soup)
	# soup = html_code(url)
	try:
		soup = html_code(url)
		url = get_reviews_url(soup)
		soup = html_code(url)
	except:
		return {'test': [], 'flag': 1}

	data = []
	count = 10  			#10 page limit to avoid long loading times while collecting data
	while True:
		reviews = soup.find_all('div', {'data-hook': 'review'})

		# For every item in review, scrape the following and store as a list called review
		for item in reviews:
			if item.find('span', {'class': 'a-size-mini a-color-state a-text-bold'}):
				data.append(item.find('span', {'data-hook': 'review-body'}).text.strip())

		if soup.find(class_='a-last') != None and soup.find(class_='a-last').find('a') != None and count > 0:  #verified customer
			url = 'https://www.amazon.in' + soup.find(class_='a-last').find('a').get('href')
			soup = html_code(url)
		else:
			flag = 0
			if data == []:
				flag = 1
			return {'test': data, 'flag': flag}

		count -= 1



if __name__ == '__main__':
    app.run(port = 5000)

