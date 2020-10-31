from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('Perfil')
    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)
    
    @property #Toda vez que referenciar email deve apontar pra própria classe.
    def email(self): #É como se fosse o get ou set do Java.
        return self.usuario.email
    
    def ja_possui_convite(self, perfil):               
        return (Convite.objects.filter(solicitante = self, convidado = perfil).exists() or
                Convite.objects.filter(solicitante = perfil, convidado = self).exists())

    def convidar(self, perfil_convidado):
        if self.pode_convidar(perfil_convidado):
            convite = Convite(solicitante=self, convidado=perfil_convidado)
            convite.save()

    def __str__(self):
        return self.nome

    def pode_convidar(self, perfil):
        nao_pode = self.convite_a_si_mesmo(perfil) or self.ja_eh_contato(perfil) or self.ja_possui_convite(perfil)
    
    def ja_eh_contato(self, perfil):
        return self.contatos.filter(id = perfil.id).exists()

    def convite_a_si_mesmo(self, perfil):
        return self == perfil

    '''
    def __init__(self, id = 0, nome= '', email= '', telefone= '', nome_empresa= ''):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nome_empresa = nome_empresa
    '''
        
class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name = 'convites_feitos', on_delete= models.CASCADE)
    convidado = models.ForeignKey(Perfil, related_name = 'convites_recebidos', on_delete= models.CASCADE)
    
    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()

# Create your models here.
