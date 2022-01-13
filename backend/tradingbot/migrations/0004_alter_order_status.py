# Generated by Django 3.2.8 on 2022-01-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbot', '0003_auto_20220108_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('A', 'Accepted'), ('F', 'Filled'), ('C', 'Cancelled')], help_text='order status', max_length=1),
        ),
    ]