import unittest

from ctci import coins

class Test(unittest.TestCase):
  def test_coins1(self):
    self.assertEqual(int(coins.coins1(0)), 1)
    self.assertEqual(int(coins.coins1(1)), 1)
    self.assertEqual(int(coins.coins1(4)), 1)
    self.assertEqual(int(coins.coins1(5)), 2)

if __name__ == "__main__":
  unittest.main()

