import unittest
from client import getRatio
class TestGetRatio(unittest.TestCase):
	def runTest(self):
		self.assertEqual(getRatio( 242.76, 245.94), 0.9870700170773359, "Correct Ratio")

		self.assertEqual(getRatio(242.76, 0), None, 'Parameters cant be zero')

		
		with self.assertRaises(ZeroDivisionError):
			zero = 242.76 / 0			

unittest.main()
