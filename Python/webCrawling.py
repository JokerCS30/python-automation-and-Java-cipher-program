import requests, bs4, webbrowser, re, time, sys, getopt

mins = 10



def main():
    deals = False
    stuff = False
    theHacker = False
    technology = False
    twit = False

    try:
        opts, args = getopt.getopt(sys.argv[1:],"ds:tj")

    except getopt.GetoptError as e:
        print (str(e))
        print ('should be python file.py (-d, -s minutes to loop for)')

    for opt, arg in opts:
        if opt == '-d':
            deals = True
        elif opt == '-s':
            stuff = True
            mins = arg
        elif opt == '-t':
            technology = True
        elif opt == '-j':
            twit = True

        else:
            print 'something didnt work'

    if deals == True:
        mightyApe()
    if stuff == True:
        loop(float(mins))
    if theHacker == True:
        hackerNews()
    if twit == True:
        twitter()



def stuffNZ():
    res2 = requests.get('http://www.stuff.co.nz')
    res2.raise_for_status()
    stuff = bs4.BeautifulSoup(res2.text, "html.parser")
    articles = ''
    words = ['hacker', 'hacking', 'shark', 'Shark', 'technology', 'Technology']
    reading = ''
    urls = []

    elems2 = stuff.select('#content a')

    for i in range(len(elems2)):

        articles += elems2[i].getText()
        for word in words:
            if word in elems2[i].getText():
                try:
                    url = ('http://www.stuff.co.nz/' + elems2[i].get('href'))
                    urls.append(url)
                    res3 = requests.get(url)
                    res3.raise_for_status()
                except:
                    url = (elems2[i].get('href'))
                    urls.append(url)
                    res3 = requests.get(url)
                    res3.raise_for_status()

                temp = bs4.BeautifulSoup(res3.text, "html.parser")
                elems3 = temp.select('article p')
                for x in range(len(elems3)):
                    print (elems3[x].getText()).lstrip()
                    time.sleep(0.5)

    res = requests.get('http://www.stuff.co.nz/technology')
    res.raise_for_status()
    stuf = bs4.BeautifulSoup(res.text, "html.parser")
    elems = stuf.select('#content a')

    for z in range(len(elems)):
        nex = False
        try:
            url2 = ('http://www.stuff.co.nz/' + elems[z].get('href'))

            for link in urls:
                if link == url2:
                    nex = True
            if nex == True:
                continue
            urls.append(url2)
            webbrowser.open(url2)
            res4 = requests.get(url2)
            res4.raise_for_status()
        except:
            url2 = (elems[z].get('href'))

            for link in urls:
                if link == url2:
                    nex = True
            if nex == True:
                continue
            urls.append(url2)
            webbrowser.open(url2)
            res4 = requests.get(url2)
            res4.raise_for_status()

        tmp = bs4.BeautifulSoup(res4.text, "html.parser")
        elems4 = tmp.select('article p')
        for f in range(len(elems4)):
            print (elems4[f].getText()).lstrip()
            time.sleep(0.5)

    for x in words:
        if x in articles:
            print 'theres a ' + x + ' article'




def loop(minutes):
    while minutes > 0:
        stuffNZ()
        print
        hackerNews()
        time.sleep(60)
        minutes -= 1


def mightyApe():
    res = requests.get('https://www.mightyape.co.nz/daily-deals')
    res.raise_for_status()
    dailyDeals = bs4.BeautifulSoup(res.text, "html.parser")

    elems = dailyDeals.select('.product')
    wholeString = ''
    listWords = ['Gaming', 'gaming', 'computer', 'Computer', 'pc', 'PC', 'laptop', 'Laptop', 'Batman', 'batman', 'joker', 'Joker', 'USB']

    for i in range(len(elems)):
        wholeString += elems[i].getText()

    for x in listWords:
        if x in wholeString:
            print 'theres a ' + x + ' deal on mightyape'

def hackerNews():
    res = requests.get('http://www.thehackernews.com/')
    res.raise_for_status()
    tweet = bs4.BeautifulSoup(res.text, "html.parser")
    read = ''
    words = ['Phone', 'phone', 'Phones', 'phones', 'tor', 'laptop', 'Laptop', 'Snowden']

    elems = tweet.select('a')
    for i in range(len(elems)):
        for word in words:
            if word in elems[i].getText():
                print elems[i].get('href')


def twitter():
    res = requests.get('https://www.twitter.com/th3j35t3r')
    res.raise_for_status()
    tweet = bs4.BeautifulSoup(res.text, "html.parser")

    elems = tweet.select('p')
    for i in range(len(elems)):
        print elems[i].getText().lstrip()
        print
        time.sleep(5)









if __name__ == "__main__":
    main()
