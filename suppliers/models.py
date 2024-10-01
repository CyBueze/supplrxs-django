from django.db import models

#from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=15)
    states = models.ManyToManyField(State)

    def __str__(self):
        return self.name

class Drug(models.Model):
    name = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='drugs')
    search_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
