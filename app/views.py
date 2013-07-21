from app import app, db
from app.models import Interval, User
from flask import render_template, jsonify, request
import time

current_user = User.query.get(1)  # this will later be set by Flask login

def get_current_interval(category):
  if category == 'build':
    if current_user.current_build is not None:
      return Interval.query.get(current_user.current_build)
    else:
      return None
  elif category == 'help':
    if current_user.current_help is not None:
      return Interval.query.get(current_user.current_help)
    else:
      return None
  elif category == 'learn':
    if current_user.current_learn is not None:
      return Interval.query.get(current_user.current_learn)
    else:
      return None
  elif category == 'love':
    if current_user.current_love is not None:
      return Interval.query.get(current_user.current_love)
    else:
      return None
  elif category == 'move':
    if current_user.current_move is not None:
      return Interval.query.get(current_user.current_move)
    else:
      return None

def set_current_interval(category, id):
  if category == 'build':
    current_user.current_build = id
  elif category == 'help':
    current_user.current_help = id
  elif category == 'learn':
    current_user.current_learn = id
  elif category == 'love':
    current_user.current_love = id
  elif category == 'move':
    current_user.current_move = id
  db.session.commit()

def update_elapsed(category, seconds):
  if category == 'build':
    current_user.build_total += seconds
  elif category == 'help':
    current_user.help_total += seconds
  elif category == 'learn':
    current_user.learn_total += seconds
  elif category == 'love':
    current_user.love_total += seconds
  elif category == 'move':
    current_user.move_total += seconds
  db.session.commit()


@app.route('/')
@app.route('/home')
def home():
  return render_template("home.html")

@app.route('/_start', methods=["POST"])
def start():
  category = request.form['category']
  i = get_current_interval(category)
  if i is None:
    i = Interval(category=category, start=int(time.time()), user_id=current_user.id)
    db.session.add(i)
    db.session.commit()
    set_current_interval(category, i.id)
    return jsonify(data="A new {0} interval has been started.".format(category))
  else:
    return jsonify(data="A {0} interval was already running.".format(category))

@app.route('/_stop', methods=["POST"])
def stop():
  category = request.form['category']
  i = get_current_interval(category)
  if i is None:
    return jsonify(data="No {0} interval is running.".format(category))
  else:
    i.stop = int(time.time())
    seconds_elapsed = i.stop - i.start
    update_elapsed(category, seconds_elapsed)
    return jsonify(data="The {0} interval was stopped.".format(category))



