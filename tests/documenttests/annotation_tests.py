import opencv as cv2
import unittest
import page
import line
import document

class highlight_test_case(unittest.TestCase):

	def setUp(self):
		self.highlight = Highlight(11, 100)
		self.highlight1 = Highlight(22, 200)

	def test_color(self):
		self.highlight.set_color("#b5b5b5")
		self.assertTrue(self.highlight.get_color() == "#b5b5b5")
		self.highlight.set_color("apple")
		self.assertTrue(self.highlight.get_color() == "#b5b5b5")

	def test_id(self):
		self.assertTrue(self.highlight.get_id() == 0)
		self.assertTrue(self.highlight1.get_id() == 1)

	def test_start_end(self):
		self.assertTrue(self.highlight.get_start() == 11)
		self.assertTrue(self.highlight.get_end() == 100)
		self.assertTrue(self.highlight1.get_start() == 22)
		self.assertTrue(self.highlight1.get_end() == 200)


if __name__ == '__main__':
    unittest.main()