from __future__ import annotations

from typing import Any

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import AgentProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_agent_profile(
    sender: type,
    instance: Any,
    created: bool,
    **kwargs: object,
) -> None:
    if created:
        AgentProfile.objects.create(
            user=instance,
            clearance_level=AgentProfile.ClearanceLevel.LEVEL_0,
            personnel_class=AgentProfile.PersonnelClass.C,
        )
