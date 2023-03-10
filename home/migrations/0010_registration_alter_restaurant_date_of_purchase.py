# Generated by Django 4.0.4 on 2023-02-20 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_restaurant_new_employee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='Date_of_Purchase',
            field=models.DateField(null=True),
        ),
    ]
