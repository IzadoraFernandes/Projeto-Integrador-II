# Generated by Django 4.2 on 2023-05-25 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0009_emprestimo_avaliacao_emprestimo_livro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='data_emprestimo',
        ),
        migrations.RemoveField(
            model_name='emprestimo',
            name='nome_emprestado',
        ),
    ]
