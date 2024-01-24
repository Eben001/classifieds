import scrapy
from classifieds.items import ClassifiedsItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor




class ClickinSpider(CrawlSpider):
    name = "clickin"
    allowed_domains = ["click.in"]
    start_urls = ["https://www.click.in/automobiles-ctgid150"]
    

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("product-grid__items css-hvew4t")), 
             callback="parse", follow=True),
    )

    def parse(self, response):
        item = ItemLoader(item=ClassifiedsItem(), response=response, selector=response)
        item.add_xpath("title", ".//h2/text()")
        item.add_xpath("make", ".//div[div='Make']/div[@clas='clickin-post-blackbold']/text()")
        item.add_xpath("model", ".//div[div='Model']/div[@class='clickin-post-blackbold']/text()")
        item.add_xpath("manfuctured_year", ".//div[div='Manufactured Year']/div[@class='clickin-post-blackbold']/text()")
        item.add_xpath("locality", ".//div[div='Locality']/div[@class='clickin-post-blackbold']/text()")
        item.add_xpath("company_name", ".//div[div='Company name']/div[@class='clickin-post-blackbold']/text()")
        yield item.load_item()