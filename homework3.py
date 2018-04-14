import sqlite3
import pandas as pd

#According to https://tutorials.technology/tutorials/08-How-to-check-that-file-exists-with-Python.html, importing Path function from pathlib module is most efficient for checking if file path exists
from pathlib import Path

def create_dataframe(fp):
	#Check that file path is valid
	file = Path(fp)
	if not file.exists():
		raise ValueError
	#From https://www.dataquest.io/blog/python-pandas-databases/
	conn = sqlite3.connect(fp)
	#Query from HW 1
	return pd.read_sql_query("SELECT video_id, category_id, 'ca' AS language FROM CAvideos UNION SELECT video_id, category_id, 'de' AS language FROM DEvideos UNION SELECT video_id, category_id, 'fr' AS language FROM FRvideos UNION SELECT video_id, category_id, 'gb' AS language FROM GBvideos UNION SELECT video_id, category_id, 'us' AS language FROM USvideos;", conn)