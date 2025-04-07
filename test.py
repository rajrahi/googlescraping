from bs4 import BeautifulSoup
import requests




url = "https://www.google.com/search?q=empmonitor&sca_esv=38528723608d6ebc&source=hp&ei=oXTzZ4nsFO2Pvr0P7ZPH4Qs&iflsig=ACkRmUkAAAAAZ_OCsQ-bka3XEekselx343-H-HnDkYK9&ved=0ahUKEwjJwIuzqcWMAxXth68BHe3JMbwQ4dUDCBA&uact=5&oq=empmonitor&gs_lp=Egdnd3Mtd2l6IgplbXBtb25pdG9yMgsQLhiABBjHARivATIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAY7wVI0y5QAFiUJXAAeACQAQCYAVygAbUGqgECMTC4AQPIAQD4AQGYAgqgAukGwgIIEAAYgAQYsQPCAgsQABiABBixAxiDAcICCxAuGIAEGLEDGIMBwgIOEC4YgAQYsQMYgwEYigXCAg4QABiABBixAxiDARiKBcICCBAuGIAEGLEDwgIFEC4YgATCAg4QLhiABBixAxjRAxjHAcICBBAAGAPCAgcQABiABBgKwgIIEAAYgAQYogSYAwCSBwIxMKAHwlKyBwIxMLgH6QY&sclient=gws-wiz&sei=qnTzZ86JC765seMP8enggAU"



def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.prettify()


print(get_page(url))
