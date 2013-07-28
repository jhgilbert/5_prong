'''
from flask import render_template, jsonify, request, session, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, oid
from app.models import Interval, User
import time

'''

'''
@app.before_request
def lookup_current_user():
  g.user = None
  if 'openid' in session:
    g.user = User.query.filter_by(openid=openid).first()
    '''

# @lm.user_loader
# def load_user(id):
#  return User.query.get(int(id))

# @app.route('_login', methods = ['POST'])
# @oid.loginhandler
# def login():
#  session['remember_me'] = True
#  return oid.try_login('https://www.google.com/accounts/o8/id')

'''
current_user = User.query.get(1)  # this will later be set by Flask login

def get_current_interval(category):
  current_user = User.query.get(1)
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
  current_user = User.query.get(1)
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

def process_finished_interval(category, seconds):
  current_user = User.query.get(1)
  if category == 'build':
    current_user.build_total += seconds
    current_user.current_build = None
  elif category == 'help':
    current_user.help_total += seconds
    current_user.current_help = None
  elif category == 'learn':
    current_user.learn_total += seconds
    current_user.current_learn = None
  elif category == 'love':
    current_user.love_total += seconds
    current_user.current_love = None
  elif category == 'move':
    current_user.move_total += seconds
    current_user.current_move = None
  db.session.commit()


@app.route('/time_machine')
def time_machine():
  return render_template("time_machine.html")

'''
'''
@app.route('/login', methods=['GET','POST'])
@oid.loginhandler
def login():
  return oid.try_login('https://www.google.com/accounts/o8/id', ask_for['email','fullname','nickname'])
  return render_template('home.html')
'''
'''
@app.route('/_start', methods=["POST"])
def start():
  current_user = User.query.get(1)
  category = request.form['category']
  i = get_current_interval(category)
  if i is None:
    i = Interval(category=category, start=int(time.time()), user_id=current_user.id)
    db.session.add(i)
    db.session.commit()
    set_current_interval(category, current_user.intervals[-1].id)
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
  '''
