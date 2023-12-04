from flask import Flask
from config import config
#importar rutas
from routes import movies
app=Flask(__name__)

def page_not_found(error):
	return "<h1>Page not Found</h1>",404
if __name__=="__main__":
	app.config.from_object(config['development'])
	#blueprint
	app.register_blueprint(movies.main,url_prefix='/api/movies')
	#agregando manejador de error
	app.register_error_handler(404,page_not_found)
	app.run()