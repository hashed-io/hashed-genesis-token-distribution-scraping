# hashed-genesis-token-distribution-scraping

## Create a vitual env

### Linux and macOS

``` bash
python3 -m venv virtual_environment_name
```

### Linux and macOS
``` bash
source virtual_environment_name/bin/activate
```

## Install all requirements

install all requirements


## Run the spider

To debug the spider, run the following command
``` bash
scrapy crawl GenesisToken
```


To save data of the spider, run the following command
``` bash
scrapy crawl GenesisToken -O token_info.json
```
