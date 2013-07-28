from flask import render_template, jsonify, request, session, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, oid
from app.models import Interval, User
import time

current_user = User.query.get(1)  # this will later be set by Flask login

def get_current_interval(category):
  current_user = User.query.get(1)
  time_machine_profile = current_user.time_machine_profile
  if category == 'build':
    if time_machine_profile.current_build is not None:
      return Interval.query.get(time_machine_profile.current_build)
    else:
      return None
  elif category == 'help':
    if time_machine_profile.current_help is not None:
      return Interval.query.get(time_machine_profile.current_help)
    else:
      return None
  elif category == 'learn':
    if time_machine_profile.current_learn is not None:
      return Interval.query.get(time_machine_profile.current_learn)
    else:
      return None
  elif category == 'love':
    if time_machine_profile.current_love is not None:
      return Interval.query.get(time_machine_profile.current_love)
    else:
      return None
  elif category == 'move':
    if time_machine_profile.current_move is not None:
      return Interval.query.get(time_machine_profile.current_move)
    else:
      return None

def set_current_interval(category, id):
  current_user = User.query.get(1)
  time_machine_profile = current_user.time_machine_profile
  if category == 'build':
    time_machine_profile.current_build = id
  elif category == 'help':
    time_machine_profile.current_help = id
  elif category == 'learn':
    time_machine_profile.current_learn = id
  elif category == 'love':
    time_machine_profile.current_love = id
  elif category == 'move':
    time_machine_profile.current_move = id

  db.session.commit()

def process_finished_interval(category, seconds):
  current_user = User.query.get(1)
  time_machine_profile = current_user.time_machine_profile
  if category == 'build':
    time_machine_profile.build_total += seconds
    time_machine_profile.current_build = None
  elif category == 'help':
    time_machine_profile.help_total += seconds
    time_machine_profile.current_help = None
  elif category == 'learn':
    time_machine_profile.learn_total += seconds
    time_machine_profile.current_learn = None
  elif category == 'love':
    time_machine_profile.love_total += seconds
    time_machine_profile.current_love = None
  elif category == 'move':
    time_machine_profile.move_total += seconds
    time_machine_profile.current_move = None
  db.session.commit()


@app.route('/switch')
def switch():
  return render_template("switch_home.html")

@app.route('/_start', methods=["POST"])
def start():
  current_user = User.query.get(1)
  time_machine_profile = current_user.time_machine_profile
  category = request.form['category']
  i = get_current_interval(category)
  if i is None:
    i = Interval(category=category, start=int(time.time()), time_machine_profile_id=time_machine_profile.id)
    db.session.add(i)
    db.session.commit()
    set_current_interval(category, time_machine_profile.intervals[-1].id)
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
    db.session.commit()
    seconds_elapsed = i.stop - i.start
    process_finished_interval(category, seconds_elapsed)
    return jsonify(data="The {0} interval was stopped.".format(category))

@app.route('/_interval_booleans')
def interval_booleans():
  intervals = {}
  categories = ['build', 'help', 'learn', 'love', 'move']
  for c in categories:
    if get_current_interval(c) is not None:
      intervals[c] = 'on'
    else:
      intervals[c] = 'off'
  return jsonify(intervals)

