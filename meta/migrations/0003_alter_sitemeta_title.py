# Generated by Django 3.2.12 on 2022-04-14 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0002_alter_sitemeta_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitemeta',
            name='title',
            field=models.CharField(default='Cooler站点', max_length=32, verbose_name='站点标题'),
        ),
    ]
