import scrapy


class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://bbc.com/news/'
    ]

    def parse(self, response):
        for post in response.css('div.nw-c-top-stories--international .nw-c-top-stories__secondary-item '):
            yield {
               'title':  post.css('.gs-c-promo-body .gs-c-promo-heading h3::text')[0].get(),
               'description': post.css('.gs-c-promo-body  p::text')[0].get(),
               'image': post.css('.gs-c-promo-image .gs-o-responsive-image img::attr(src)').get(),
              
            }
        