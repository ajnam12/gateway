# Generated by Django 3.1.7 on 2021-03-29 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210329_1531'),
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExamplePlugin',
        ),
        migrations.CreateModel(
            name='Randomness',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.plugin',),
        ),
    ]