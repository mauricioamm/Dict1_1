import os
# coloquei import os pra usar esse recurso de text-to-speech
# pip install django-next-prev
from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.db import connection
from next_prev import next_in_order, prev_in_order
from random import randint
from .models import dictclass
from .forms import DictForm, DictForm2
# from .forms import DictForm, TipoAudio
# importei esse gtts agora... É só digitar e ele mesmo vai pedir pra instalar
from gtts import gTTS
import sqlite3
from django.db.models import Count
import pyglet
from time import sleep
from django.http import HttpResponse
from django.db import connection
import datetime
import csv
from django.contrib.auth.views import LogoutView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

def criar(request):
    data = {}
    form = DictForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, "dictapp/Entrada_iniciar.html")
    data['form'] = form
    # return render(request, 'dictapp/form2.html', data)
    return render(request, 'dictapp/principal_vazio.html', data)


def Entrada(request):
    return render(request, "dictapp/Entrada.html")


def Entrada_login(request):

    usuario = request.user
    if request.POST.get('Visitante'):
        request.user = User.objects.get(username='visitante')
        usuario = User(username='visitante')
        u = User.objects.get(username='visitante')
        u.save()

    context = {
        "user": usuario
    }

    return render(request, "dictapp/Entrada_login.html", context)


# @login_required
def Entrada_Iniciar(request):
    # user = request.user
    # banquinho = str(user)
    ##lista = EprogModel.objetos.using(banquinho).all()

    # user = request.user
    # banquinho = str(user)

    # mudar sessao - inicio
    # objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
    # objetinho_sessao = dictclass.objetos.get(pk=1)
    # objeto_procedimento = ProcedimentoModel.objetos.using(banquinho).get(pk=1)
    # SessaoAntiga = objeto_procedimento.SessaoAtual
    # n_SessaoAntiga = int(SessaoAntiga)
    # n_SessaoAtual = n_SessaoAntiga + 1
    # objeto_procedimento.SessaoAtual = str(n_SessaoAtual)
    # objeto_procedimento.save()
    # objetinho_sessao.Sessao = objeto_procedimento.SessaoAtual
    # objetinho_sessao.save()
    # mudar sessao - fim

    if request.POST.get('comecar_sessao'):
        return redirect('url_sessao_testar', pk=n_rand)

    if request.POST.get('comecar_sessao_ale'):
        banquinho = 'db_ale'
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro= obj_primeiro.id
        return redirect('url_principal_ale', pk=n_primeiro)

    if request.POST.get('comecar_sessao_ing'):
        banquinho = 'db_ing'
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro= obj_primeiro.id
        return redirect('url_principal_ing', pk=n_primeiro)


    return render(request, "dictapp/Entrada_iniciar.html")

"""
def editar(request, pk):
    data = {}
    banquinho = 'db_ale'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    data['form'] = form
    data['objetinho'] = objetinho
    if request.POST.get('Salvar'):
        if form.is_valid():
            form.save()
        return redirect('url_Entrada_Iniciar')
    if request.POST.get('voltar'):
        return redirect('url_Entrada_Iniciar')

    return render(request, 'dictapp/Editar_Dict.html', data)
"""
def editar_ale (request, pk):
    data = {}
    banquinho = 'db_ale'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    data['form'] = form
    data['objetinho'] = objetinho
    if request.POST.get('Salvar'):
        if form.is_valid():
            form.save()
        return redirect('url_Entrada_Iniciar')
    if request.POST.get('voltar'):
        return redirect('url_Entrada_Iniciar')

    return render(request, 'dictapp/Editar_ale.html', data)

def editar_ing (request, pk):
    data = {}
    banquinho = 'db_ing'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    data['form'] = form
    data['objetinho'] = objetinho
    if request.POST.get('Salvar'):
        if form.is_valid():
            form.save()
        return redirect('url_Entrada_Iniciar')
    if request.POST.get('voltar'):
        return redirect('url_Entrada_Iniciar')

    return render(request, 'dictapp/Editar_ing.html', data)

"""
def delete(request, pk):
    lista = dictclass.objetos.get(pk=pk)
    lista.delete()
    return redirect('url_Entrada_Iniciar')
"""

def sessao_testar_port_ale(request, pk):
    data = {}
    banquinho = 'db_ale'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)

    if request.POST.get('Resposta'):
        form2 = DictForm2(request.POST or None, instance=objetinho)
        if form2.is_valid():
            form2.save()
        return redirect('url_principal_ale', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_port_ale.html", context)

def sessao_testar_port_ing(request, pk):
    data = {}
    banquinho = 'db_ing'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)

    if request.POST.get('Resposta'):
        form2 = DictForm2(request.POST or None, instance=objetinho)
        if form2.is_valid():
            form2.save()
        return redirect('url_principal_ing', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_port_ing.html", context)


def sessao_testar_figura_ale(request, pk):
    data = {}
    banquinho = 'db_ale'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)

    if request.POST.get('Resposta'):
        form2 = DictForm2(request.POST or None, instance=objetinho)
        if form2.is_valid():
            form2.save()
        return redirect('url_principal_ale', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_figura_ale.html", context)

def sessao_testar_figura_ing(request, pk):
    data = {}
    banquinho = 'db_ing'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)

    if request.POST.get('Resposta'):
        form2 = DictForm2(request.POST or None, instance=objetinho)
        if form2.is_valid():
            form2.save()
        return redirect('url_principal_ing', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_figura_ing.html", context)

def sessao_testar_audio_ale(request, pk):
    data = {}
    banquinho = 'db_ale'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)

    campo = 'id'
    obj = dictclass.objetos.using(banquinho).get(pk=pk)
    valor_campo = getattr(obj, campo)
    n = valor_campo
    frasex = obj.frase
    tts = gTTS(text=frasex, lang='de')
    tts.save('ale.mp3')
    os.system("ale.mp3")

    if request.POST.get('Resposta'):
        form2 = DictForm2(request.POST or None, instance=objetinho)
        if form2.is_valid():
            form2.save()
        return redirect('url_principal_ale', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_audio_ale.html", context)

def sessao_testar_audio_ing(request, pk):
    data = {}
    banquinho = 'db_ing'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)

    campo = 'id'
    obj = dictclass.objetos.using(banquinho).get(pk=pk)
    valor_campo = getattr(obj, campo)
    n = valor_campo
    frasex = obj.frase
    tts = gTTS(text=frasex, lang='en')
    tts.save('ing.mp3')
    os.system("ing.mp3")


    if request.POST.get('Resposta'):
        form2 = DictForm2(request.POST or None, instance=objetinho)
        if form2.is_valid():
            form2.save()
        return redirect('url_principal_ing', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_audio_ing.html", context)

def sessao_testar_ale(request, pk):
    data = {}
    banquinho = 'db_ale'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)

    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)
    if request.POST.get('Resposta'):
        form2 = DictForm2(request.POST or None, instance=objetinho)
        if form2.is_valid():
            form2.save()
        return redirect('url_principal_ale', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_ale.html", context)

def sessao_testar_ing(request, pk):
    data = {}
    banquinho = 'db_ing'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    form2 = DictForm2(request.POST or None, instance=objetinho)
    if request.POST.get('Resposta'):
        form2 = DictForm2(request.POST or None, instance=objetinho)
        if form2.is_valid():
            form2.save()
        return redirect('url_principal_ing', pk=pk)

    if request.POST.get('Sair'):
        return redirect('url_Entrada_Iniciar')

    context = {
        "form": form,
        "form2": form2,
        "objetinho": objetinho,
    }
    return render(request, "dictapp/sessao_testar_ing.html", context)

def principal_ale(request, pk):
    data = {}
    banquinho = 'db_ale'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    objsuaresp = dictclass.objetos.using(banquinho).get(pk=pk)
    objsuaresp.suaresposta1 = ''
    x = objsuaresp.suaresposta1
    objsuaresp.save()


    if request.POST.get('Sair'):
        return redirect('url_entrada')

    if request.POST.get('Novo'):
        objeto_ultimo = dictclass.objetos.using(banquinho).last()
        n_saida_ultimo = objeto_ultimo.id
        pk_next = n_saida_ultimo + 1
        objeto_novo = dictclass.objetos.using(banquinho).last()
        objeto_novo.pk = None
        objeto_novo.pk = pk_next
        objeto_novo.id = pk_next
        objeto_novo.Ordem = pk_next
        objeto_novo.palavra = ''
        objeto_novo.palavratrad = ''
        objeto_novo.frase = ''
        objeto_novo.frasetrad = ''
        objeto_novo.frase2 = ''
        objeto_novo.frasetrad2 = ''
        objeto_novo.frase3 = ''
        objeto_novo.frasetrad3 = ''
        objeto_novo.figura1 = '/static/dictapp/img/vazio.jpg'
        objeto_novo.som1 = '/static/dictapp/sons/vazio.mp3'
        objeto_novo.save()
        return redirect('url_editar_ale', pk=pk_next)

    if request.POST.get('Editar'):
        data = {}
        banquinho = 'db_ale'
        objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
        form = DictForm(request.POST or None, instance=objetinho)
        return redirect('url_editar_ale', pk=pk)

    if request.POST.get('Excluir'):
        objetinho.delete()
        c = sqlite3.connect('db_ale.sqlite3')

        # 1- CRIAR TABELA CLONADA table tableclone sem ID
        c.execute('CREATE TABLE tableclone (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
                  'palavra TEXT, palavratrad TEXT, frase TEXT, frasetrad TEXT, frase2 TEXT, frasetrad2 TEXT, '
                  'frase3	TEXT, frasetrad3 TEXT, figura1 TEXT, som1 TEXT, Ordem TEXT, suaresposta1 TEXT, '
                  'suaresposta2	TEXT, suaresposta3 TEXT)')

        c.execute('INSERT INTO tableclone (id, palavra, palavratrad, frase, frasetrad, frase2, frasetrad2, '
                  'frase3, frasetrad3, figura1, som1, Ordem, suaresposta1, suaresposta2, suaresposta3) '
                  'SELECT NULL, palavra, '
                  'palavratrad, frase, frasetrad, frase2, frasetrad2, frase3, frasetrad3, figura1, som1, '
                  'Ordem, suaresposta1, suaresposta2, suaresposta3 FROM dictapp_dictclass')
        c.commit()

        # 3- Destruir dictapp_dictclass
        c.execute('drop table dictapp_dictclass')

        # Renomear tabela tableclone para dictapp_dictclass
        c.execute('ALTER TABLE tableclone RENAME TO dictapp_dictclass')

        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        return redirect('url_principal_ale', pk=n_primeiro)

    if request.POST.get('primeiro'):
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        return redirect('url_principal_ale', pk=n_primeiro)

    if request.POST.get('proximo'):
        banquinho = 'db_ale'
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        campo = 'id'
        #user = request.user
        #banquinho = str(user)
        obj_ultimo = dictclass.objetos.using(banquinho).last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = dictclass.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        # valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = n_primeiro

        return redirect('url_principal_ale', pk=n)

    if request.POST.get('anterior'):
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = n_primeiro

        return redirect('url_principal_ale', pk=n)

    if request.POST.get('Sortear_AlePort'):
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_sessao_testar_ale', pk=n_rand)

    if request.POST.get('Sortear_PortAle'):
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_sessao_testar_port_ale', pk=n_rand)

    if request.POST.get('Sortear_Audio'):
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_sessao_testar_audio_ale', pk=n_rand)

    if request.POST.get('Sortear_Figura'):
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_sessao_testar_figura_ale', pk=n_rand)

    if request.POST.get('ultimo'):
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_principal_ale', pk=n)

    if request.POST.get('audio_f1'):
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo

        frasex = obj.frase
        tts = gTTS(text=frasex, lang='de')
        tts.save('ale.mp3')
        os.system("ale.mp3")

        return redirect('url_principal_ale', pk=n)

    data['form'] = form
    data['objetinho'] = objetinho
    return render(request, 'dictapp/principal_ale.html', data)

def principal_ing(request, pk):
    data = {}
    banquinho = 'db_ing'
    objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
    form = DictForm(request.POST or None, instance=objetinho)
    objsuaresp = dictclass.objetos.using(banquinho).get(pk=pk)
    objsuaresp.suaresposta1 = ''
    x = objsuaresp.suaresposta1
    objsuaresp.save()

    if request.POST.get('Sair'):
        return redirect('url_entrada')

    if request.POST.get('Novo'):
        objeto_ultimo = dictclass.objetos.using(banquinho).last()
        n_saida_ultimo = objeto_ultimo.id
        pk_next = n_saida_ultimo + 1
        objeto_novo = dictclass.objetos.using(banquinho).last()
        objeto_novo.pk = None
        objeto_novo.pk = pk_next
        objeto_novo.id = pk_next
        objeto_novo.Ordem = pk_next
        objeto_novo.palavra = ''
        objeto_novo.palavratrad = ''
        objeto_novo.frase = ''
        objeto_novo.frasetrad = ''
        objeto_novo.frase2 = ''
        objeto_novo.frasetrad2 = ''
        objeto_novo.frase3 = ''
        objeto_novo.frasetrad3 = ''
        objeto_novo.figura1 = '/static/dictapp/img/vazio.jpg'
        objeto_novo.som1 = '/static/dictapp/sons/vazio.mp3'
        objeto_novo.save()
        return redirect('url_editar_ing', pk=pk_next)

    if request.POST.get('Editar'):
        data = {}
        banquinho = 'db_ing'
        objetinho = dictclass.objetos.using(banquinho).get(pk=pk)
        form = DictForm(request.POST or None, instance=objetinho)
        return redirect('url_editar_ing', pk=pk)

    if request.POST.get('Excluir'):
        objetinho.delete()
        c = sqlite3.connect('db_ing.sqlite3')

        # 1- CRIAR TABELA CLONADA table tableclone sem ID
        c.execute('CREATE TABLE tableclone (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
                  'palavra TEXT, palavratrad TEXT, frase TEXT, frasetrad TEXT, frase2 TEXT, frasetrad2 TEXT, '
                  'frase3	TEXT, frasetrad3 TEXT, figura1 TEXT, som1 TEXT, Ordem TEXT, suaresposta1 TEXT, '
                  'suaresposta2	TEXT, suaresposta3 TEXT)')

        c.execute('INSERT INTO tableclone (id, palavra, palavratrad, frase, frasetrad, frase2, frasetrad2, '
                  'frase3, frasetrad3, figura1, som1, Ordem, suaresposta1, suaresposta2, suaresposta3) '
                  'SELECT NULL, palavra, '
                  'palavratrad, frase, frasetrad, frase2, frasetrad2, frase3, frasetrad3, figura1, som1, '
                  'Ordem, suaresposta1, suaresposta2, suaresposta3 FROM dictapp_dictclass')
        c.commit()

        # 3- Destruir dictapp_dictclass
        c.execute('drop table dictapp_dictclass')

        # Renomear tabela tableclone para dictapp_dictclass
        c.execute('ALTER TABLE tableclone RENAME TO dictapp_dictclass')

        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        return redirect('url_principal_ing', pk=n_primeiro)

    if request.POST.get('primeiro'):
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        return redirect('url_principal_ing', pk=n_primeiro)

    if request.POST.get('proximo'):
        banquinho = 'db_ing'
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        campo = 'id'
        # user = request.user
        # banquinho = str(user)
        obj_ultimo = dictclass.objetos.using(banquinho).last()
        valor_ultimo = getattr(obj_ultimo, campo)
        total = valor_ultimo
        obj_atual = dictclass.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj_atual, campo)
        # valor_campo = getattr(obj_atual, campo)
        n = valor_campo + 1
        if n > total:
            n = n_primeiro

        return redirect('url_principal_ing', pk=n)

    if request.POST.get('anterior'):
        obj_primeiro = dictclass.objetos.using(banquinho).first()
        n_primeiro = obj_primeiro.id
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo - 1
        if n == 0:
            n = n_primeiro

        return redirect('url_principal_ing', pk=n)

    if request.POST.get('Sortear_IngPort'):
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_sessao_testar_ing', pk=n_rand)

    if request.POST.get('Sortear_PortIng'):
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_sessao_testar_port_ing', pk=n_rand)

    if request.POST.get('Sortear_Audio'):
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_sessao_testar_audio_ing', pk=n_rand)

    if request.POST.get('Sortear_Figura'):
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        total = valor_campo
        n_rand = randint(1, total)
        return redirect('url_sessao_testar_figura_ing', pk=n_rand)

    if request.POST.get('ultimo'):
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).last()
        valor_campo = getattr(obj, campo)
        n = valor_campo
        return redirect('url_principal_ing', pk=n)

    if request.POST.get('audio_f1'):
        campo = 'id'
        obj = dictclass.objetos.using(banquinho).get(pk=pk)
        valor_campo = getattr(obj, campo)
        n = valor_campo

        frasex = obj.frase
        tts = gTTS(text=frasex, lang='en')
        tts.save('ing.mp3')
        os.system("ing.mp3")

        return redirect('url_principal_ing', pk=n)

    data['form'] = form
    data['objetinho'] = objetinho
    return render(request, 'dictapp/principal_ing.html', data)


def Entrada_sobre(request):
    return render(request, "dictapp/Entrada_sobre.html")


# @staff_member_required
def Entrada_configuracoes(request):
    """"
    if request.POST.get('editar_eprogModel'):
        return redirect('url_Editar_EprogModel', pk=1)

    if request.POST.get('editar_calculosModel'):
        return redirect('url_Editar_CalculosModel', pk=1)

    if request.POST.get('editar_procedimentoModel'):
        return redirect('url_Editar_ProcedimentoModel', pk=1)

    if request.POST.get('editar_sessaoModel'):
        return redirect('url_Editar_SessaoModel', pk=1)

    if request.POST.get('reset_eprogModel'):
        return redirect('url_Reset_EprogModel')

    if request.POST.get('reset_calculosModel'):
        return redirect('url_Reset_CalculosModel')

    if request.POST.get('reset_procedimentoModel'):
        return redirect('url_Reset_procedimentoModel')

    if request.POST.get('reset_sessaoModel'):
        return redirect('url_Reset_SessaoModel', pk=1)
    """

    return render(request, "dictapp/Entrada_configuracoes.html")


# @staff_member_required
def Entrada_relatorios(request):
    """
    user = request.user
    banquinho = str(user)
    if request.POST.get('export'):
        #listax = SessaoModel.objetos.using(banquinho).all()
        #listax = SessaoModel.objetos.using(banquinho).values()
        listax= SessaoModel.objetos.using(banquinho).values_list(
            'Participante', 'Modulo', 'Sessao', 'Dia', 'Horario', 'Ordem', 'Acertou', 'DuvidaComent', )

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)
        writer.writerow(['Participante', 'Modulo', 'Sessao', 'Dia', 'Horario', 'Ordem', 'Acertou', 'DuvidaComent'])
        for item in listax:
            print(item)
            writer = csv.writer(response)
            writer.writerow([item])
        return response
        """
    return render(request, "dictapp/Entrada_relatorios.html")
