# Generated by Django 2.1.7 on 2019-03-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iwansell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.FileField(default='anon.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.FileField(default='anon.png', upload_to=''),
        ),
    ]