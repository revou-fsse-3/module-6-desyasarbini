from app.utils.database import db

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.Integer, primary_key=True)
    
    def as_dict(self):
        return {
                'id': self.id, 
                'name': self.name, 
                'birthdate': self.birthdate
                }