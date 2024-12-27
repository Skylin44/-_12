import unittest
from unittest import TestCase
from HumanMoveTest.runner import Runner


class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner('Оля')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
        self.is_frozen = False

    def test_run(self):
        runner = Runner('Оля')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    def test_challenge(self):
        runner1 = Runner('Оля')
        runner2 = Runner('Витя')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
