# Generated by Django 5.1.1 on 2024-09-21 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0007_delete_bet_alter_lottery_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, verbose_name='เลขที่เดิมพัน')),
                ('top', models.CharField(blank=True, max_length=10, null=True, verbose_name='บน')),
                ('bottom', models.CharField(blank=True, max_length=10, null=True, verbose_name='ล่าง')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='วันที่เดิมพัน')),
                ('lottery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lottery.lottery', verbose_name='หวยที่เดิมพัน')),
            ],
            options={
                'verbose_name': 'โพยเดิมพัน',
                'verbose_name_plural': 'โพยเดิมพัน',
            },
        ),
    ]
