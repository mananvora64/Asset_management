# Generated by Django 4.0.4 on 2023-02-17 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_restaurant_alter_entry_dropdown'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='New_Employee',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Date_of_Purchase',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='entry',
            name='dropdown',
            field=models.CharField(choices=[('Laptop', 'Laptop'), ('Mouse', 'Mouse'), ('Desktop', 'Desktop'), ('Printer', 'Printer')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='No_of_Dishes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='No_of_Fans',
            field=models.IntegerField(blank=True),
        ),
    ]
