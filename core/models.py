from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class Usuario(models.Model):
    user_nome = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario_nome')
    user_senha = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario_senha')
    user_prof_id = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True, blank=True)
    user_alu_id = models.ForeignKey('Aluno', on_delete=models.SET_NULL, null=True, blank=True)

class Aluno(models.Model):
    alu_nome = models.CharField(max_length=255)
    alu_email = models.EmailField(unique=True)
    alu_senha = models.IntegerField()  
    prof_foto = models.ImageField(upload_to='fotos_professores/', default='static/images/sem_foto.jpg')
    alu_num_matricula = models.IntegerField()
    
    def __str__(self):
        return self.alu_nome
    
    # Se a imagem existir, ela será exibida. Caso contrário, a imagem padrão sem_foto.jpg será exibida:
    def foto_tag(self):
        if self.foto:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.foto.url))
        else:
            default_image_path = 'core/images/sem_foto.jpg'
            return mark_safe('<img src="{}" width="50" height="50" />'.format(default_image_path))

    foto_tag.short_description = 'Imagem'

    # Verifica se a foto está em branco e, se estiver, atribui o caminho da imagem padrão
    def save(self, *args, **kwargs):
        if not self.foto:
            self.foto = 'alunos/sem_foto.jpg'

        super(Aluno, self).save(*args, **kwargs)

class AutoAvaliacao(models.Model):
    auto_nome = models.CharField(max_length=255)
    auto_peso = models.FloatField()
    auto_id_alu = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return self.auto_nome

class Professor(models.Model):
    prof_nome = models.CharField(max_length=255)
    prof_sobrenome = models.CharField(max_length=255)
    prof_foto = models.ImageField(upload_to='fotos_professores/', default='static/images/sem_foto.jpg')
    prof_telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.prof_nome
    
     # Se a imagem existir, ela será exibida. Caso contrário, a imagem padrão sem_foto.jpg será exibida:
    def foto_tag(self):
        if self.foto:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.foto.url))
        else:
            default_image_path = 'core/images/sem_foto.jpg'
            return mark_safe('<img src="{}" width="50" height="50" />'.format(default_image_path))

    foto_tag.short_description = 'Imagem'

    # Verifica se a foto está em branco e, se estiver, atribui o caminho da imagem padrão
    def save(self, *args, **kwargs):
        if not self.foto:
            self.foto = 'professores/sem_foto.jpg'

        super(Professor, self).save(*args, **kwargs)

class Curso(models.Model):
    curso_nome = models.CharField(max_length=255)

    def __str__(self):
        return self.curso_nome

class Disciplina(models.Model):
    disc_nome = models.CharField(max_length=255)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.disc_nome

class TurmaDisciplina(models.Model):
    disc_id = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    prof_id = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.alu_nome

class Avaliacao(models.Model):
    aval_nome = models.CharField(max_length=255)
    aval_valortotal = models.FloatField()
    aval_disc_id = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    aval_prof_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    aval_tur_id = models.ForeignKey('Turma', on_delete=models.CASCADE) # 'Turma' está entre aspas pois a classe Turma ainda não foi definida
    aval_data = models.DateTimeField()

    def __str__(self):
        return self.aval_nome

class Turma(models.Model):
    tur_nome = models.CharField(max_length=255)
    tur_sala = models.IntegerField()
    tur_turno = models.CharField('Turno', max_length=20, choices=[
        ('matutino', 'Matutino'), ('vespertino', 'Vespertino'), ('noturno', 'Noturno')])

    def __str__(self):
        return self.tur_nome

class Criterio(models.Model):
    crit_nome = models.CharField(max_length=255)
    crit_descricao = models.CharField(max_length=1024)
    crit_peso = models.FloatField()
    crit_aval_id = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.crit_nome

class AvaliacoesAluno(models.Model):
    aval_alun_crit_id = models.ForeignKey(Criterio, on_delete=models.CASCADE)
    aval_alun_nota = models.FloatField()

    def __str__(self):
        return self.aval_alun_crit_id