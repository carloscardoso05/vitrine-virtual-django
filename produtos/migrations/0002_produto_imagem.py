# Generated by Django 4.2 on 2023-04-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default='media/malbec.jpeg', upload_to='media'),
            preserve_default=False,
        ),
    ]
