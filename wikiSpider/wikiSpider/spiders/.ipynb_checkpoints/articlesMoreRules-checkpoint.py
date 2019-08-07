from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/'
                 'Benevolent_dictator_for_life']
    rules = [
        Rule(LinkExtractor(allow='^(/wiki/)((?!:).)*$'),
             callback='parse_items', follow=True,
             cb_kwargs={'is_article': True}),
        Rule(LinkExtractor(allow='.*'), callback='parse_items', 
             cb_kwargs={'is_article': False})
    ]
    
    def parse_items(self, res, is_article):
        print(res.url)
        title = res.css('h1::text').extract_first()
        if is_article:
            url = res.url
            text = res.xpath('//div[@id="mw-content-text"]//text()').extract()
            last_updated = res.css('li#footer-info-lastmod::text').extract_first()
            last_updated = last_updated.replace('This page was last edited on ', '')
            print("title is: {}".format(title))
            print("text is: {}".format(text))
            print("Last Updated: {}".format(last_updated))
        else:
            print('This is not an article: {}'.format(title))