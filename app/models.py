from app import db

class Interval(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  category = db.Column(db.String(32), index=True)
  start = db.Column(db.Integer)
  stop = db.Column(db.Integer)
  elapsed = db.Column(db.Integer)
  note = db.Column(db.String(255))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return '<Interval {0}>'.format(self.id)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), index=True, unique=True)
  build_total = db.Column(db.Integer, default=0)
  help_total = db.Column(db.Integer, default=0)
  learn_total = db.Column(db.Integer, default=0)
  love_total = db.Column(db.Integer, default=0)
  move_total = db.Column(db.Integer, default=0)
  current_build = db.Column(db.Integer)
  current_help = db.Column(db.Integer)
  current_learn = db.Column(db.Integer)
  current_love = db.Column(db.Integer)
  current_move = db.Column(db.Integer)
  intervals = db.relationship('Interval', backref='intervals')

  def __repr__(self):
    return '<User {email}, ID {id}>'.format(email=self.email, id=self.id)