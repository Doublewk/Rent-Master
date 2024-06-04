from django.db import models
class Rent(models.Model):
    title = models.CharField(max_length=256, verbose_name='标题')
    picture = models.CharField(max_length=256, verbose_name='图片')
    district = models.CharField(max_length=20, verbose_name='区域')
    address = models.CharField(max_length=20, verbose_name='地址')
    area = models.CharField(max_length=20, verbose_name='面积(㎡)')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    types = models.CharField(max_length=20, verbose_name='类型')
    floor = models.CharField(max_length=50, verbose_name='楼层')
    price = models.FloatField(verbose_name='租金(元/月)')
    remark = models.CharField(max_length=150, verbose_name='备注')
    link = models.CharField(max_length=256,verbose_name='详细信息')

    add_date = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    mod_date = models.DateTimeField(auto_now=True, verbose_name="修改日期")

    class Meta:
        db_table = "rent_house"
        verbose_name = '租房'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "{}-{}".format(self.title, self.price)

# class jinjiang(models.Model):
#     title = models.CharField(max_length=256, verbose_name='标题')
#     picture = models.CharField(max_length=256, verbose_name='图片')
#     address = models.CharField(max_length=20, verbose_name='地址')
#     area = models.CharField(max_length=20, verbose_name='面积(㎡)')
#     direction = models.CharField(max_length=20, verbose_name='朝向')
#     types = models.CharField(max_length=20, verbose_name='类型')
#     floor = models.CharField(max_length=50, verbose_name='详细信息')
#     price = models.FloatField(verbose_name='租金(元/月)')
#     remark = models.CharField(max_length=30, verbose_name='备注')
#     link = models.CharField(max_length=256,verbose_name='详细信息')
#
#     class Meta:
#         db_table = "jinjiang"
#
# class qingyang(models.Model):
#     title = models.CharField(max_length=256, verbose_name='标题')
#     picture = models.CharField(max_length=256, verbose_name='图片')
#     address = models.CharField(max_length=20, verbose_name='地址')
#     area = models.CharField(max_length=20, verbose_name='面积(㎡)')
#     direction = models.CharField(max_length=20, verbose_name='朝向')
#     types = models.CharField(max_length=20, verbose_name='类型')
#     floor = models.CharField(max_length=50, verbose_name='详细信息')
#     price = models.FloatField(verbose_name='租金(元/月)')
#     remark = models.CharField(max_length=30, verbose_name='备注')
#     link = models.CharField(max_length=256,verbose_name='详细信息')
#
#     class Meta:
#         db_table = "qingyang"
#
# class wuhou(models.Model):
#     title = models.CharField(max_length=256, verbose_name='标题')
#     picture = models.CharField(max_length=256, verbose_name='图片')
#     address = models.CharField(max_length=20, verbose_name='地址')
#     area = models.CharField(max_length=20, verbose_name='面积(㎡)')
#     direction = models.CharField(max_length=20, verbose_name='朝向')
#     types = models.CharField(max_length=20, verbose_name='类型')
#     floor = models.CharField(max_length=50, verbose_name='详细信息')
#     price = models.FloatField(verbose_name='租金(元/月)')
#     remark = models.CharField(max_length=30, verbose_name='备注')
#     link = models.CharField(max_length=256,verbose_name='详细信息')
#
#     class Meta:
#         db_table = "wuhou"
#
# class gaoxin(models.Model):
#     title = models.CharField(max_length=256, verbose_name='标题')
#     picture = models.CharField(max_length=256, verbose_name='图片')
#     address = models.CharField(max_length=20, verbose_name='地址')
#     area = models.CharField(max_length=20, verbose_name='面积(㎡)')
#     direction = models.CharField(max_length=20, verbose_name='朝向')
#     types = models.CharField(max_length=20, verbose_name='类型')
#     floor = models.CharField(max_length=50, verbose_name='详细信息')
#     price = models.FloatField(verbose_name='租金(元/月)')
#     remark = models.CharField(max_length=30, verbose_name='备注')
#     link = models.CharField(max_length=256,verbose_name='详细信息')
#
#     class Meta:
#         db_table = "gaoxin"
#
# class chenghua(models.Model):
#     title = models.CharField(max_length=256, verbose_name='标题')
#     picture = models.CharField(max_length=256, verbose_name='图片')
#     address = models.CharField(max_length=20, verbose_name='地址')
#     area = models.CharField(max_length=20, verbose_name='面积(㎡)')
#     direction = models.CharField(max_length=20, verbose_name='朝向')
#     types = models.CharField(max_length=20, verbose_name='类型')
#     floor = models.CharField(max_length=50, verbose_name='详细信息')
#     price = models.FloatField(verbose_name='租金(元/月)')
#     remark = models.CharField(max_length=30, verbose_name='备注')
#     link = models.CharField(max_length=256,verbose_name='详细信息')
#
#     class Meta:
#         db_table = "chenghua"
#
# class jinniu(models.Model):
#     title = models.CharField(max_length=256, verbose_name='标题')
#     picture = models.CharField(max_length=256, verbose_name='图片')
#     address = models.CharField(max_length=20, verbose_name='地址')
#     area = models.CharField(max_length=20, verbose_name='面积(㎡)')
#     direction = models.CharField(max_length=20, verbose_name='朝向')
#     types = models.CharField(max_length=20, verbose_name='类型')
#     floor = models.CharField(max_length=50, verbose_name='详细信息')
#     price = models.FloatField(verbose_name='租金(元/月)')
#     remark = models.CharField(max_length=30, verbose_name='备注')
#     link = models.CharField(max_length=256,verbose_name='详细信息')
#
#     class Meta:
#         db_table = "jinniu"
#
# class tianfuxinqu(models.Model):
#     title = models.CharField(max_length=256, verbose_name='标题')
#     picture = models.CharField(max_length=256, verbose_name='图片')
#     address = models.CharField(max_length=20, verbose_name='地址')
#     area = models.CharField(max_length=20, verbose_name='面积(㎡)')
#     direction = models.CharField(max_length=20, verbose_name='朝向')
#     types = models.CharField(max_length=20, verbose_name='类型')
#     floor = models.CharField(max_length=50, verbose_name='详细信息')
#     price = models.FloatField(verbose_name='租金(元/月)')
#     remark = models.CharField(max_length=30, verbose_name='备注')
#     link = models.CharField(max_length=256,verbose_name='详细信息')
#
#     class Meta:
#         db_table = "tianfuxinqu"
#
# class gaoxinxi(models.Model):
#     title = models.CharField(max_length=256, verbose_name='标题')
#     picture = models.CharField(max_length=256, verbose_name='图片')
#     address = models.CharField(max_length=20, verbose_name='地址')
#     area = models.CharField(max_length=20, verbose_name='面积(㎡)')
#     direction = models.CharField(max_length=20, verbose_name='朝向')
#     types = models.CharField(max_length=20, verbose_name='类型')
#     floor = models.CharField(max_length=50, verbose_name='详细信息')
#     price = models.FloatField(verbose_name='租金(元/月)')
#     remark = models.CharField(max_length=30, verbose_name='备注')
#     link = models.CharField(max_length=256,verbose_name='详细信息')
#
#     class Meta:
#         db_table = "gaoxinxi"
#
# class shuangliu(models.Model):
#     title = models.CharField(max_length=256, verbose_name='标题')
#     picture = models.CharField(max_length=256, verbose_name='图片')
#     address = models.CharField(max_length=20, verbose_name='地址')
#     area = models.CharField(max_length=20, verbose_name='面积(㎡)')
#     direction = models.CharField(max_length=20, verbose_name='朝向')
#     types = models.CharField(max_length=20, verbose_name='类型')
#     floor = models.CharField(max_length=50, verbose_name='详细信息')
#     price = models.FloatField(verbose_name='租金(元/月)')
#     remark = models.CharField(max_length=30, verbose_name='备注')
#     link = models.CharField(max_length=256,verbose_name='详细信息')
#
#     class Meta:
#         db_table = "shuangliu"
#
# class wenjiang(models.Model):
#     title = models.CharField(max_length=256, verbose_name='标题')
#     picture = models.CharField(max_length=256, verbose_name='图片')
#     address = models.CharField(max_length=20, verbose_name='地址')
#     area = models.CharField(max_length=20, verbose_name='面积(㎡)')
#     direction = models.CharField(max_length=20, verbose_name='朝向')
#     types = models.CharField(max_length=20, verbose_name='类型')
#     floor = models.CharField(max_length=50, verbose_name='详细信息')
#     price = models.FloatField(verbose_name='租金(元/月)')
#     remark = models.CharField(max_length=30, verbose_name='备注')
#     link = models.CharField(max_length=256,verbose_name='详细信息')
#
#     class Meta:
#         db_table = "wenjiang"
#
# class pidu(models.Model):
#     title = models.CharField(max_length=256, verbose_name='标题')
#     picture = models.CharField(max_length=256, verbose_name='图片')
#     address = models.CharField(max_length=20, verbose_name='地址')
#     area = models.CharField(max_length=20, verbose_name='面积(㎡)')
#     direction = models.CharField(max_length=20, verbose_name='朝向')
#     types = models.CharField(max_length=20, verbose_name='类型')
#     floor = models.CharField(max_length=50, verbose_name='详细信息')
#     price = models.FloatField(verbose_name='租金(元/月)')
#     remark = models.CharField(max_length=30, verbose_name='备注')
#     link = models.CharField(max_length=256,verbose_name='详细信息')
#
#     class Meta:
#         db_table = "pidu"