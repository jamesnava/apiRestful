from decouple import config

class Config:
	SECRE_KEY=config('SECRET_KEY')

class DevelopmentConfig(Config):
	DEBUG=True
	
config={
'development':DevelopmentConfig
	}