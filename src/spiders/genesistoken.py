from doctest import OutputChecker
import scrapy
import json

from src.items import SrcItem
from scrapy.loader import ItemLoader

# $ scrapy shell "https://parachains.info/details/nodle#token"

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

def get_url_batch(n):
    if n == 1:
        urls = [
                'https://parachains.info/details/dora_factory#token',
                'https://parachains.info/details/acala_network#token'
                'https://parachains.info/details/karura#token',
                'https://parachains.info/details/bit_country_pioneer#token',
                'https://parachains.info/details/shiden_network#token',
                'https://parachains.info/details/astar#token',
                'https://parachains.info/details/bifrost_finance#token',
                'https://parachains.info/details/bifrost_finance_polkadot#token',
                'https://parachains.info/details/pichiu#token',
                'https://parachains.info/details/equilibrium#token',
                'https://parachains.info/details/genshiro#token',
                'https://parachains.info/details/nodle#token',
                'https://parachains.info/details/crust_shadow#token',
                'https://parachains.info/details/calamari_network#token',
                'https://parachains.info/details/parallel_finance#token',
                'https://parachains.info/details/heiko_finance#token',
                'https://parachains.info/details/centrifuge#token',
                'https://parachains.info/details/moonbeam#token'
                ]
    if n==2:
        urls = [
            'https://parachains.info/details/moonriver#token',
            'https://parachains.info/details/altair#token',
            'https://parachains.info/details/litentry#token',
            'https://parachains.info/details/litmus#token',
            'https://parachains.info/details/integritee#token',
            'https://parachains.info/details/unique_network#token',
            'https://parachains.info/details/subsocial#token',
            'https://parachains.info/details/khala#token',
            'https://parachains.info/details/phala_network#token',
            'https://parachains.info/details/hydradx#token',
            'https://parachains.info/details/turing_network#token',
            'https://parachains.info/details/darwinia_crab#token',
            'https://parachains.info/details/interlay#token',
            'https://parachains.info/details/kintsugi#token',
            'https://parachains.info/details/basilisk#token',
            'https://parachains.info/details/quartz#token',
            'https://parachains.info/details/kilt_protocol#token',
            'https://parachains.info/details/robonomics#token',
            'https://parachains.info/details/sora#token',
            'https://parachains.info/details/encointer#token']
    if n==3:
        urls = [
            'https://parachains.info/details/picasso#token',
            'https://parachains.info/details/composable_finance#token',
            'https://parachains.info/details/polkadex#token',
            'https://parachains.info/details/efinity#token',
            'https://parachains.info/details/zeitgeist#token',
            'https://parachains.info/details/clover_finance#token',
            'https://parachains.info/details/sakura#token',
            'https://parachains.info/details/mangata_x#token',
            'https://parachains.info/details/origintrail#token',
            'https://parachains.info/details/kico#token',
            'https://parachains.info/details/bajun_network#token',
            'https://parachains.info/details/imbue_network#token',
            'https://parachains.info/details/coinversation_protocol#token',
            'https://parachains.info/details/listen#token',
            'https://parachains.info/details/tanganika#token',
            'https://parachains.info/details/kabocha#token',
            'https://parachains.info/details/totem#token',
            'https://parachains.info/details/geminis#token',
            'https://parachains.info/details/bit_country#token',
            'https://parachains.info/details/subdao#token']
    if n==4:
        urls = [
            'https://parachains.info/details/konomi#token',
            'https://parachains.info/details/kylin_network#token',
            'https://parachains.info/details/standard_protocol#token',
            'https://parachains.info/details/unorthodox#token',
            'https://parachains.info/details/crust_network#token',
            'https://parachains.info/details/manta_network#token',
            'https://parachains.info/details/kpron_network#token',
            'https://parachains.info/details/apron_network#token',
            'https://parachains.info/details/idavoll_network#token',
            'https://parachains.info/details/oak_network#token',
            'https://parachains.info/details/darwinia#token',
            'https://parachains.info/details/ares_protocol#token',
            'https://parachains.info/details/mars#token',
            'https://parachains.info/details/t3rn#token',
            'https://parachains.info/details/invarch#token',
            'https://parachains.info/details/subgame#token',
            'https://parachains.info/details/subgame_gamma#token',
            'https://parachains.info/details/laminar#token',
            'https://parachains.info/details/shadows_network#token',
            'https://parachains.info/details/polkasmith#token']
    if n==5:
        urls = [
            'https://parachains.info/details/polkafoundry#token',
            'https://parachains.info/details/subspace#token',
            'https://parachains.info/details/trustbase#token',
            'https://parachains.info/details/loom_network#token',
            'https://parachains.info/details/mathchain#token',
            'https://parachains.info/details/zcloak#token',
            'https://parachains.info/details/sherpax#token',
            'https://parachains.info/details/valiu#token',
            'https://parachains.info/details/ternoa#token',
            'https://parachains.info/details/datahighway#token',
            'https://parachains.info/details/uniarts_network#token',
            'https://parachains.info/details/dico#token',
            'https://parachains.info/details/patract#token',
            'https://parachains.info/details/zero#token',
            'https://parachains.info/details/celer_network#token',
            'https://parachains.info/details/cere_network#token',
            'https://parachains.info/details/dock#token',
            'https://parachains.info/details/ajuna_network#token',
            'https://parachains.info/details/stonedefi#token',
            'https://parachains.info/details/stafi#token']
    if n==6:
        urls = [
            'https://parachains.info/details/nsure_network#token',
            'https://parachains.info/details/akropolis#token',
            'https://parachains.info/details/deeper_network#token',
            'https://parachains.info/details/ruby_protocol#token',
            'https://parachains.info/details/pendulum#token',
            'https://parachains.info/details/amplitude#token',
            'https://parachains.info/details/opensquare_network#token',
            'https://parachains.info/details/layerx_zerochain#token',
            'https://parachains.info/details/dot_mog#token',
            'https://parachains.info/details/datdot#token',
            'https://parachains.info/details/cap9#token',
            'https://parachains.info/details/evercity#token',
            'https://parachains.info/details/zeropool#token',
            'https://parachains.info/details/dipole#token',
            'https://parachains.info/details/definex#token',
            'https://parachains.info/details/caelum_labs#token',
            'https://parachains.info/details/snowfork#token',
            'https://parachains.info/details/tea_project#token',
            'https://parachains.info/details/chainlink#token',
            'https://parachains.info/details/subquery#token'
          ]
    if n==7:
        urls = [
            'https://parachains.info/details/joystream#token',
            'https://parachains.info/details/bluzelle#token',
            'https://parachains.info/details/reef#token',
            'https://parachains.info/details/riodefi#token',
            'https://parachains.info/details/tidal_finance#token',
            'https://parachains.info/details/linear#token',
            'https://parachains.info/details/mxc#token',
            'https://parachains.info/details/covercompared#token',
            'https://parachains.info/details/paralink_network#token',
            'https://parachains.info/details/gear#token',
            'https://parachains.info/details/etha_lend#token',
            'https://parachains.info/details/fractal#token',
            'https://parachains.info/details/royale#token',
            'https://parachains.info/details/automata#token',
            'https://parachains.info/details/mantraDAO#token',
            'https://parachains.info/details/exeedme#token',
            'https://parachains.info/details/edgeware#token',
            'https://parachains.info/details/chainx#token',
            'https://parachains.info/details/mangata_finance#token',
            'https://parachains.info/details/bondly#token']
    if n==8: 
        urls = [
            'https://parachains.info/details/rai_finance#token',
            'https://parachains.info/details/bandot#token',
            'https://parachains.info/details/energy_web#token',
            'https://parachains.info/details/gamedao#token',
            'https://parachains.info/details/oax_foundation#token',
            'https://parachains.info/details/polkabridge#token',
            'https://parachains.info/details/xpredict#token',
            'https://parachains.info/details/momentum#token',
            'https://parachains.info/details/compound_gateway#token',
            'https://parachains.info/details/kulupu#token',
            'https://parachains.info/details/bitgreen#token',
            'https://parachains.info/details/peaq#token',
            'https://parachains.info/details/map_protocol#token',
            'https://parachains.info/details/seor#token',
            'https://parachains.info/details/acuity_social#token',
            'https://parachains.info/details/bestay#token',
            'https://parachains.info/details/sunrise_protocol#token',
            'https://parachains.info/details/everlife_ai#token',
            'https://parachains.info/details/summa_network#token',
            'https://parachains.info/details/dego_finance#token']
    if n==9: 
        urls =[
            'https://parachains.info/details/shift#token',
            'https://parachains.info/details/curio#token',
            'https://parachains.info/details/hazel#token',
            'https://parachains.info/details/cdot#token',
            'https://parachains.info/details/wiv#token',
            'https://parachains.info/details/polimec#token',
            'https://parachains.info/details/pulse_network#token' ]

    return urls
class GenesisToken(scrapy.Spider):
	
    name = 'GenesisToken'
    allowed_domains = ['parachains.info']

    def start_requests(self):
        
        urls = get_url_batch(3)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    # def parse(self, response):
    #     self.logger.info('parse')

    #     table = response.css("table.table-sm.main_table")

    #     row = table.xpath('//tr')

    #     self.logger.info(table)

    def parse(self, response):
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
