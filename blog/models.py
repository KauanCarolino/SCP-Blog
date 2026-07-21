from django.db import models
from django.contrib.auth.models import User

from blog.config.model import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

NOT_SPECIFIED = 'NOT_SPECIFIED'
SAFE = 'SAFE'
EUCLID = 'EUCLID'
KETER = 'KETER'

OBJECT_CLASS_CHOICES = (
    (NOT_SPECIFIED, "Não Especificado"),
    (SAFE, "Seguro"),
    (EUCLID, "Euclideo"),
    (KETER, "Keter"),
)


class Publication(BaseModel):
    class StateContainment(models.IntegerChoices):
        CONTAINED = 0, 'Contido'
        SAFE = 1, 'Seguro'
        CRITICAL = 2, 'Crítico'

    title = models.CharField(max_length=50, verbose_name='Título')
    item_number = models.CharField(max_length=50, verbose_name='Número do Item')
    name_SCP = models.CharField(max_length=50, verbose_name='Nome SCP')
    object_class = models.CharField(
        max_length=13, choices=OBJECT_CLASS_CHOICES, 
        default=NOT_SPECIFIED, verbose_name='Classe do Objeto')
    image = models.ImageField(
        upload_to='scpImage/cover/%Y/%m/%d/', blank=True, default='', verbose_name='Imagem')
    resume = models.CharField(max_length=100, verbose_name='Resumo')
    special_containment_procedures = models.TextField(verbose_name='Procedimentos de Contenção Especial')
    description = models.TextField(verbose_name='Descrição')
    addendum = models.TextField(null=True, blank=True, verbose_name='Adendo')
    is_published = models.BooleanField(default=False, verbose_name='Publicado')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None, verbose_name='Categoria')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Autor')
    state_containment = models.IntegerField(
        choices=StateContainment.choices, blank=True, null=True, verbose_name='Estado de Contenção')
    local = models.CharField(max_length=100, null=True, blank=True, verbose_name='Local')

    def __str__(self):
        return self.title
    
# class News(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     image = models.ImageField(upload_to='newsImages/%Y/%m/%d/', blank=True, null=True)
#     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     publication_date = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title