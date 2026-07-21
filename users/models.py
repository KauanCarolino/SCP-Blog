from django.conf import settings
from django.db import models


class AgentProfile(models.Model):
    class ClearanceLevel(models.IntegerChoices):
        LEVEL_0 = 0, 'Apenas Para Uso Oficial'
        LEVEL_1 = 1, 'Confidencial'
        LEVEL_2 = 2, 'Restrito'
        LEVEL_3 = 3, 'Secreto'
        LEVEL_4 = 4, 'Ultra Secreto'
        LEVEL_5 = 5, 'Thaumiel'

    class PersonnelClass(models.TextChoices):
        A = 'A', 'Classe A'
        B = 'B', 'Classe B'
        C = 'C', 'Classe C'
        D = 'D', 'Classe D'
        E = 'E', 'Classe E'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='agent_profile',
        verbose_name='Usuário',
    )
    clearance_level = models.PositiveSmallIntegerField(
        choices=ClearanceLevel.choices,
        default=ClearanceLevel.LEVEL_0,
        verbose_name='Nível de Credencial',
    )
    personnel_class = models.CharField(
        max_length=1,
        choices=PersonnelClass.choices,
        default=PersonnelClass.C,
        verbose_name='Classe de Pessoal',
    )
    site_assignment = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name='Atribuição de Site',
    )

    class Meta:
        verbose_name = 'Perfil do Agente'
        verbose_name_plural = 'Perfis dos Agentes'

    def __str__(self) -> str:
        return f'user_id={self.user_id} — Nível {self.clearance_level}'
