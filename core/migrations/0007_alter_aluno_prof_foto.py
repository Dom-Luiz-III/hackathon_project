# Generated by Django 4.2.6 on 2023-12-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_aluno_autoavaliacao_avaliacao_avaliacoesaluno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='prof_foto',
            field=models.ImageField(blank=True, default='static/images/sem_foto.jpg', null=True, upload_to='fotos_professores/', verbose_name='Foto'),
        ),
    ]
