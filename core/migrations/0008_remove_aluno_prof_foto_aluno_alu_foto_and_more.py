# Generated by Django 4.2.6 on 2023-12-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_aluno_prof_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='prof_foto',
        ),
        migrations.AddField(
            model_name='aluno',
            name='alu_foto',
            field=models.ImageField(blank=True, default='static/images/sem_foto.jpg', null=True, upload_to='media/alunos', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='prof_foto',
            field=models.ImageField(default='static/images/sem_foto.jpg', upload_to='media/professores'),
        ),
    ]
