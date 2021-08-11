import requests
import time
from pushover import Client

# MuirSkate links (testingitem always in stock)
harryclarke = "https://www.muirskate.com/longboard/decks/73393/madrid-2019-pro-series-snitch-harry-clarke-longboard-skateboard-deck-w-grip"

# other links
neuvision = "https://neuvisionskateco.com/collections/boards/products/neuvision-skate-co-v1"
earthwing = "https://www.earthwingboards.com/product-page/belly-racer-2020"
justinrouleau = "https://www.fullcircledistribution.com/collections/madrid-skateboards/products/madrid-pro-series-trapstar-36-justin-rouleau"

# define client
userToken = None
apiToken = None
client = Client(userToken, api_token=apiToken)

# requests html
def getPage(url):
		r = requests.get(url)
		r.text
		return r.text

# send message via pushover
def sendMessage(message, title, sound, url, urlTitle):
		client.send_message(message, title=title, sound=sound, url=url, url_title=urlTitle)

# html reader (for when you don't know what a page looks like when in stock)
def HTMLread(file):
	htmlRead = open(file, "r")
	return htmlRead.read()

# the actual checker
while True:
	if HTMLread("html/neuvision.html") != str(getPage(neuvision)): # checks downloaded html against updated html
		sendMessage("Neuvision Skate Co. V1 is IN STOCK at Neuvision Skate Co.", "NEUVISION DECK IN STOCK, BUY NOW!", "cashregister", neuvision, "click to buy")
		print("OH DAMN")
	else:
		print("nah")
	time.sleep(5)
	if HTMLread("html/earthwing.html") != str(getPage(earthwing)): # checks downloaded html against updated html
		sendMessage("Belly Racer is IN STOCK at Earthwing", "BELLY RACER DECK IN STOCK, BUY NOW!", "cashregister", earthwing, "click to buy")
		print("OH DAMN")
	else:
		print("nah")
	time.sleep(5)
	if str(getPage(harryclarke)).count("outofstock") < 3: # checks for the amount of "outofstock"s in the html
		sendMessage("Madrid Pro Series Harry Clarke is IN STOCK at MuirSkate", "HARRY CLARKE DECK IN STOCK, BUY NOW!", "cashregister", harryclarke, "click to buy")
		print("OH DAMN")
	else:
		print("nah")
	time.sleep(5)
	if "http://schema.org/OutOfStock" in str(getPage(justinrouleau)): # checks for "OutOfStock" schema in website
		print("nah")
	else:
		sendMessage("Madrid Pro Series Justin Rouleau is IN STOCK at Full Circle Distribution", "JUSTIN ROULEAU DECK IN STOCK, BUY NOW!", "cashregister", justinrouleau, "click to buy")
		print("OH DAMN")
	time.sleep(5)
