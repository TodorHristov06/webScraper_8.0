import scrapy


class DesktopbgSpiderSpider(scrapy.Spider):
    name = "desktopbg_spider"
    allowed_domains = ["desktop.bg"]
    start_urls = ["https://desktop.bg"]

    def parse(self, response):
        pass
