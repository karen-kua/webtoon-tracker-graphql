# Generated by Django 3.2.4 on 2021-06-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayofrelease',
            name='webtoons',
            field=models.ManyToManyField(related_name='releases', to='api.Webtoon'),
        ),
    ]