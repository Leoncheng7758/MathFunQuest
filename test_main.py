import unittest
from unittest.mock import patch

from kivy.uix.button import Button
from kivy.animation import Animation

from main import MathFunQuestApp


class CountingTests(unittest.TestCase):
    def setUp(self):
        self.app = MathFunQuestApp()
        self.manager = self.app.build()
        self.game = self.manager.get_screen('count')

    def tearDown(self):
        if getattr(self.game, '_next_question', None) is not None:
            self.game._next_question.cancel()
        for button in self.game.answer_layout.children:
            Animation.cancel_all(button)

    def correct_button(self):
        quantity = self.game.objects.text.count('●')
        return next(button for button in self.game.answer_layout.children
                    if button.text == str(quantity))

    def test_correct_answer_works_when_imported(self):
        self.correct_button().dispatch('on_press')
        self.assertEqual(self.game.score, 1)

    def test_wrong_answer_does_not_score_or_schedule_a_question(self):
        correct = self.correct_button()
        wrong = next(button for button in self.game.answer_layout.children
                     if button is not correct)
        with patch('main.Clock.schedule_once') as schedule:
            wrong.dispatch('on_press')
            schedule.assert_not_called()
        self.assertEqual(self.game.score, 0)
        self.assertTrue(all(not button.disabled for button in self.game.answer_layout.children))

    def test_every_question_displays_the_correct_number_of_objects(self):
        for correct in range(3, 9):
            with patch('main.random.randint', side_effect=[correct, 1, 2]):
                self.game.create_options()
            self.assertEqual(self.game.objects.text.count('●'), correct)
            choices = [int(button.text) for button in self.game.answer_layout.children]
            self.assertEqual(len(set(choices)), 3)
            self.assertIn(correct, choices)
            self.assertIn('数一数', self.game.question.text)

    def test_rapid_correct_answers_award_only_one_point_and_timer(self):
        button = self.correct_button()
        with patch('main.Clock.schedule_once') as schedule:
            button.dispatch('on_press')
            button.dispatch('on_press')
            self.assertEqual(self.game.score, 1)
            schedule.assert_called_once()
        self.assertTrue(all(button.disabled for button in self.game.answer_layout.children))

    def test_next_question_restores_prompt_and_buttons(self):
        with patch('main.Clock.schedule_once'):
            self.correct_button().dispatch('on_press')
        self.game._advance_question(0)
        self.assertIn('数一数', self.game.question.text)
        self.assertTrue(all(not button.disabled for button in self.game.answer_layout.children))
        self.assertEqual(self.game.score, 1)

    def test_leaving_screen_cancels_pending_question(self):
        with patch('main.Clock.schedule_once') as schedule:
            self.correct_button().dispatch('on_press')
            self.game.on_leave()
            schedule.return_value.cancel.assert_called_once()
        self.assertIsNone(self.game._next_question)
        self.assertIn('数一数', self.game.question.text)

    def test_counting_screen_has_working_return_button(self):
        self.manager.current = 'count'
        back = next(widget for widget in self.game.walk()
                    if isinstance(widget, Button) and widget.text == '返回主菜单')
        back.dispatch('on_press')
        self.assertEqual(self.manager.current, 'menu')


if __name__ == '__main__':
    unittest.main()
