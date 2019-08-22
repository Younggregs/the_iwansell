# Generated by Django 2.1.7 on 2019-08-14 01:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('iwansell', '0004_retweet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.TextField()),
                ('product_image', models.FileField(upload_to='')),
                ('budget', models.CharField(max_length=100)),
                ('success', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iwansell.Account')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iwansell.Campus')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iwansell.Category')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.RemoveField(
            model_name='rafflebook',
            name='traffle_client',
        ),
        migrations.RemoveField(
            model_name='retweet',
            name='raffle_book',
        ),
        migrations.RemoveField(
            model_name='traffle',
            name='raffle_book',
        ),
        migrations.RemoveField(
            model_name='traffle',
            name='traffle_client',
        ),
        migrations.RemoveField(
            model_name='winner',
            name='raffle_book',
        ),
        migrations.RemoveField(
            model_name='winner',
            name='traffle',
        ),
        migrations.DeleteModel(
            name='RaffleBook',
        ),
        migrations.DeleteModel(
            name='Retweet',
        ),
        migrations.DeleteModel(
            name='Traffle',
        ),
        migrations.DeleteModel(
            name='TraffleClient',
        ),
        migrations.DeleteModel(
            name='Winner',
        ),
    ]