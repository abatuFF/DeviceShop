# Generated by Django 4.2.7 on 2024-01-31 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mice',
            options={'verbose_name': 'Mice', 'verbose_name_plural': 'Mice'},
        ),
        migrations.AddField(
            model_name='mice',
            name='image',
            field=models.ImageField(default='products/img.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='mice',
            name='description',
            field=models.TextField(max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='mice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='mice',
            name='tittle',
            field=models.CharField(max_length=50, verbose_name='Заголовок'),
        ),
    ]
