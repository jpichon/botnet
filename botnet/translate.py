import re
import urllib

from BeautifulSoup import BeautifulSoup

class Translator(object):

    def entofr(self, args):
        return self.translate('http://www.wordreference.com/enfr/' + args)

    def frtoen(self, args):
        return self.translate('http://www.wordreference.com/fren/' + args)

    def translate(self, url):
        f = urllib.urlopen(url)
        data = f.read()
        f.close()
        soup = BeautifulSoup(data)

        # The div we're interested in is obfuscated, so we get to it using the xpath
        search_results = soup.find('td', attrs={'class':'content'}).find('div').find('div')

        if not len(search_results):
            return "No results found."

        return self.remove_html_tags(str(search_results))

    def remove_html_tags(self, text):
        p = re.compile(r'<.*?>')
        return p.sub('', text)
