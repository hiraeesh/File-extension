# Generated by Django 4.1.4 on 2022-12-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_modelwithfilefield3_fileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelwithfilefield3',
            name='fileimg',
            field=models.FileField(upload_to='xyz'),
        ),
    ]
