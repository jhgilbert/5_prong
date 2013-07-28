from app import db

# Basic user model for generic purposes

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), index=True, unique=True)
  time_machine_profile = db.relationship('TimeMachineProfile', uselist=False, backref="time_machine_profile")

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    return unicode(self.id)

  def __repr__(self):
    return '<User {email}, ID {id}>'.format(email=self.email, id=self.id)

# Models for blog

class BlogPost(db.Model):
  __tablename__ = 'blog_post'
  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.Integer)
  published_on = db.Column(db.Integer)
  live = db.Column(db.Boolean)
  title = db.Column(db.String(255))
  body = db.Column(db.Text)

# Time Machine models

class TimeMachineProfile(db.Model):
  __tablename__ = 'time_machine_profile'
  id = db.Column(db.Integer, primary_key=True)
  current_build = db.Column(db.Integer)
  current_help = db.Column(db.Integer)
  current_learn = db.Column(db.Integer)
  current_love = db.Column(db.Integer)
  current_move = db.Column(db.Integer)
  build_total = db.Column(db.Integer, default=0)
  help_total = db.Column(db.Integer, default=0)
  learn_total = db.Column(db.Integer, default=0)
  love_total = db.Column(db.Integer, default=0)
  move_total = db.Column(db.Integer, default=0)
  intervals = db.relationship('Interval', backref="intervals")
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Interval(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  category = db.Column(db.String(32), index=True)
  start = db.Column(db.Integer)
  stop = db.Column(db.Integer)
  elapsed = db.Column(db.Integer)
  note = db.Column(db.String(255))
  time_machine_profile_id = db.Column(db.Integer, db.ForeignKey('time_machine_profile.id'))

  def __repr__(self):
    return '<Interval {0}>'.format(self.id)