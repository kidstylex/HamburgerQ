# Generated by Django 2.2.5 on 2019-10-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0005_auto_20191029_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitingroom',
            name='room_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='waitingroom',
            unique_together=set(),
        ),
    ]
