# Generated by Django 4.0.4 on 2023-02-16 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_entry_dropdown'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('New_Employee', models.CharField(max_length=50)),
                ('No_of_Dishes', models.IntegerField()),
                ('No_of_Spoon', models.IntegerField()),
                ('Water_bottles', models.IntegerField()),
                ('No_of_Fans', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='entry',
            name='dropdown',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
