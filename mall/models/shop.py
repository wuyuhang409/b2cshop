from .base_model import BaseModel
from django.db import models


# 商品分类表
class GoodsCategory(BaseModel):
    """商品分类表"""
    name = models.CharField(max_length=50, verbose_name="分类名称")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="父分类id")


# 商品SPU表(商品总述)
class GoodsSPU(BaseModel):

    title = models.CharField(max_length=255, verbose_name="商品标题")
    name = models.CharField(max_length=255, verbose_name='商品名称')
    description = models.CharField(max_length=255, verbose_name="商品描述")
    cover = models.CharField(max_length=255, verbose_name="封面")
    content = models.TextField(verbose_name="商品详情(富文本)")


# 商品SKU表(最小单元)
class GoodsSKU(BaseModel):

    spu = models.ForeignKey("GoodsSPU", on_delete=models.CASCADE, verbose_name="商品spu id")
    spec = models.ManyToManyField("Spec", verbose_name="规格多对多属性")
    image = models.CharField(max_length=255, verbose_name="图片")
    stock = models.IntegerField(verbose_name="库存")


# 规格表
class GoodsSpec(BaseModel):
    """规格表"""
    name = models.CharField(max_length=20, verbose_name="规格名称")


# 商品封面表
class GoodsCovers(BaseModel):
    """商品封面表"""
    spu = models.ForeignKey('GoodsSPU', on_delete=models.CASCADE, verbose_name="商品外键")
    path = models.CharField(max_length=255, verbose_name="路径")
    sort = models.IntegerField(verbose_name="排序依据")


# 运费模板表
class FareTemplate(BaseModel):
    """运费模板表"""
    name = models.CharField(max_length=50, verbose_name="模板名称")
