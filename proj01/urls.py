from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dictapp import views
from dictapp.views import editar_ale, editar_ing, \
                            sessao_testar_ale, sessao_testar_ing,\
                            principal_ale, principal_ing,\
                            Entrada_Iniciar, Entrada_login,\
                            Entrada_sobre, Entrada,\
                            Entrada_configuracoes, Entrada_relatorios,\
                            sessao_testar_audio_ale, sessao_testar_port_ale, sessao_testar_figura_ale,\
                            sessao_testar_audio_ing, sessao_testar_port_ing, sessao_testar_figura_ing,\
                            sessao_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Entrada, name='url_entrada'),
    path('', views.Home.as_view(), name='home'),
    #path('upload', views.upload, name='upload'),
 
    path('Entrada_Iniciar/', Entrada_Iniciar, name='url_Entrada_Iniciar'),
    path('Entrada_login/', Entrada_login, name='url_Entrada_login'),
    path('Entrada_configuracoes/', Entrada_configuracoes, name='url_Entrada_configuracoes'),
    path('Entrada_relatorios/', Entrada_relatorios, name='url_Entrada_relatorios'),
    path('Entrada_sobre/', Entrada_sobre, name='url_Entrada_sobre'),

    path('editar_ale/<int:pk>/', editar_ale, name='url_editar_ale'),
    path('editar_ing/<int:pk>/', editar_ing, name='url_editar_ing'),


    path('principal_ale/<int:pk>/', principal_ale, name='url_principal_ale'),
    path('principal_ing/<int:pk>/', principal_ing, name='url_principal_ing'),

    path('sessao_testar_ale/<int:pk>/', sessao_testar_ale, name='url_sessao_testar_ale'),
    path('sessao_testar_port_ale/<int:pk>/', sessao_testar_port_ale, name='url_sessao_testar_port_ale'),
    path('sessao_testar_audio_ale/<int:pk>/', sessao_testar_audio_ale, name='url_sessao_testar_audio_ale'),
    path('sessao_testar_figura_ale/<int:pk>/', sessao_testar_figura_ale, name='url_sessao_testar_figura_ale'),

    path('sessao_testar_ing/<int:pk>/', sessao_testar_ing, name='url_sessao_testar_ing'),
    path('sessao_testar_port_ing/<int:pk>/', sessao_testar_port_ing, name='url_sessao_testar_port_ing'),
    path('sessao_testar_audio_ing/<int:pk>/', sessao_testar_audio_ing, name='url_sessao_testar_audio_ing'),
    path('sessao_testar_figura_ing/<int:pk>/', sessao_testar_figura_ing, name='url_sessao_testar_figura_ing'),
    path('sessao_upload/<int:pk>/', sessao_upload, name='url_sessao_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
    path('', entrada, name='url_entrada'),
    path('teste/', teste_view, name= 'url_teste_view'),
    path('teste2/', teste2_view, name= 'url_teste2_view'),
    path('teste_loop/', teste_loop, name= 'url_teste_loop_view'),
    path('criar_tabela/', criar_tabela, name= 'url_criar_tabela'),
    path('clonar/', clonar_model, name='url_clonar_model'),
    path('Parabens/', parabens_view, name='url_parabens_view'),

    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    path('principal/<int:pk>/', principal, name='url_principal'),
    path('update/<int:pk>/', update, name='url_update'),
    path('sessao/<int:pk>/', sessao_view, name='url_sessao'),
    path('sessao_testar/<int:pk>/', sessao_testar, name='url_sessao_testar'),
    path('comecar_sessao/', comecar_sessao_view , name='url_comecar_sessao'),

    path('Editar_EprogModel/<int:pk>', Editar_EprogModel, name='url_Editar_EprogModel'),
    path('Editar_CalculosModel/<int:pk>', Editar_CalculosModel, name='url_Editar_CalculosModel'),
    path('Editar_ProcedimentoModel/<int:pk>', Editar_ProcedimentoModel, name='url_Editar_ProcedimentoModel'),
    path('Editar_SessaoModel/<int:pk>', Editar_SessaoModel, name='url_Editar_SessaoModel'),

    path('Reset_EprogModel/', Reset_EprogModel, name='url_Reset_EprogModel'),
    path('Reset_CalculosModel/', Reset_CalculosModel, name='url_Reset_CalculosModel'),
    path('Reset_ProcedimentoModel/', Reset_ProcedimentoModel, name='url_Reset_ProcedimentoModel'),
    path('Reset_SessaoModel/<int:pk>', Reset_SessaoModel, name='url_Reset_SessaoModel'),

    path('principal_hidden/<int:pk>/', principal_hidden, name='url_principal_hidden'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("logout/", LogoutView.as_view(), name="logout"),
"""
