# Generated by Django 4.2 on 2023-04-08 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_remove_produto_em_promocao_remove_produto_promocao'),
        ('promocoes', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Promocao',
        ),
    ]
