# Generated by Django 3.2.5 on 2022-04-04 06:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0002_post_abstract'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'demo'},
        ),
    ]
