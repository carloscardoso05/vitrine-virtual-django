# Generated by Django 4.2 on 2023-04-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_produto_promocao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
