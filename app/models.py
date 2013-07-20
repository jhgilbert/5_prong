from app import db

class Interval(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  category = db.Column(db.String(32), index=True)
  start = db.Column(db.Integer)
  stop = db.Column(db.Integer)
  running = db.Column(db.Boolean)
  note = db.Column(db.String(255))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return '<Interval {0}>'.format(self.id)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), index=True, unique=True)
  love_total = db.Column(db.Integer)
  build_total = db.Column(db.Integer)
  move_total = db.Column(db.Integer)
  learn_total = db.Column(db.Integer)
  help_total = db.Column(db.Integer)
  intervals = db.relationship('Interval', backref='intervals')

  def __repr__(self):
    return '<User {email}, ID {id}>'.format(email=self.email, id=self.id)