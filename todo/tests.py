from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from todo.models import Task

# Create your tests here.
class SampleTestCase(TestCase):
    def test_sample1(self):
        self.assertEqual(1 + 2, 3)

class TaskModelCase(TestCase):
    def test_create_task1(self):
        due = timezone.make_aware(datetime(2026, 6, 18, 12, 00, 00))
        task = Task(title='task1', due_at=due)
        task.save()

        task = Task.objects.get(pk=task.pk)
        self.assertEqual(task.title, 'task1')
        self.assertFalse(task.completed)
        self.assertEqual(task.due_at, due)

    def test_create_task2(self):
        task = Task(title='task2')
        task.save()

        task = Task.objects.get(pk=task.pk)
        self.assertEqual(task.title, 'task2')
        self.assertFalse(task.completed)
        self.assertEqual(task.due_at, None)

    def test_is_overdue_future(self):
        due = timezone.make_aware(datetime(2026, 6, 18, 12, 00, 00))
        current = timezone.make_aware((datetime(2026, 6, 18, 00, 00, 00)))
        task = Task(title='task1', due_at=due)
        task.save()

        self.assertFalse(task.is_overdue(current))
        