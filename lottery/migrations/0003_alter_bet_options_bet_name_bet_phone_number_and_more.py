# Generated by Django 5.1.1 on 2024-09-15 10:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0002_bet_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bet',
            options={'verbose_name': 'การแทงหวย', 'verbose_name_plural': 'การแทงหวย'},
        ),
        migrations.AddField(
            model_name='bet',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ชื่อของผู้แทง'),
        ),
        migrations.AddField(
            model_name='bet',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='เบอร์โทรศัพท์ไม่ถูกต้อง', regex='^\\+?1?\\d{9,15}$')], verbose_name='เบอร์โทรศัพท์ของผู้แทง'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='bet_number',
            field=models.CharField(max_length=10, verbose_name='หมายเลขที่แทง'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='bet_type',
            field=models.CharField(choices=[('two_digit_top', 'Two-Digit Top'), ('two_digit_bottom', 'Two-Digit Bottom'), ('three_digit_top', 'Three-Digit Top'), ('three_digit_mix', 'Three-Digit Mix'), ('top_run', 'Top Run'), ('bottom_run', 'Bottom Run')], max_length=20, verbose_name='ประเภทการแทง'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='country',
            field=models.CharField(choices=[('thailand', 'Thailand'), ('usa', 'USA'), ('uk', 'UK'), ('vietnam', 'Vietnam'), ('laos', 'Laos')], default='thailand', max_length=20, verbose_name='ประเทศ'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='placed_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='เวลาที่แทง'),
        ),
    ]
