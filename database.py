from AssetInvestment.models import Portfolio, Asset, tData
from django.utils import timezone
from datetime import *

portfolio1 = Portfolio()
portfolio1.pname = "组合1"
portfolio1.pnum = 5
portfolio1.save()
portfolio2 = Portfolio()
portfolio2.pname = "组合2"
portfolio2.pnum = 5
portfolio2.save()
portfolio3 = Portfolio()
portfolio3.pname = "组合3"
portfolio3.pnum = 5
portfolio3.save()
portfolio4 = Portfolio()
portfolio4.pname = "组合4"
portfolio4.pnum = 5
portfolio4.save()

asset1 = Asset()
asset1.aname = "平安银行"
asset1.acode = "000001"
asset1.abelong = portfolio1
asset1.save()
asset12 = Asset()
asset12.aname = "招商银行"
asset12.acode = "600036"
asset12.abelong = portfolio1
asset12.save()
asset13 = Asset()
asset13.aname = "贵州茅台"
asset13.acode = "600519"
asset13.abelong = portfolio1
asset13.save()
asset14 = Asset()
asset14.aname = "海通证券"
asset14.acode = "600837"
asset14.abelong = portfolio1
asset14.save()
asset15 = Asset()
asset15.aname = "万华化学"
asset15.acode = "600309"
asset15.abelong = portfolio1
asset15.save()
