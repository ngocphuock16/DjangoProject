from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Manufactory(models.Model):
    manuname = models.CharField(max_length=100, null=False)

    def __str__(self):
        m = str(self.manuname)
        return m


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    manufactory = models.ForeignKey(Manufactory, null=False, verbose_name=_('Manufactory'), on_delete=models.CASCADE)
    description = models.TextField(null=False)
    image = models.ImageField(null=True)
    count = models.IntegerField(default=0, null=False)
    price = models.IntegerField(default=0, null=False)

    # in noi dung
    def __str__(self):
        a = "Tên sản phẩm : " + str(self.name) + ", có nhà sản xuất là: " + str(
            self.manufactory) + ", Số lượng: " + str(self.count) + ", có giá: " + str(self.price)
        return a
