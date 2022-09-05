# Generated by Django 3.2.8 on 2022-01-11 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbot', '0005_auto_20220110_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='optimization_strategy',
            field=models.CharField(choices=[('none', 'None'), ('ma_sharp_ratio', 'Sharp ratio based on moving average')], default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='rebalancing_strategy',
            field=models.CharField(choices=[('manual', 'Manual portfolio management'), ('monte_carlo', 'Monte carlo portfolio rebalancing')], default='manual', help_text='Portfolio Rebalancing Strategy', max_length=50),
        ),
    ]
