from django.db import models


# Create your models here.
class Portfolio(models.Model):  #资产组合表结构
    pname = models.CharField(max_length=100) #资产组合名称
    pnum = models.IntegerField() #资产数量
    isDelete = models.BooleanField(default=False) #是否删除


class Asset(models.Model): #资产表结构
    aname = models.CharField(max_length=100) #资产名称
    acode = models.CharField(max_length=100) #资产代码
    abelong = models.ForeignKey("Portfolio", on_delete=models.CASCADE) #关联外键，所属资产组合
    isDelete = models.BooleanField(default=False) #是否删除


class tData(models.Model): #交易数据表结构
    date = models.DateTimeField() #日期
    open = models.FloatField() #开盘价
    close = models.FloatField() #收盘价
    high = models.FloatField() #最高价
    low = models.FloatField() #最低价
    volume = models.FloatField() #成交量
    tbelong = models.ForeignKey("Asset", on_delete=models.CASCADE) #关联外键，交易数据所属资产
    isDelete = models.BooleanField(default=False) #是否删除