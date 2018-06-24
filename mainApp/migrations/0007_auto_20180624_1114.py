# Generated by Django 2.0.6 on 2018-06-24 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_auto_20180624_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='choose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Distributor'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='timeleft',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
