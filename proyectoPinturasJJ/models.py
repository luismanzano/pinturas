from django.db import models as models


class Material(models.Model):
    name = models.CharField(max_length=200)
    cost_sqm = models.FloatField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    exists = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

class Budget(models.Model):
    client_name = models.CharField(max_length=200)
    sqm = models.FloatField(max_length=200)
    total_cost = models.FloatField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    exists = models.BooleanField(default=True)

    def __str__(self):
        return str(self.client_name)

class MaterialBudget(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    exists = models.BooleanField()

    def __str__(self):
        return str(self.short_url)
