from django.test import TestCase
from django.utils import timezone
from .models import Question


class QuestionModelTests(TestCase):
    def test_question_creation(self):
        """Test that a question can be created."""
        question = Question.objects.create(
            question_text="What's new?", pub_date=timezone.now()
        )
        self.assertEqual(question.question_text, "What's new?")

    def test_was_published_recently(self):
        """Test the was_published_recently method."""
        question = Question(question_text="Test?", pub_date=timezone.now())
        self.assertTrue(question.was_published_recently())
