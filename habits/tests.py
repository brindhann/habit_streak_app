
from datetime import date, timedelta

from django.test import TestCase

from .models import Habit


class HabitStreakTests(TestCase):

    def setUp(self):
        self.habit = Habit.objects.create(name="Workout")

    def test_initial_streak_is_zero(self):
        self.assertEqual(self.habit.streak, 0)
        self.assertIsNone(self.habit.last_completed)

    def test_first_completion_starts_streak_at_one(self):
        self.habit.complete()

        self.habit.refresh_from_db()

        self.assertEqual(self.habit.streak, 1)
        self.assertEqual(self.habit.last_completed, date.today())

    def test_multiple_completions_on_same_day_do_not_increase_streak(self):
        self.habit.complete()
        self.habit.complete()

        self.habit.refresh_from_db()

        self.assertEqual(self.habit.streak, 1)

    def test_consecutive_day_increases_streak(self):
        yesterday = date.today() - timedelta(days=1)

        self.habit.streak = 3
        self.habit.last_completed = yesterday
        self.habit.save()

        self.habit.complete()

        self.habit.refresh_from_db()

        self.assertEqual(self.habit.streak, 4)
        self.assertEqual(self.habit.last_completed, date.today())

    def test_missed_day_resets_streak_to_one(self):
        two_days_ago = date.today() - timedelta(days=2)

        self.habit.streak = 5
        self.habit.last_completed = two_days_ago
        self.habit.save()

        self.habit.complete()

        self.habit.refresh_from_db()

        self.assertEqual(self.habit.streak, 1)
        self.assertEqual(self.habit.last_completed, date.today())
