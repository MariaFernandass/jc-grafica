# Generated by Django 4.0.5 on 2024-01-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(default='', max_length=50)),
                ('email', models.TextField(default='', max_length=50)),
                ('produto', models.CharField(max_length=250)),
                ('quantidade', models.IntegerField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('preco_unitario', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.TextField(default='Análise', max_length=10)),
            ],
        ),
    ]
