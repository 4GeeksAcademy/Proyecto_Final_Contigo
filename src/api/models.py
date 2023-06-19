from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ONG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    cif = db.Column(db.Integer(), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    url = db.Column(db.String(80), unique=True, nullable=False)
    dirección = db.Column(db.String(80), unique=False, nullable=False)
    codigo_postal = db.Column(db.Integer(), unique=False, nullable=False)
    telefono = db.Column(db.Integer(), unique=True, nullable=False)
    logo = db.Column(db.String(300), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "nombre": self.nombre,
            "cif": self.cif,
            "url": self.url,
            "dirección": self.dirección,
            "codigo_postal": self.codigo_postal,
            "telefono": self.telefono,
            "logo": self.logo
            # do not serialize the password, its a security breach
        }
    
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=False, nullable=False)
    apellido = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable=False)
    ong_id = db.Column(db.Integer, db.ForeignKey('ong.id'))

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "ong_id": self.ong_id
            # do not serialize the password, its a security breach
        }    

class Recurso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(80), db.ForeignKey('categorias.descripcion'))
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    virtual = db.Column(db.Boolean(), unique=False, nullable=False)
    dirección = db.Column(db.String(80), unique=False, nullable=True)
    codigo_postal = db.Column(db.Integer(), unique=False, nullable=True)
    telefono = db.Column(db.Integer(), unique=False, nullable=False)
    descripcion = db.Column(db.String(400), unique=True, nullable=False)
    img = db.Column(db.String(300), unique=False, nullable=True)
    fichero = db.Column(db.String(300), unique=False, nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    ong_id = db.Column(db.Integer, db.ForeignKey('ong.id'))

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "categoria": self.categoria,
            "nombre": self.nombre,
            "virtual": self.virtual,
            "direccion": self.direccion,
            "codigo_postal": self.codigo_postal,
            "telefono": self.telefono,
            "descripcion": self.descripcion,
            "img": self.img,
            "fichero": self.fichero,
            "usuario_id": self.usuario_id,
            "ong_id": self.ong_id
            # do not serialize the password, its a security breach
        }

class Categorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(20), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            # do not serialize the password, its a security breach
        }



class Peticion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=False, nullable=False)
    apellido = db.Column(db.String(80), unique=False, nullable=False)
    texto = db.Column(db.String(400), unique=False, nullable=False)
    preferencia = db.Column(db.String(20), unique=False, nullable=False)
    telefono = db.Column(db.Integer(), unique=False, nullable=True)
    email = db.Column(db.String(60), unique=False, nullable=True)
    recurso_id = db.Column(db.Integer, db.ForeignKey('recurso.id'))

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "texto": self.texto,
            "preferencia": self.preferencia,
            "telefono": self.telefono,
            "email": self.email,
            "recurso_id": self.recurso_id,
            # do not serialize the password, its a security breach
        }