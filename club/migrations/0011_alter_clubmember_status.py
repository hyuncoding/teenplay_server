# Generated by Django 5.0.2 on 2024-02-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0010_alter_clubmember_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubmember',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '가입중'), (0, '탈퇴'), (-1, '가입대기')], default=-1),
        ),
    ]
