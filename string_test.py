import unittest

class StringTestCase(unittest.TestCase):

	def test_lower(self):
		data = "THIS IS A STRING"
		self.assertEqual(data.lower(), 'this is a string')

	def test_upper(self):
		data = 'this is a string'
		self.assertEqual(data.upper(), 'THIS IS A STRING')

	def test_count(self):
		data = 'this is a string'
		self.assertEqual(data.count('i'), 3)


if __name__ == '__main__':
	unittest.main()