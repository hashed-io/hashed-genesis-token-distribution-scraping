import scrapy
import json

from src.items import SrcItem
from scrapy.loader import ItemLoader


class GenesisToken(scrapy.Spider):
	
    name = 'GenesisToken'
    allowed_domains = ['parachains.info']

    def start_requests(self):
        urls = [
            'https://parachains.info/details/acala_network#token/'
          ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info('In parse info')

        item = SrcItem()
        # h4 mb-0 d-flex flex-wrap align-items-center
        token_name = response.css('div').re('.*h3.*')
        self.logger.info("dirty name")
        self.logger.info(token_name[0])
        token_name = token_name[0]
        token_name = token_name.replace("<h1 class=\"h3 mb-0\">", "")
        token_name = token_name.replace("</h1>", "")

        self.logger.info(token_name)

        item["name"] = token_name

        # delete the first 4 elements on those variables
        market_supply = response.css('div.row.tokenomic_row')[2].re('\d+')
        circulation_supply = response.css('div.row.tokenomic_row')[3].re('\d+')
        market_cap = response.css('div.row.tokenomic_row')[4].re('\d+') # market cap

        # item["market_supply"] = market_supply

        pattern = r'dataset: {[\r\n]+([^\r\n]+)' # there is a variable in the script with this pattern
        token_dist = response.css('script::text').re_first(pattern) # get the data with the pattern

        # making sure the output is a JSON
        token_dist = token_dist.replace(" ", "")
        token_dist = token_dist.replace("source", "\"source\"")
        token_dist = "{" + token_dist + "}"
        token_dist = json.loads(token_dist) # details json var
        self.logger.info(market_supply)

        yield item
