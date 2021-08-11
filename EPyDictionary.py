import sys, re
import requests
from bs4 import BeautifulSoup

def soup_this(url, parser="html.parser"):
    return BeautifulSoup(requests.get(url).text, parser)


python2 = False
if list(sys.version_info)[0] == 2:
    python2 = True

class PyDictionary(object):

    def __init__(self, *args):
        try:
            if isinstance(args[0], list):
                self.args = args[0]
            else:
                self.args = args
        except:
            self.args = args

    @staticmethod
    def meaning(term):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                html = soup_this("http://wordnetweb.princeton.edu/perl/webwn?s={0}".format(term))
                types = html.findAll("h3")
                lists = html.findAll("ul")
                out = {}
                if types[0].text == "Your search did not return any results.":
                    return None
                for a in types:
                    reg = str(lists[types.index(a)])
                    meanings = []
                    for x in re.findall(r'> \((.*?)\) <', reg):
                        if 'often followed by' in x:
                            pass
                        elif len(x) > 5 or ' ' in str(x):
                            meanings.append(x)
                    name = a.text
                    out[name] = meanings
                return out
            except:
                return None