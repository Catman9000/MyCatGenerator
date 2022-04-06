from application import db

class results(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key = True)
    cat = db.Column(db.String(50))
    treat = db.Column(db.String(50))
    def __str__(self):
        return f"{self.cat} goes {self.treat}"