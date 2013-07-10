from app import app

@app.route('/')
@app.route('/home')
def home():
  return "This is the home page."