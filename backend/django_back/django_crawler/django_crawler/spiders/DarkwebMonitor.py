import scrapy
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk import PorterStemmer
import re
from scrapy.selector import Selector
from .. import views as vi


stemmer = PorterStemmer()
STOPS = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace('  ', ' ')
    text = text.translate(str.maketrans('', '', punctuation))
    word_list = text.split(' ')
    filtered_words = [word for word in word_list if word not in STOPS]
    return filtered_words

from nltk.tokenize import sent_tokenize

def clean2(content):
    # Remove Tags
    soup = BeautifulSoup(content, "html.parser")
    text_content = soup.get_text().replace('\n',' ').replace('  ',' ')

    # Tokenize into sentences
    sentences = sent_tokenize(text_content)
    return sentences

def passdata(data):
    vi.input_list(data)
    return

class DrlSpider(scrapy.Spider):
    def __init__(self):
        self.Entire_page = ["Hello"]
    name = 'DRL'
    allowed_domains = ['onion']
    def start_requests(self):
        urls = ['http://c32zjeghcp5tj3kb72pltz56piei66drc63vkhn5yixiyk4cmerrjtid.onion/f/guns/comments']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    

    def parse(self, response):
        print("print4")
        soup = BeautifulSoup(response.body, "html.parser")
        links = set()

        for link in soup.findAll('a'):
            inspect_link = link.get('href')
            if inspect_link and '.onion' in inspect_link:
                links.update({inspect_link})

        title_tag = soup.title
        title = title_tag.text if title_tag else ''
        title_keywords = Counter(clean_text(title))


        meta_tags = soup.find_all('meta')

        keywords = ''
        description = ''

        for meta_tag in meta_tags:
            if meta_tag.get('name') in ['keywords', 'Keywords']:
                keywords = Counter(clean_text(meta_tag.get('content')))
                break

        for meta_tag in meta_tags:
            if meta_tag.get('name') in ['description', 'Description']:
                description = meta_tag.get('content')
                break

        #word_frequency = Counter(clean_text(response.text))

        meta_data = {key:val for key, val in response.meta.items() if key not in ['proxy', 'download_timeout']}

        selector = Selector(text = response.text)
        #comments = selector.xpath('//p/text()').extract()
        print("print1")
        self.Entire_page = clean2(response.text)
        passdata(self.Entire_page)
        
        # yield {
        #     'url': response.url,
        #     'title': title,
        #     'title_keywords': dict(title_keywords),
        #     'keywords': dict(keywords),
        #     'description': description,
        #     'meta': meta_data,
        #     # 'Data' : comments,
        #     #'content' : Entire_page,
        # }
        #print("Entire Page data tokens:",Entire_page)
        for next_page in links:
            if next_page:
                yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

