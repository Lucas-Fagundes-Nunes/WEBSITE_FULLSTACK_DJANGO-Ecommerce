# Generated by Django 4.1.3 on 2022-12-03 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetoecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='id_produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projetoecommerce.produto'),
        ),
    ]