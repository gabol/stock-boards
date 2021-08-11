import requests

def getPage(url):
		r = requests.get(url)
		r.text
		return r.text

def makeNewFile(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()

makeNewFile("earthwing.html", getPage("https://www.earthwingboards.com/product-page/belly-racer-2020"))
makeNewFile("neuvision.html", getPage("https://neuvisionskateco.com/collections/boards/products/neuvision-skate-co-v1"))