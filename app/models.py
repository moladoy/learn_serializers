from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=125)
    text = models.TextField()
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    user = models.ForeignKey('auth.User', models.CASCADE, related_name='user')


