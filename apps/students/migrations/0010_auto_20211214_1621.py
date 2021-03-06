# Generated by Django 3.2.5 on 2021-12-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_alter_studentbulkupload_csv_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=20)),
                ('image_carousel', models.ImageField(blank=True, upload_to='students/carousel_file/')),
            ],
        ),
        migrations.AlterField(
            model_name='vacancy_info',
            name='level',
            field=models.CharField(max_length=1000),
        ),
    ]
