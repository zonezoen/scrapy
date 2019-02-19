from scrapy.cmdline import execute

import sys
import os
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","jd_spider"])
# setting --> ROBOTSTXT_OBEY = False


