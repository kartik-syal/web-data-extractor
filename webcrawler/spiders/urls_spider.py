import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class UrlsSpider(CrawlSpider):
    name = "urls"
    allowed_domains = ['domain.com']  # Replace with the target website's domain
    start_urls = ['https://domain.com']  # Replace with the target website

    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        self.logger.info('Crawling URL: %s', response.url)
        yield {
            'url': response.url,
            'title': response.css('title::text').get(),
        }

# Customize Scrapy settings
process = CrawlerProcess(settings={
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'urls.csv',
    'ROBOTSTXT_OBEY': True,  # Respect robots.txt rules
    'LOG_LEVEL': 'INFO',  # Reduce logging verbosity
    'DEPTH_LIMIT': 5,  # Increase depth limit
    'CLOSESPIDER_PAGECOUNT': 1000,  # Adjust as needed
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',  # Use a common user agent
})

process.crawl(UrlsSpider)
process.start()
