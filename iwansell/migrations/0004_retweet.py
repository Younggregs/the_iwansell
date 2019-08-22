# Generated by Django 2.1.7 on 2019-07-22 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iwansell', '0003_auto_20190624_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('screen_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('profile_image', models.CharField(default='https://twitter.com/didierdrogba/photo', max_length=200)),
                ('location', models.CharField(default='Lagos, Allen Ave', max_length=100)),
                ('raffle_book', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='iwansell.RaffleBook')),
            ],
        ),
    ]