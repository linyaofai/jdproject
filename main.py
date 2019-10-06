from scrapy import cmdline, Spider
if __name__ == '__main__':
    cmdline.execute("scrapy crawl jd --nolog ".split())