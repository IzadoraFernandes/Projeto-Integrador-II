# Generated by Django 4.2 on 2023-05-23 11:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0006_livros_quantidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='descricao',
            new_name='descricao_categoria',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='nome',
            new_name='nome_categoria',
        ),
        migrations.RenameField(
            model_name='livros',
            old_name='nome',
            new_name='editora',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='data_devolucao',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='data_emprestimo',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='nome_emprestado',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='tempo_duracao',
        ),
        migrations.AddField(
            model_name='categoria',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='livro.categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='nome_emprestado',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='tempo_duracao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livros',
            name='data_lancamento',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='livros',
            name='descricao_livro',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livros',
            name='nome_livro',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
