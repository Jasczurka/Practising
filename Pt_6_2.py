import scrapy
from scrapy.crawler import CrawlerProcess


class SteamSpider(scrapy.Spider):
    name = 'steam_tags'
    allowed_domains = ["store.steampowered.com"]
    url = "https://store.steampowered.com/search/?category1=" \
          "998&filter=topsellers&ndl=1&page=%s"
    page = 1
    start_urls = [url % page]
    count = 0
    games_num = 1000

    def parse(self, response):
        for el in response.css("a.search_result_row.ds_collapse_flag"):
            yield response.follow(el, callback=self.tags,
                                  cookies={'birthtime': 567891332})
        if self.count < self.games_num:
            self.page += 1
            yield response.follow(self.url % self.page, callback=self.parse)

    def tags(self, response):
        if 'sub/' in response.url:
            return
        if self.count >= self.games_num:
            return
        self.count += 1
        game = response.css("div.apphub_AppName::text").get()
        yield {
            'name': game,
            'tags': list(
                map(str.strip, response.css("a.app_tag::text").getall()))
        }


if __name__ == "__main__":
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "tags.csv": {"format": "csv"},
            },
        }
    )

    process.crawl(SteamSpider)
    process.start()
