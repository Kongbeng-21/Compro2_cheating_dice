import unittest
from dice import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        self.probs = [0.1, 0.2, 0.3, 0.1, 0.2, 0.1]
        self.dice = Dice(self.probs)

    def test_init_valid(self):
        dice = Dice([0.5, 0.5])
        self.assertEqual(dice.num_faces, 2)

    def test_init_num_faces(self):
        self.assertEqual(self.dice.num_faces, 6)

    def test_init_faces_range(self):
        self.assertEqual(self.dice.faces, [1, 2, 3, 4, 5, 6])

    def test_init_invalid_sum(self):
        with self.assertRaises(ValueError):
            Dice([0.1, 0.2, 0.3])  

    def test_init_negative_probability(self):
        with self.assertRaises(ValueError):
            Dice([-0.1, 0.6, 0.5])

    def test_init_empty_list(self):
        with self.assertRaises(ValueError):
            Dice([])

    def test_roll_returns_int(self):
        result = self.dice.roll()
        self.assertIsInstance(result, int)

    def test_roll_within_range(self):
        for _ in range(200):
            result = self.dice.roll()
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, self.dice.num_faces)

    def test_roll_many_returns_list(self):
        result = self.dice.roll_many(10)
        self.assertIsInstance(result, list)

    def test_roll_many_correct_length(self):
        for n in [1, 5, 10, 100]:
            result = self.dice.roll_many(n)
            self.assertEqual(len(result), n)

    def test_roll_many_values_within_range(self):
        results = self.dice.roll_many(500)
        for val in results:
            self.assertIn(val, self.dice.faces)

    def test_roll_many_invalid_zero(self):
        with self.assertRaises(ValueError):
            self.dice.roll_many(0)

    def test_roll_many_invalid_negative(self):
        with self.assertRaises(ValueError):
            self.dice.roll_many(-1)

    def test_roll_many_invalid_float(self):
        with self.assertRaises(ValueError):
            self.dice.roll_many(2.5)

    def test_fair_dice_distribution(self):
        fair_dice = Dice([1/6] * 6)
        rolls = fair_dice.roll_many(6000)
        for face in range(1, 7):
            count = rolls.count(face)
            self.assertGreater(count, 700, f"Face {face} appeared too rarely: {count}")
            self.assertLess(count, 1300, f"Face {face} appeared too often: {count}")

    def test_single_face_dice(self):
        dice = Dice([1.0])
        for _ in range(20):
            self.assertEqual(dice.roll(), 1)

    def test_repr(self):
        r = repr(self.dice)
        self.assertIn("Dice", r)
        self.assertIn("6", r)


if __name__ == "__main__":
    unittest.main(verbosity=2)