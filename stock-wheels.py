import requests
import time
from pushover import Client

# PP and S1 links (testingitem always in stock)
testingitem = "hhttps://powell-peralta.com/powell-peralta-ripper-skateboard-deck-natural-turquoise-shape-242-8-x-31-45"
purplePP = "https://powell-peralta.com/powell-peralta-kevin-reimer-skateboard-wheels-72mm-75a-4pk-purple"
greenPP = "https://powell-peralta.com/powell-peralta-kevin-reimer-skateboard-wheels-72mm-75a-4pk-green"
purpleS1 = "https://www.skateone.com/powell-peralta-kevin-reimer-skateboard-wheels-72mm-75a-4pk-purple"
greenS1 = "https://www.skateone.com/powell-peralta-kevin-reimer-skateboard-wheels-72mm-75a-4pk-green"

# Other links
purpleMuir = "https://www.muirskate.com/longboard/wheels/72819/72mm-powell-peralta-soft-slide-kevin-reimer-longboard-skateboard-wheels"

# define client
userToken = None
apiToken = None
client = Client(userToken, api_token=apiToken)

# requests html
def getPage(url):
		r = requests.get(url)
		r.text
		return r.text

# sends message via pushover
def sendMessage(message, title, sound, url, urlTitle):
		client.send_message(message, title=title, sound=sound, url=url, url_title=urlTitle)

# the actual checker
while True:
	if 'in-stock' in str(getPage(purplePP)): # checks for the substring "in-stock" in the html
		sendMessage("Purple Krimes in STOCK at Powell Peralta", "PURPLE KRIMES IN STOCK, BUY NOW!", "cashregister", purplePP, "click to buy")
		print("OH DAMN")
	else:
		print("nah")
		time.sleep(5)
	if 'in-stock' in str(getPage(greenPP)): # checks for the substring "in-stock" in the html
		sendMessage("Green Krimes in STOCK at Powell Peralta", "GREEN KRIMES IN STOCK, BUY NOW!", "cashregister", greenPP, "click to buy")
		print("OH DAMN")
	else:
		print("nah")
		time.sleep(5)
	if 'in-stock' in str(getPage(purpleS1)): # checks for the substring "in-stock" in the html
		sendMessage("Purple Krimes in STOCK at Skate One", "PURPLE KRIMES IN STOCK, BUY NOW!", "cashregister", purpleS1, "click to buy")
		print("OH DAMN")
	else:
		print("nah")
	if 'in-stock' in str(getPage(greenS1)): # checks for the substring "in-stock" in the html
		sendMessage("Green Krimes in STOCK at Skate One", "GREEN KRIMES IN STOCK, BUY NOW!", "cashregister", greenS1, "click to buy")
		print("OH DAMN")
	else:
		print("nah")
	time.sleep(5)
	if 'outofstock' in str(getPage(purpleMuir)): # checks for the substring "outofstock" in the html
		print("nah")
	else:
		sendMessage("Purple Krimes in STOCK at MuirSkate", "PURPLE KRIMES IN STOCK, BUY NOW!", "cashregister", purpleMuir, "click to buy")
		print("OH DAMN")
