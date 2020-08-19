from app import db
from app import manager

class Noticias(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String(100))
	texto = db.Column(db.String(200))
	autor = db.Column(db.String(20))

db.create_all()
manager.create_api(Noticias, methods=['POST','GET','PUT','DELETE'])
