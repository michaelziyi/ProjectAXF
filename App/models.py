from django.db import models

# Create your models here.
class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'


class Nav(Base):
    class Meta:
        db_table = 'axf_nav'

class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'