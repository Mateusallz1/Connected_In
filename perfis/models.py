from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length= 255, null = False)
    email = models.EmailField(max_length= 255, null = False)
    telefone = models.CharField(max_length= 15, null = False)
    nome_empresa = models.CharField(max_length= 255, null = False)

    '''
    def __init__(self, id = 0, nome= '', email= '', telefone= '', nome_empresa= ''):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nome_empresa = nome_empresa
    '''
    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self, convidado=perfil_convidado)
        convite.save()
        
class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name = 'convites_feitos', on_delete= models.CASCADE)
    convidado = models.ForeignKey(Perfil, related_name = 'convites_recebidos', on_delete= models.CASCADE)

# Create your models here.
