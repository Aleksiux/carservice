# Generated by Django 4.2 on 2023-04-25 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0003_alter_car_car_model_id_alter_order_car_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrow',
            name='service_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_app.service'),
        ),
    ]
