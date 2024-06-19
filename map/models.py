from django.db import models

from orders.models import Order


class Map(models.Model):
    start_longitude = models.FloatField()
    start_latitude = models.FloatField()
    end_longitude = models.FloatField()
    end_latitude = models.FloatField()
    order = models.ForeignKey(Order, related_name='map', on_delete=models.CASCADE)

    def __str__(self):
        return f"Map for Order {self.order.id}"

    class Meta:
        db_table = "map"

    # class Map(Base):
    #     __tablename__ = 'map'
    # id = Column(Integer, primary_key=True)
    # start_longitude = Column(Float)
    # start_latitude = Column(Float)
    # end_longitude = Column(Float)
    # end_latitude = Column(Float)
    # order_id = Column(Integer, ForeignKey('orders.id'))
    # orders = relationship("Order", back_populates="map")


    # class Map(models.Model):
    #     start_longitude = models.FloatField()
    # start_latitude = models.FloatField()
    # end_longitude = models.FloatField()
    # end_latitude = models.FloatField()
    # order = models.ForeignKey(Order, related_name='map', on_delete=models.CASCADE)
    #
    # def __str__(self):
    #     return f"Map for Order {self.order.order_number}"