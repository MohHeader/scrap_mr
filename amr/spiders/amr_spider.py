import scrapy
from amr.items import AmrItem

class Amrpider(scrapy.Spider):
    name = "amr"
    allowed_domains = ["ldlp-dictionary.com"]
    start_urls = ['http://www.ldlp-dictionary.com/dictionaries/word/%d/ /0/Al-Mughni Al-Akbar (En/Ar)' %(n) for n in range(4277183, 4277190)]
# from  : 4277183
# to    : 4391332
    def parse(self, response):
        item = AmrItem()
        item['english'] = response.css("#keywordContainer .keyword::text").extract()
        print response.css(".definitionListEntry::text")[0].extract()
        item['arabic'] = response.css(".definitionListEntry::text")[0].extract()
        yield item
