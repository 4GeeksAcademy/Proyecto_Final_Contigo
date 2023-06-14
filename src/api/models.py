from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ONG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    cif = db.Column(db.Integer(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    url = db.Column(db.String(80), unique=True, nullable=False)
    dirección = db.Column(db.String(80), unique=False, nullable=False)
    codigo_postal = db.Column(db.Integer(5), unique=False, nullable=False)
    telefono = db.Column(db.Integer(15), unique=True, nullable=False)
    logo = db.Column(db.String(300), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=False, nullable=False)
    apellido = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable=False)
    ong_id = db.Column(db.Integer, db.ForeignKey('ONG.id'))

class Recurso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(50), db.ForeignKey('Categoria.id'))
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    modalidad = db.Column(db.String(20), db.ForeignKey('Modalidad.id'))
    dirección = db.Column(db.String(80), unique=False, nullable=True)
    codigo_postal = db.Column(db.Integer(5), unique=False, nullable=True)
    telefono = db.Column(db.Integer(15), unique=False, nullable=False)
    descripcion = db.Column(db.String(400), unique=True, nullable=False)
    img = db.Column(db.String(300), unique=False, nullable=True)
    fichero = db.Column(db.String(300), unique=False, nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'))
    ong_id = db.Column(db.Integer, db.ForeignKey('ONG.id'))

class Categorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(20), unique=True, nullable=False)

class Modalidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(20), unique=True, nullable=False)    


class Peticion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=False, nullable=False)
    apellido = db.Column(db.String(80), unique=False, nullable=True)
    texto = db.Column(db.String(400), unique=False, nullable=False)
    preferencia = db.Column(db.String(20), unique=False, nullable=False)
    telefono = db.Column(db.Integer(50), unique=False, nullable=True)
    email = db.Column(db.String(60), unique=True, nullable=True)
    recurso_id = db.Column(db.Integer, db.ForeignKey('Recurso.id'))
