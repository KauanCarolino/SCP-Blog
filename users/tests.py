from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase

from users.context_processors import agent_clearance
from users.models import AgentProfile

User = get_user_model()


class AgentProfileSignalTests(TestCase):
    def test_should_create_agent_profile_on_user_create(self) -> None:
        user = User.objects.create_user(username='agent_x', password='testpass123')
        profile = AgentProfile.objects.get(user=user)
        self.assertEqual(profile.clearance_level, AgentProfile.ClearanceLevel.LEVEL_0)
        self.assertEqual(profile.personnel_class, AgentProfile.PersonnelClass.C)

    def test_should_have_valid_clearance_choices(self) -> None:
        values = {choice.value for choice in AgentProfile.ClearanceLevel}
        self.assertEqual(values, {0, 1, 2, 3, 4, 5})
        labels = {choice.label for choice in AgentProfile.ClearanceLevel}
        self.assertIn('Restrito', labels)
        self.assertIn('Thaumiel', labels)

    def test_should_have_valid_personnel_class_choices(self) -> None:
        values = {choice.value for choice in AgentProfile.PersonnelClass}
        self.assertEqual(values, {'A', 'B', 'C', 'D', 'E'})


class AgentClearanceContextProcessorTests(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_should_expose_anonymous_clearance(self) -> None:
        from django.contrib.auth.models import AnonymousUser

        request = self.factory.get('/')
        request.user = AnonymousUser()
        ctx = agent_clearance(request)
        self.assertEqual(ctx['agent_clearance']['level'], 0)
        self.assertFalse(ctx['agent_clearance']['authorized'])
        self.assertFalse(ctx['agent_clearance']['is_authenticated'])
        self.assertIn('SEM CREDENCIAL', ctx['agent_clearance']['label'])

    def test_should_expose_authenticated_clearance(self) -> None:
        user = User.objects.create_user(username='agent_y', password='testpass123')
        profile = user.agent_profile
        profile.clearance_level = AgentProfile.ClearanceLevel.LEVEL_2
        profile.save(update_fields=['clearance_level'])

        request = self.factory.get('/')
        request.user = user
        ctx = agent_clearance(request)
        data = ctx['agent_clearance']
        self.assertEqual(data['level'], 2)
        self.assertTrue(data['authorized'])
        self.assertEqual(data['short'], 'NÍVEL 2')
        self.assertEqual(data['label'], 'NÍVEL 2 · RESTRITO')
        self.assertEqual(data['personnel_class'], 'C')
