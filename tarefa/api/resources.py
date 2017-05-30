from tastypie.resources import ModelResource
from tastypie import fields, utils
from tastypie.authorization import Authorization
from tarefa.models import *
from django.contrib.auth.models import User
from tastypie.exceptions import Unauthorized

class ProjetoUsuarioResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized("Voce não pode deletar toda a lista");

    class Meta:
        queryset = ProjetoUsuario.objects.all() #lista ou consulta do recurso
        allowed_methods = ['get','post','put','delete']
        filtering = { #aplicações de filtros, recebe um json
            "projeto": ('exact', 'startswith',) #o campo descrição é para fornecer dois tipos de filtros, passando a palavra exata e um tipo de filtro
        }
        authorization = Authorization() #permite que qualquer pessoa faça requisições (chamadas) para APIS (chamadas Put)

class UsuarioResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized("Voce não pode deletar toda a lista");

    class Meta:
        queryset = Usuario.objects.all() #lista ou consulta do recurso
        allowed_methods = ['get','post','put','delete']
        filtering = { #aplicações de filtros, recebe um json
            "nome": ('exact', 'startswith',) #o campo descrição é para fornecer dois tipos de filtros, passando a palavra exata e um tipo de filtro
        }
        authorization = Authorization() #permite que qualquer pessoa faça requisições (chamadas) para APIS (chamadas Put)

class ProjetoResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized("Voce não pode deletar toda a lista");

    class Meta:
        queryset = Projeto.objects.all() #lista ou consulta do recurso
        allowed_methods = ['get','post','put','delete']
        filtering = { #aplicações de filtros, recebe um json
            "nome": ('exact', 'startswith',) #o campo nome é para fornecer dois tipos de filtros, passando a palavra exata e um tipo de filtro
        }
        authorization = Authorization() #permite que qualquer pessoa faça requisições (chamadas) para APIS (chamadas Put)

class TarefaResource(ModelResource):
    def obj_create(self, bundle, **kwargs):
        projeto = bundle.data['projeto'].split("/")
        usuario = bundle.data['usuario'].split("/")

        print(projeto[4])

        #verifica se o projeto não está cadastrado
        if not(Tarefa.objects.filter(projeto=projeto[4])):
            tarefa = Tarefa()
            tarefa.nome = bundle.data['nome']
            tarefa.projeto = Projeto.objects.get(pk=projeto[4])
            tarefa.usuario = Usuario.objects.get(pk=usuario[4])
            tarefa.save() #salva os dados
            bundle.obj = tarefa #salva o objeto que acabou de ser criado, dentro do bundle
            return bundle
        else:
            raise Unauthorized('Já existe um projeto cadastrado entre as tarefas');

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized("Voce não pode deletar toda a lista");

    def obj_delete(self, bundle, **kwargs):
        return bundle.obj.user == bundle.request.user

    def obj_update(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    class Meta:
        queryset = Tarefa.objects.all() #lista ou consulta do recurso
        allowed_methods = ['get','post','put','delete']
        filtering = { #aplicações de filtros, recebe um json
            "nome": ('exact', 'startswith',) #o campo descrição é para fornecer dois tipos de filtros, passando a palavra exata e um tipo de filtro
        }
