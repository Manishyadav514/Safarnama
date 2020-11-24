# Generated by Django 3.1.1 on 2020-11-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='super',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.IntegerField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
                ('delete', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]