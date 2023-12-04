from database.db import get_connection
from .entities.Movie import Movie

class MovieModel():
	@classmethod
	def get_movies(self):
		try:
			connection=get_connection()
			movies=[]
			with connection.cursor() as cursor:
				cursor.execute("SELECT  id,title,duration,releases FROM pelicula ORDER BY title ASC")
				resultset=cursor.fetchall()
				for row in resultset:
					mov=Movie(row[0],row[1],row[2],row[3])
					movies.append(mov.to_JSON())
			connection.close()
			return movies
		except Exception as e:
			raise e

	@classmethod
	def get_movie(self,id):
		try:
			connection=get_connection()			
			with connection.cursor() as cursor:
				cursor.execute("SELECT  id,title,duration,releases FROM pelicula WHERE id=%s",(id,))
				row=cursor.fetchone()
				mov=None
				if not row==None:				
					mov=Movie(row[0],row[1],row[2],row[3])
					mov=mov.to_JSON()
			connection.close()
			return mov
		except Exception as e:
			raise e

	@classmethod
	def add_movie(self,movie):
		try:
			connection=get_connection()			
			with connection.cursor() as cursor:
				cursor.execute("""INSERT INTO pelicula(id,title,duration,releases) VALUES(%s,%s,%s,%s)""",
								(movie.id,movie.title,movie.duration,movie.released))
				
				row_affected=cursor.rowcount
				connection.commit()
			connection.close()
			return row_affected
		except Exception as e:
			raise e

	@classmethod
	def delete_movie(self,movie):
		try:
			connection=get_connection()			
			with connection.cursor() as cursor:
				cursor.execute("DELETE FROM pelicula WHERE id=%s",(movie.id,))				
				row_affected=cursor.rowcount
				connection.commit()
			connection.close()
			return row_affected
		except Exception as e:
			raise e

	@classmethod
	def update_movie(self,movie):
		try:
			connection=get_connection()			
			with connection.cursor() as cursor:
				cursor.execute("""UPDATE pelicula SET title=%s,duration=%s,releases=%s WHERE id=%s""",(movie.title,movie.duration,movie.released,movie.id))
				
				row_affected=cursor.rowcount
				connection.commit()
			connection.close()
			return row_affected
		except Exception as e:
			raise e