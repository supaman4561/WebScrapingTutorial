from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/'
                  'Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items',
            follow=True)]
    
    def parse_items(self, res):
        url = res.url
        title = res.css('h1::text').extract_first()
        text = res.xpath('//div[@id="mw-content-text"]//text()').extract()
        last_updated = res.css('li#footer-info-lastmod::text').extract_first()
        last_updated = last_updated.replace('This page was last edited on ', '')
        print("URL is: {}".format(url))
        print("title is: {}".format(title))
        print("text is: {}".format(text))
        print("Last Updated: {}".format(last_updated))