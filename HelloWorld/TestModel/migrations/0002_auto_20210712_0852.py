# Generated by Django 3.2.5 on 2021-07-12 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]