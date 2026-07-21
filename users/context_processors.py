from __future__ import annotations

from typing import Any

from django.http import HttpRequest

from users.models import AgentProfile


def agent_clearance(request: HttpRequest) -> dict[str, Any]:
    """Expose the current user's SCP clearance to all templates.

    Profile creation is handled by users.signals — this processor never writes.
    `authorized` means logged-in vs guest UI (not a clearance gate).
    """
    user = request.user

    if not user.is_authenticated:
        return {
            'agent_clearance': {
                'level': 0,
                'label': 'NÍVEL 0 · SEM CREDENCIAL',
                'short': 'NÍVEL 0',
                'personnel_class': None,
                'is_authenticated': False,
                'authorized': False,
            }
        }

    try:
        profile: AgentProfile | None = user.agent_profile
    except AgentProfile.DoesNotExist:
        profile = None

    if profile is None:
        return {
            'agent_clearance': {
                'level': 0,
                'label': 'NÍVEL 0 · SEM CREDENCIAL',
                'short': 'NÍVEL 0',
                'personnel_class': None,
                'is_authenticated': True,
                'authorized': True,
            }
        }

    level = int(profile.clearance_level)
    clearance_label = profile.get_clearance_level_display().upper()

    return {
        'agent_clearance': {
            'level': level,
            'label': f'NÍVEL {level} · {clearance_label}',
            'short': f'NÍVEL {level}',
            'personnel_class': profile.personnel_class,
            'is_authenticated': True,
            'authorized': True,
        }
    }
