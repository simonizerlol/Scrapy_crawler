import scrapy

class newsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        'http://www.ithome.com.tw/security',
    ]

    def parse(self, response):
        for quote in response.css('div.span4.channel-item'):
            yield {
                'title': quote.css('p.title::text()').extract_first(),
				
				'link': quote.xpath('//a/@href').extract_first(),
                'date': quote.xpath('p.post-at').extract_first(),
            }

       