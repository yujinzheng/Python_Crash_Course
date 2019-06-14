from django.db import models

class Pizza(models.Model):
    """披萨类"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回披萨的名字"""
        return self.name

class Topping(models.Model):
    """Topping类"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topp = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回披萨的配料"""
        return self.topp