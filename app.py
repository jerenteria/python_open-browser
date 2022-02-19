import webbrowser
import requests
from bs4 import BeautifulSoup


## url to open
url = 'http://google.com/'

## opens chrome
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
webbrowser.get(chrome_path).open(url)

result = requests.get(url)
## html.parser gets the actual html info from the page
doc = BeautifulSoup(result.text, "html.parser")

