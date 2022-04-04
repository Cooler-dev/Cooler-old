# Generated by Django 3.2.5 on 2022-04-04 01:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sitemeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Cooler站点', max_length=10, verbose_name='站点标题')),
                ('author', models.CharField(max_length=10, verbose_name='作者名称')),
            ],
        ),
    ]
