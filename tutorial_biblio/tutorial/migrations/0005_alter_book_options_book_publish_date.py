# Generated by Django 4.2.4 on 2023-08-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-price'], 'verbose_name_plural': 'Libros'},
        ),
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
