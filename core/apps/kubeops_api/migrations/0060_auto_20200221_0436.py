# Generated by Django 2.2.10 on 2020-02-21 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0059_auto_20200221_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clusterhealthhistory',
            name='date_type',
            field=models.CharField(choices=[('DAY', 'DAY'), ('HOUR', 'HOUR')], default='HOUR', max_length=255),
        ),
    ]