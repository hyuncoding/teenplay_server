# Generated by Django 5.0.2 on 2024-02-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitymember',
            name='status',
            field=models.BooleanField(choices=[(1, '참가중'), (-1, '참가대기'), (0, '취소')], default=0),
        ),
    ]
