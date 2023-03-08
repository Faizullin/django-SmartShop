from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeleteModel(models.Model):

    deleted_at = models.DateTimeField(null=True, default=None)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True



class Role(SoftDeleteModel):
    name = models.CharField(max_length=100)

class ShopData(SoftDeleteModel):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    open = models.BooleanField(default = False)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

class Shop(SoftDeleteModel):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.ForeignKey(ShopData, on_delete=models.CASCADE)



class GoodType(SoftDeleteModel):
    name = models.CharField(max_length=100)

class Good(SoftDeleteModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.ForeignKey(GoodType, on_delete=models.CASCADE)

class Purchase(SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    goods = models.ForeignKey(Good, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


def get_user_stories(user_id):
    user = User.objects.get(id=user_id)
    purchases = Purchase.objects.filter(user=user).order_by('-id')
    shop_ids = purchases.values_list('shop_id', flat=True).distinct()
    shops = Shop.objects.filter(id__in=shop_ids)

    # Return the purchases and shops as a dictionary
    return {'purchases': purchases, 'shops': shops}