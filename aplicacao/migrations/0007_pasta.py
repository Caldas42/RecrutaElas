# Generated by Django 5.1.1 on 2024-11-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0006_cadastros_skillcostura_cadastros_skillgerenciamento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cadastros', models.ManyToManyField(related_name='pastas', to='aplicacao.cadastros')),
            ],
        ),
    ]
