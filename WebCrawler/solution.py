"""
The code will be class based consisting of function to trigger operation
"""

import requests
from bs4 import BeautifulSoup
import sys

class Scrape:
    KW = ""
    PG = 0

    def __init__(self,kw="",pg=0):
        self.KW = kw
        self.PG = pg

    def numOfRes():
        pg_counter = 1
        output = 0

        while True:
            response = requests.get("http://www.shopping.com/products~PG-%d?KW=%s"%(pg_counter, self.KW))

            if (response.status_code != 200):
                break

            soup = BeautifulSoup(response.text)

            items = soup.findAll('div','gridItemTop')

            totalItems = len(items)

            if (not totalItems):
                break

            output = output + totalItems

            pg_counter = pg_counter + 1

        return output

    def listItems():

        response = requests.get("http://www.shopping.com/products~PG-%d?KW=%s"%(page, kw))

        if (response.status_code != 200):
            raise SystemExit("Invalid Keyword")

        soup = BeautifulSoup(res.text)

        items = soup.findAll('div','gridItemTop')

        output = [i.img['title'] for i in items]

        return output


def main():
    args = len(sys.argv)
    if(args==1):
        raise SystemExit("Kindly specify arguments")
    elif(args==2):
        scrape = Scrape(kw=sys.argv[1])
        print scrape.numOfRes()
    else:
        scrape = Scrape(kw='+'.join(sys.argv[2:]),pg=int(sys.argv[1]))
        for item in scrape.listItems():
            print item

if __name__ == '__main__':
    main()

