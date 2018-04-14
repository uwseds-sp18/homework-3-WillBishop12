import unittest
import homework3

class TestHomework3(unittest.TestCase):

	#Test for wrong file path
	def test_wrong_filepath(self):
		with self.assertRaises(ValueError):
			homework3.create_dataframe('x.db')

	#Test for column names
	def test_column_names(self):
		df = homework3.create_dataframe('class.db')
		self.assertTrue(len(df.columns) == 3)
		self.assertTrue(all(x in df.columns for x in ['video_id', 'category_id', 'language']))
	
	#Test for length
	def test_len(self):
		df = homework3.create_dataframe('class.db')
		self.assertTrue(len(df) > 9)

	#Test for key
	def test_key(self):
		df = homework3.create_dataframe('class.db')
		self.assertTrue(len(df.groupby(['video_id', 'language']).count()) == len(df))



if __name__ == '__main__':
	unittest.main()