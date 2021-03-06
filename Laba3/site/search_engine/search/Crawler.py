# -*- coding: utf-8 -i*-

import sys
import requests
import urlparse
import os.path
import base64
import time

from threading import Thread
import threading
from Queue import Queue
from bs4 import BeautifulSoup

class Crawler(object):

    def __init__(self, depth, count, cur_url, storage_dir):
        self.url = cur_url[0]
        self.q = Queue()
        self.depth = depth
        self.listOfThreads = []
        self.q.put((self.url, 0))
        print cur_url
        for i in xrange(1, len(cur_url)):
            self.q.put((cur_url[i], 0))
        self.path = storage_dir
        self._stop = threading.Event()

        for i in xrange(count):
            t = Thread(self.todo())
            t.signal = True
            t.daemon = True
            self.listOfThreads.append(t)

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def write_into_file(self, u, txt):
        file_name = os.path.join(self.path, base64.b16encode(u))
        f = open(file_name, "w")
        print file_name
        soup = BeautifulSoup(txt, 'html.parser')
        data = soup.get_text()
        for i in data:
            try:
                f.write(i.encode("utf-8")) 
            except Exception:
                print i
                print "_------------------------------"
        f.close()
        sys.stdout.flush()
        return

    def todo(self):
        while True:
            try:
                if self.stopped():
                    break
                self.do()
            except Exception, e:
                print e

    def downloadPages(self):
        for i in self.listOfThreads:
            i.start()

        while not self.stopped():
            time.sleep(0.1)
            
    def absolut_url(self, u):
        temp = urlparse.urljoin(self.url, u)
        if '#' in temp:
            temp = temp[:temp.index('#')]
        return temp

    def download(self, u):
        page = requests.get(u) #downland page of site 
        if  page.status_code != 200:
            raise Exception(page.status_code)
        return page.text
    
    def findURLs(self, u):
        page = self.download(u)
        self.write_into_file(u, page)
        soup = BeautifulSoup(page, 'html.parser') #beautiful  HTML
        listOfUrls = []
        for url in soup.find_all('a'):
            listOfUrls.append(self.absolut_url(url.get('href')))
        return listOfUrls
            
    def do(self):
        if self.q.empty():
            self.stop()

        temp = self.q.get()
        link = temp[0]
        depth = temp[1]
        print link
        print depth
        if depth > self.depth:
            self.stop()
            return
        listOfURLs = self.findURLs(link)
        for i in listOfURLs:
            self.q.put((i, depth + 1))
        

def main():
    a = Crawler(10, 5, ['http://www.bbc.com/news'], '/home/katrin/databasetemp/')
    k = a.downloadPages()

if __name__ == "__main__":
    main()
