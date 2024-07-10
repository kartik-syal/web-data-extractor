from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from webcrawler.spiders.urls_spider import UrlsSpider

process = CrawlerProcess(get_project_settings())
process.crawl(UrlsSpider)
process.start()  # This will block until the spider finishes
