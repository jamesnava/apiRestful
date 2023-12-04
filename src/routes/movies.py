from flask import Blueprint,jsonify,request
#importamos los models
from models.MovieModel import MovieModel
#importamos entidad movies
from models.entities.Movie import Movie
import uuid


main=Blueprint('movie_blueprint',__name__)

@main.route('/')
def get_movies():
	try:
		movies=MovieModel.get_movies()
		return jsonify(movies)
	except Exception as e:
		raise e

@main.route('/<id>')
def get_movie(id):
	try:
		movie=MovieModel.get_movie(id)
		if not movie==None:
			return jsonify(movie)
		else:
			return jsonify({"message":"Datos no encontrados"}),404
	except Exception as e:
		raise e

@main.route('/add',methods=["POST"])
def add_movie():
	try:
		title=request.json['title']
		duration=int(request.json['duration'])
		releases=request.json['releases']
		id=uuid.uuid4()		
		mov=Movie(str(id),title,duration,releases)
		rows_Affected=MovieModel.add_movie(mov)
		if rows_Affected:
			return jsonify(mov.id)
		else:
			return jsonify({"error":"error al insertar"})
		
	except Exception as e:
		return jsonify({'message':str(e)}),500

@main.route('/update/<id>',methods=["PUT"])
def update_movie(id):
	try:
		title=request.json['title']
		duration=int(request.json['duration'])
		releases=request.json['releases']			
		mov=Movie(id,title,duration,releases)
		rows_Affected=MovieModel.update_movie(mov)
		if rows_Affected:
			return jsonify(mov.id)
		else:
			return jsonify({"error":"no pudo actualizarse"})
		
	except Exception as e:
		return jsonify({'message':str(e)}),500

@main.route('/delete/<id>',methods=["DELETE"])
def delete_movie(id):
	try:
					
		mov=Movie(id)
		rows_Affected=MovieModel.delete_movie(mov)
		if rows_Affected:
			return jsonify(mov.id)
		else:
			return jsonify({"error":"objeto no se pudo eliminar"})
		
	except Exception as e:
		return jsonify({'message':str(e)}),500
	