from django.db import models


class Mice(models.Model):
    tittle = models.CharField( max_length=50, verbose_name="Заголовок")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(max_length=300,verbose_name="Описание")
    image = models.ImageField(upload_to='images/', blank=False, verbose_name="Изображение")

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Mice'
        verbose_name_plural = 'Mice'