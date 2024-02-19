from app.utils.database import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, primary_key=False)
    
    def as_dict(self):
        return {
                'id': self.id, 
                'name': self.name, 
                'age': self.age
                }