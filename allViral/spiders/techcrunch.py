# -*- coding: utf-8 -*-
import scrapy
import json

class Article(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    pass


class TechcrunchSpider(scrapy.Spider):
    name = 'techcrunch'
    allowed_domains = ['techcrunch.com']
    start_urls = ['http://techcrunch.com/']

    def parse(self, response):
        # title
        titles = response.css('a.post-block__title__link::text').getall()

        # description
        descriptions = response.css('div.post-block__content::text').getall()

        # link
        links = response.css('a.post-block__title__link::attr(href)').getall()

        # date
        # still need to work on the time zone and format 
        dates = response.css('time::attr(datetime)').getall()

        # author
        authors = response.css('div span.river-byline__authors a::text').getall()

        # image
        images = response.css('.post-block__media img::attr(src)').getall()
        img_srcs = []

        for img in images:
            image = img.split('?')
            img_srcs.append(image[0]) 
            pass

        for i in range(len(titles)):

            title = titles[i]
            link = links[i]
            description = descriptions[i]
            date = dates[i]
            author = authors[i]
            img_link = img_srcs[i]


            # item = Article(title = title, link = link, description = description, date = date, author = author)
            article = {
                'title': titles[i],
                'link': links[i],
                'description': descriptions[i],
                'date': dates[i],
                'author': authors[i],
                'image' : img_link
            }
            yield article

            jsonArticle = json.dumps(article)

        pass
