# Generated by Django 4.2 on 2023-04-25 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0004_alter_orderrow_service_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrow',
            name='service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='car_app.service'),
        ),
    ]