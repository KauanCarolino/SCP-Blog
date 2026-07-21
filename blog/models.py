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
THAUMIEL = 'THAUMIEL'
NEUTRALIZED = 'NEUTRALIZED'
APOLLYON = 'APOLLYON'
ARCHON = 'ARCHON'
EXPLAINED = 'EXPLAINED'
PENDING = 'PENDING'

OBJECT_CLASS_CHOICES = (
    (SAFE, 'Seguro'),
    (EUCLID, 'Euclídeo'),
    (KETER, 'Keter'),
    (THAUMIEL, 'Thaumiel'),
    (NEUTRALIZED, 'Neutralizado'),
    (APOLLYON, 'Apollyon'),
    (ARCHON, 'Archon'),
    (EXPLAINED, 'Explicado'),
    (PENDING, 'Pendente'),
    (NOT_SPECIFIED, 'Não Especificado'),
)

WHITE = 'WHITE'
YELLOW = 'YELLOW'
ORANGE = 'ORANGE'
RED = 'RED'
PURPLE = 'PURPLE'
BLACK = 'BLACK'
INDETERMINATE = 'INDETERMINATE'

THREAT_LEVEL_CHOICES = (
    (WHITE, 'Branco'),
    (YELLOW, 'Amarelo'),
    (ORANGE, 'Laranja'),
    (RED, 'Vermelho'),
    (PURPLE, 'Roxo'),
    (BLACK, 'Preto'),
    (INDETERMINATE, 'Indeterminado'),
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
        max_length=20,
        choices=OBJECT_CLASS_CHOICES,
        default=NOT_SPECIFIED,
        verbose_name='Classe do Objeto',
    )
    threat_level = models.CharField(
        max_length=20,
        choices=THREAT_LEVEL_CHOICES,
        default=INDETERMINATE,
        verbose_name='Nível de Ameaça',
    )
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
