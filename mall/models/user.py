from django.db import models
from .base_model import BaseModel


class User(BaseModel):
    """用户表"""
    username = models.CharField(max_length=18, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    info = models.OneToOneField('UserInfo', on_delete=models.CASCADE, verbose_name="用户信息信息")


# 用户信息表
class UserInfo(BaseModel):
    """用户信息表"""
    pass


# 地区表
class City(BaseModel):
    """地区表"""
    name = models.CharField(max_length="地区名称")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="父地区id")


# 收货地址表
class Addr(BaseModel):
    """收货地址表"""
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="用户")
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name="地区")
    addr = models.CharField(max_length=256, verbose_name="收货地址(不包含省, 市, 区)")
    addr_detail = models.CharField(max_length=256, verbose_name="收货地址(完整地址)")
    name = models.CharField(max_length=20, verbose_name="收货人姓名")
    tel = models.CharField(max_length=20, verbose_name="收货人手机号")
    default = models.BooleanField(default=False, verbose_name="是否为默认收货地址")
