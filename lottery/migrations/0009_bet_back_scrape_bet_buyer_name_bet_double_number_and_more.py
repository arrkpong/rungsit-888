# Generated by Django 5.1.1 on 2024-09-21 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0008_bet'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='back_scrape',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='รูดหลัง'),
        ),
        migrations.AddField(
            model_name='bet',
            name='buyer_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ชื่อผู้ซื้อ'),
        ),
        migrations.AddField(
            model_name='bet',
            name='double_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='เลขเบิ้ล'),
        ),
        migrations.AddField(
            model_name='bet',
            name='front_scrape',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='รูดหน้า'),
        ),
        migrations.AddField(
            model_name='bet',
            name='nineteen_door',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='19 ประตู'),
        ),
        migrations.AddField(
            model_name='bet',
            name='reverse_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='กลับเลข'),
        ),
        migrations.AddField(
            model_name='bet',
            name='running_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='เลขวิ่ง'),
        ),
        migrations.AddField(
            model_name='bet',
            name='six_back',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='6 กลับ'),
        ),
        migrations.AddField(
            model_name='bet',
            name='triple_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='เลขตอง'),
        ),
    ]
