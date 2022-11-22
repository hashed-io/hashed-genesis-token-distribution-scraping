from doctest import OutputChecker
import scrapy
import json

from src.items import SrcItem
from scrapy.loader import ItemLoader

# $ scrapy shell "https://parachains.info/details/dora_factory#token"

# parachain_text

def format_item(value):
    if value:
        output = ""

        value.pop(0)
        value.pop(0)
        value.pop(0)
        value.pop(0)

        for k in value:
            output += k

        return output

    else:
        return value

def get_table_item(value, regex):
    try:
        if value.css('span.font-weight-bold::text').re(regex):
            output = value.css('span.font-weight-bold::text').re(regex)[0]
    except:
        output = ""
    
    return output


def format_text(value, dirty, format):
    if value:
        return value.replace(dirty, format)
    
    else:
        return ""

class GenesisToken(scrapy.Spider):
	
    name = 'GenesisToken'
    allowed_domains = ['parachains.info']

    def start_requests(self):
        
        url = 'https://parachains.info/'
        
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info('Getting links')

        links = response.css('a.d-flex.align-self-center.mr-3.parachain_url::attr(href)').getall()

        for link in links:
            yield scrapy.Request('https://parachains.info' + link + '#token', self.parse_parachain)


    def parse_parachain(self, response):
        self.logger.info('parse_token')

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
        item["relay_chain"] = response.css("div.parachain_text::text").get().replace("\n", "")
        item["link"] = response.url

        try:
            tags = []
            chaing_tag = response.css('span.rounded-pill::text').getall()
            for tag in chaing_tag:
                tags.append(tag.replace("\n", ""))
            self.logger.info(tags)
        except:
            tags = "None"
            self.logger.info(tags)
        
        item["chain_tag"] = tags

        try:
            market_supply = response.css('div.row.tokenomic_row')[2].re('\d+')
        
            self.logger.info("dirty market_supply")
            self.logger.info(market_supply)

            item["market_supply"] = format_item(market_supply)
        except:
            item["market_supply"] = 0

        try:
            circulation_supply = response.css('div.row.tokenomic_row')[3].re('\d+')

            self.logger.info("dirty circulation_supply")
            self.logger.info(circulation_supply)

            item["circulation_supply"] = format_item(circulation_supply)

        except:
            item["circulation_supply"] = "0"


        try:
            coingecko = response.css('a.material-tooltip-smaller.parachain_url').attrib['href']

            self.logger.info("dirty market_cap")
            self.logger.info(coingecko)
            item['coingecko'] = coingecko

        except:
            item['coingecko'] = ""


        try:
            market_cap = response.css('div.row.tokenomic_row')

            dic = {}
            counter = 0
            for i in market_cap:
                if counter != 0:
                    dic[i.css('span.font-weight-bold::text').get()] = i.css('div.col-6.col-md-8.m-auto::text').get().replace("\n", "")
                    if i.css('span.font-weight-bold::text').re('[Mm]arket\s[Cc]ap.'):
                        market_cap_key = get_table_item(i, '[Mm]arket\s[Cc]ap.')

                    if i.css('span.font-weight-bold::text').re('[Tt]otal\s[Ss]upply.'):
                        total_supply_key = get_table_item(i, '[Tt]otal\s[Ss]upply.')

                    if i.css('span.font-weight-bold::text').re('[Cc]irculation\s[Ss]upply.'):
                        circulation_supply_key = get_table_item(i, '[Tt]irculation\s[Ss]upply.')
                counter += 1

            self.logger.info("dirty market_cap")
            self.logger.info(market_cap)
            self.logger.info(dic)
            self.logger.info(market_cap_key)
            self.logger.info(dic[market_cap_key])

            item["market_cap"] = format_text(dic[market_cap_key].replace("$", ""), " ", "")
            item["token_info"] = dic

        except:
            item["market_cap"] = 0
            item["token_info"] = dic

        try:
            pattern = r'dataset: {[\r\n]+([^\r\n]+)' # there is a variable in the script with this pattern
            token_dist = response.css('script::text').re_first(pattern) # get the data with the pattern

            token_dist = format_text(token_dist, " ", "")
            # making sure the output is a JSON
            token_dist = token_dist.replace(" ", "")
            token_dist = token_dist.replace("source", "\"source\"")
            token_dist = "{" + token_dist + "}"
            token_dist = json.loads(token_dist) # details json var

            self.logger.info(token_dist["source"])

            item["token_distribution"] = token_dist["source"]

        except:
            item["token_distribution"] = []

        yield item
