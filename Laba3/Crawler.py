import requests
from bs4 import BeautifulSoup
import urlparse

class Crawler(object):

    def __init__(self, count, cur_url):
        self.count_thread = count
        self.url = cur_url


    def absolut_url(self, u):
        temp = urlparse.urljoin(self.url, u)
        if '#' in temp:
            temp = temp[:temp.index('#')]
        return temp

    def download(self):
        page = requests.get(self.url) #downland page of site 
        if  page.status_code != 200:
            raise Exception(page.status_code)
        return page.text
    
    def findURLs(self):
        soup = BeautifulSoup(self.download(), 'html.parser') #beautiful  HTML
        listOfUrls = []
        for url in soup.find_all('a'):
            listOfUrls.append(self.absolut_url(url.get('href')))
        return listOfUrls
        


def main():
    a = Crawler(3, 'http://stackoverflow.com/questions/4019971/how-to-implement-iter-self-for-a-container-object-python')
    k = a.findURLs()
    for i in k:
        print i

if __name__ == "__main__":
    main()
