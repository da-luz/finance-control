from datetime import date
from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=50)
    flow = models.CharField(
        max_length=3,
        choices=[
            ('in', 'income'),
            ('out', 'expense'),
        ]
    )

    created_by = models.ForeignKey(get_user_model(), models.CASCADE)
    created_at = models.DateField(default=date.today)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Categories"


class Transaction(models.Model):
    amount = models.FloatField()
    description = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, models.CASCADE)

    created_by = models.ForeignKey(get_user_model(), models.CASCADE)
    created_at = models.DateField(default=date.today)

    class Meta:
        ordering=["-created_at"]
