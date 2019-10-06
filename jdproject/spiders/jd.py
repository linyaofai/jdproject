# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from scrapy_splash.request import SplashRequest, SplashFormRequest


class JdSpider(scrapy.Spider):
    name = "jd"

    def start_requests(self):
        splash_args = {"lua_source": """
                    --splash.response_body_enabled = true
                    splash.private_mode_enabled = false
                    splash:set_user_agent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
                    assert(splash:go("https://item.jd.com/5089239.html"))
                    splash:wait(3)
                    return {html = splash:html()}
                    """}
        yield SplashRequest("https://item.jd.com/5089239.html", endpoint='run', args=splash_args, callback=self.onSave)

    def onSave(self, response):
        value = response.xpath('//span[@class="p-price"]//text()').extract()
        print(value)