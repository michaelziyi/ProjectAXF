# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-06 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_foodtypes_goods_mainshow_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('isselect', models.BooleanField(default=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Goods')),
            ],
            options={
                'db_table': 'axf_cart',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=80, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('addr', models.CharField(max_length=256)),
                ('img', models.CharField(max_length=100)),
                ('rank', models.IntegerField(default=1)),
                ('token', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
        migrations.AlterField(
            model_name='mustbuy',
            name='trackid',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='nav',
            name='trackid',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='shop',
            name='trackid',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='wheel',
            name='trackid',
            field=models.CharField(max_length=10),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.User'),
        ),
    ]
