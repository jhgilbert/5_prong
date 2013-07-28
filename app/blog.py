from flask import render_template, jsonify, request, session, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, oid
from app.models import Interval, User
import time

@app.route('/')
@app.route('/home')
def home():
  return render_template('blog_home.html')

@app.route('/admin')
def admin():
  return render_template('blog_admin.html')