# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
from wikiSpider.items import Article
from string import whitespace

class WikispiderPipeline(object):
    def process_item(self, item, spider):
        date_str = article['last_updated']
        article['last_updated'] = article['last_updated']
            .replace('This page was last edited on ', '')
        article['last_updated'] = article['last_updated'].strip()
        article['last_updated']  datetime.strptime(
            article['last_updated'], '%d %B %Y, at %H:%M.')
        article['text'] = [line for line in article['text'] if line not in whitespace]
        article['text'] = ''.join(article['text'])
        return article