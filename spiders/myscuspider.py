import scrapy
from scuspider.items import ScuspiderItem
from scrapy.selector import Selector

class ScuSpider(scrapy.Spider):
    name = "myscuspider"
    Login_urls = "http://zhjw.scu.edu.cn/loginAction.do"
    start_urls = "http://zhjw.scu.edu.cn/gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2017-2018%D1%A7%C4%EA%C7%EF(%C1%BD%D1%A7%C6%DA)"

    def start_requests(self):
        return [scrapy.Request(self.Login_urls,
                               meta={'cookiejar' : 1},
                               callback=self.logging_first)]

    def logging_first(self, response):
        return [scrapy.FormRequest.from_response(response,
                                                 url=self.Login_urls,
                                                 meta={'cookiejar': response.meta['cookiejar']},
                                                 formdata={
                                                     'zjh' : '*************',
                                                     'mm' : '******'
                                                 },
                                                 callback=self.logging_second)]

    def logging_second(self, response):
        yield scrapy.Request(self.start_urls,
                             meta={'cookiejar': True},
                             callback=self.after_logged)

    def after_logged(self, response):
        temp = Selector(response)
        courses = temp.xpath('//table[@class="titleTop2"]/tr/td[@class="pageAlign"]/table/tr[@class="odd"]')
        for course in courses:
            item = ScuspiderItem()
            item['num1'] = course.xpath('.//td[@align="center"]/text()').extract()[0].strip()
            item['num2'] = course.xpath('.//td[@align="center"]/text()').extract()[1].strip()
            item['name_en'] = course.xpath('.//td[@align="center"]/text()').extract()[2].strip()
            item['name_ch'] = course.xpath('.//td[@align="center"]/text()').extract()[3].strip()
            item['value'] = course.xpath('.//td[@align="center"]/text()').extract()[4].strip()
            item['_type'] = course.xpath('.//td[@align="center"]/text()').extract()[5].strip()
            item['grades'] = course.xpath('.//td[@align="center"]/p[@align="center"]/text()').extract()[0].strip('\xa0')
            yield item