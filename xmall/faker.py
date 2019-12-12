from random import randint

from faker import Faker

from goods.models import Good


def goods(count=100):
    fake = Faker(locale='zh-CN')
    for i in range(count):
        Good.objects.create(
            salePrice=randint(1, 9999),
            productName=fake.name(),
            subTitle=fake.words()
        )
