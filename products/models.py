from django.db import models


class Mice(models.Model):
    tittle = models.CharField('Название', max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Mice'
        verbose_name_plural = 'Mice'