from django.contrib import admin
from .models import (Usuario, Aluno, AutoAvaliacao, Professor, Curso, 
                     Disciplina, TurmaDisciplina, Avaliacao, Turma, Criterio, AvaliacoesAluno)

# Utilize os decorators para registrar os modelos

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['user_nome', 'user_prof_id', 'user_alu_id']


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['alu_nome', 'alu_email', 'alu_num_matricula']
    search_fields = ['alu_nome', 'alu_email']
    list_filter = ('alu_nome',)


@admin.register(AutoAvaliacao)
class AutoAvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['auto_nome', 'auto_peso', 'auto_id_alu']


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['prof_nome', 'prof_sobrenome', 'prof_telefone']
    search_fields = ['prof_nome', 'prof_sobrenome']


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['curso_nome']


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['disc_nome', 'curso_id']


@admin.register(TurmaDisciplina)
class TurmaDisciplinaAdmin(admin.ModelAdmin):
    list_display = ['disc_id', 'prof_id']


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['aval_nome', 'aval_valortotal', 'aval_data']
    list_filter = ('aval_data',)


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['tur_nome', 'tur_sala', 'tur_turno']


@admin.register(Criterio)
class CriterioAdmin(admin.ModelAdmin):
    list_display = ['crit_nome', 'crit_peso', 'crit_aval_id']


@admin.register(AvaliacoesAluno)
class AvaliacoesAlunoAdmin(admin.ModelAdmin):
    list_display = ['aval_alun_crit_id', 'aval_alun_nota']