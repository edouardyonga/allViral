# -*- coding: utf-8 -*-
import scrapy
import json
import re

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

    def remove_re(string,reg_rmv,replace_with, self):

        
        new_string = string

        for character in reg_rmv:
          new_string = new_string.replace(character, replace_with)

        return new_string

    # def remove_re(string,reg_rmv,replace_with, self):

    #     # characters_to_remove = u"\u2018\u2019"
    #     new_string = str(string)

    #     for character in reg_rmv:
    #       re.sub(reg_rmv, replace_with, new_string)

    #     return new_string


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

        # image for next version
        # images = response.css('.post-block footer img::attr(src)').getall()
        # img_srcs = []

        # for img in images:
        #     image = img.split('?')
        #     img_srcs.append(image[0])
        #     pass
        

        for i in range(len(titles)):

            title = titles[i]
            link = links[i]
            description = descriptions[i]
            date = dates[i]
            author = authors[i]
            # img_link = img_srcs[i]


            
            title = titles[i].replace("\n", "").replace("\t", "").replace("\u2018", "'").replace("\u2019", "'")
            description =  descriptions[i].replace("\n", "").replace("\t", "").replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2014",", ")
            author = authors[i].replace("\n", "").replace("\t", "")

            # title = self.remove_re(title[i],"\u2018\u2019","'")
            # description = self.remove_re(descriptions[i],"\t\n","")
            


            # item = Article(title = title, link = link, description = description, date = date, author = author)
            article = {
                'title': title,
                'link': links[i],
                'description': description,
                'date': dates[i],
                'author': author,
                # 'image' : img_link
            }
            yield article

            jsonArticle = json.dumps(article)

        pass
