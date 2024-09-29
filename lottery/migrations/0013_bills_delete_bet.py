# Generated by Django 5.1.1 on 2024-09-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0012_remove_bet_bet_type_remove_bet_position_bet_bottom_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100, verbose_name='สินค้า')),
                ('date', models.DateField(verbose_name='ประจำวันที่')),
                ('time', models.TimeField(verbose_name='เวลา')),
                ('status', models.CharField(max_length=20, verbose_name='สถานะ')),
                ('total', models.IntegerField(verbose_name='ยอดรวม')),
                ('correct', models.IntegerField(default=0, verbose_name='ถูก')),
                ('remaining', models.IntegerField(default=0, verbose_name='คงเหลือ')),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='วันที่สร้าง')),
            ],
            options={
                'verbose_name': 'บิล',
                'verbose_name_plural': 'บิล',
            },
        ),
        migrations.DeleteModel(
            name='Bet',
        ),
    ]
