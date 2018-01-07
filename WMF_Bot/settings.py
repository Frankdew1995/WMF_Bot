# -*- coding: utf-8 -*-

# Scrapy settings for WMF_Bot project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WMF_Bot'

SPIDER_MODULES = ['WMF_Bot.spiders']
NEWSPIDER_MODULE = 'WMF_Bot.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# # Override the default request headers:
# HEADERS = {
#   'Accept': '*/*',
#   'Accept-Language': 'en,zh;q=0.9,zh-CN;q=0.8,en-US;q=0.7',
# 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',

# 'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=en&v=v1514934548259&k=6LekTicUAAAAACZMK-qKBQ1rHto-e5jtObCXCtLs',

# 'cookie':'CONSENT=YES+DE.zh-CN+20150712-15-0; OTZ=4205312_52_52_123900_48_436380; SID=mAWQiipiwAv7TDm-gduPALU12dO5vb9_Zf5FNX9oULJnmYuu8TlRpVXYGXFr3rVGC1qTyg.; HSID=A0BYsz6XjlLOeTFiU; SSID=A31K2Fwo4oZXdEPDA; APISID=xie7ONEkkOix72lH/AiiaDOkeQX_2vESo9; SAPISID=myFhtnCX7LkINXdd/APZjL-ImxdPlAob_b; NID=121=QhN_-BoLrJ1TOXS4VDn6DVMI7gZF0nctnTQK2Quta5F2tmJTj9M3Wx1Bc6SJwVnuwKvYYLwJxBfslHJVVurRARS0_9GZDskqXr4SSItG3m560VGDPf5Us-lkF5dVRC02J-97SV9VPh_sCpYUdf16R8cvChh5FeW-cRF6nU_YVL9s4zu9VENY3m9uny1IGxPVnoBUKTWNIiFLpqeDfQQk-vuJgc6zOIEvt0uXQwG09VScEbEiGqveLr3vFFlBWNTBBlUslHO1; 1P_JAR=2018-1-7-10; SIDCC=AAiTGe_T00Df9uHp60cktafsV-xdJgSvjT13-PfDW_NBPZzH1NQZsGMAxAqNUo5iWE2T2Nx5kQg',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
SPLASH_URL = 'http://localhost:8050/'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'WMF_Bot.pipelines.WmfBotPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
