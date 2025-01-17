# Generated by Django 5.0.7 on 2024-07-18 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zootovar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='name_en',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='carrier_en',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='carrier_ru',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='filler_en',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='filler_ru',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
    ]
