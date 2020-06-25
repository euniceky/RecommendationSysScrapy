import scrapy
#from scrapy.http.request import Request


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
        #product_id=row["product_id"]
        yield scrapy.Request("https://api.bazaarvoice.com/data/batch.json?passkey=er2l539angpfdmmlhlp7vsxe6&apiversion=5.5&displaycode=0063-en_us&resource.q0=reviews&filter.q0=isratingsonly%3Aeq%3Afalse&filter.q0=productid%3Aeq%3A{}&filter.q0=contentlocale%3Aeq%3Aen_US&sort.q0=submissiontime%3Adesc&stats.q0=reviews&filteredstats.q0=reviews&include.q0=authors%2Cproducts%2Ccomments&filter_reviews.q0=contentlocale%3Aeq%3Aen_US&filter_reviewcomments.q0=contentlocale%3Aeq%3Aen_US&filter_comments.q0=contentlocale%3Aeq%3Aen_US&limit.q0=30&offset.q0=8&limit_comments.q0=3".format(row["product_id"]), callback= self.parse_review)
    #"https://api.bazaarvoice.com/data/batch.json?passkey=er2l539angpfdmmlhlp7vsxe6&apiversion=5.5&displaycode=0063-en_us&resource.q0=products&filter.q0=id%3Aeq%3A514433&stats.q0=reviews&filteredstats.q0=reviews&filter_reviews.q0=contentlocale%3Aeq%3Aen_US&filter_reviewcomments.q0=contentlocale%3Aeq%3Aen_US&resource.q1=reviews&filter.q1=isratingsonly%3Aeq%3Afalse&filter.q1=productid%3Aeq%3A{}&filter.q1=contentlocale%3Aeq%3Aen_US&sort.q1=submissiontime%3Adesc&stats.q1=reviews&filteredstats.q1=reviews&include.q1=authors%2Cproducts%2Ccomments&filter_reviews.q1=contentlocale%3Aeq%3Aen_US&filter_reviewcomments.q1=contentlocale%3Aeq%3Aen_US&filter_comments.q1=contentlocale%3Aeq%3Aen_US&limit.q1=8&offset.q1=0".format(row["product_id"]), callback= self.parse_review)
    #scrapy.Request(url, callback=self.parse_url, cb_kwargs=dict(product_id=row["product_id"]))

    #     #
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


# Keep in mind that in this case, requirements.txt file
# will list all packages that have been installed in virtual environment,
# regardless of where they came from


# #  This happens because parse() is Scrapy’s default callback method,
#  #  which is called for requests without an explicitly assigned callback.
#  def parse(self, response):
#      #print(response.css('.pagination-progress scrolled active p99 div.inset'))
#      for post in response.css('.product-wrap'):
#          yield{
#              'link': post.css('a::attr(href)')[1].get()
#          }


# def parse(self, response):
#     for post in response.css('.product-wrap'):
#         with open(filename, 'wb') as f:
#             json.dump(post.css('a::attr(href)')[1].get(), f)
