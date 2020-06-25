import scrapy

class MySpider(scrapy.spiders.CSVFeedSpider):
    name = "myspider"

    start_urls = [
        "file:///Users/kkim14/Box Sync/Personal/Data/product_id.csv"
    ]
    delimiter = ','
    headers = ['idx', 'product_id']

    def parse_row(self, response, row):
        # self.logger.info('Hi, this is a row!: %r', row)
        url="https://www.loft.com/{}".format(row["product_id"])
        yield scrapy.Request(url, callback=self.parse_url, cb_kwargs=dict(product_id=row["product_id"]))

    def parse_review(self, response):
        yield{
            "review": response.css("p::text").get()
        }

    def parse_url(self, response, product_id):
        yield{
            product_id: [response.css("h1::text").get(),
                         response.css(".color-families::text").get().split(":")[-1],
                         response.css(".description::text").get()]
        }

