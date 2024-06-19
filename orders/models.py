from django.db import models

from couriers.models import Courier
from shop.models import Product
from users.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusEnum(models.TextChoices):
    NOT_ACCEPTED = 'not_accepted', _('Not Accepted')
    ACCEPTED = 'accepted', _('Accepted')
    CANCELED = 'canceled', _('Canceled')
    COMPLETED = 'completed', _('Completed')


class Order(models.Model):
    #first_name = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)
    #email = models.EmailField()
    #address = models.CharField(max_length=250)
    #postal_code = models.CharField(max_length=20)
    #city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)
    total_cost = models.FloatField(default=0.0)
    status = models.CharField(
        max_length=20,
        choices=StatusEnum.choices,
        default=StatusEnum.NOT_ACCEPTED
    )
    #paid = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', )
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name='courier', default=1)

    class Meta:
        ordering = ['-created']
        indexes = [
        models.Index(fields=['-created']),
        ]
        db_table = "orders"

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        db_table = "orderItem"



# class Order(Base):
#     __tablename__ = 'orders'
#     id = Column(Integer, primary_key=True)
#     order_number = Column(String)
#     address = Column(String)
#     total_amount = Column(Float)
#     status = Column(EnumColumn(StatusEnum), default=StatusEnum.NOT_ACCEPTED)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship("User", back_populates="orders")
#     map = relationship("Map", back_populates="orders")
#     created_at = Column(DateTime, default=datetime.now)

# class StatusEnum(models.TextChoices):
#     NOT_ACCEPTED = 'not_accepted', _('Not Accepted')
#     ACCEPTED = 'accepted', _('Accepted')
#     CANCELED = 'canceled', _('Canceled')
#     COMPLETED = 'completed', _('Completed')
#
#
# class Order(models.Model):
#     order_number = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     total_amount = models.FloatField()
#     status = models.CharField(
#         max_length=20,
#         choices=StatusEnum.choices,
#         default=StatusEnum.NOT_ACCEPTED
#     )
#     user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.order_number