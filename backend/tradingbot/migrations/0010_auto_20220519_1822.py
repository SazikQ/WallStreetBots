# Generated by Django 3.2.8 on 2022-05-19 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbot', '0009_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='optimization_strategy',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='rebalancing_strategy',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='strategy',
            field=models.CharField(choices=[('manual', 'Manual portfolio management'), ('hmm_naive_even_split', 'HMM model prediction + Even split portfolio'), ('ma_sharp_ratio_monte_carlo', 'Moving average + Sharpe ratio Monte Carlo simulation'), ('hmm_sharp_ratio_monte_carlo', 'HMM model prediction + Sharpe ratio Monte Carlo simulation')], default='manual', help_text='Portfolio Rebalancing Strategy', max_length=50),
        ),
    ]