from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
boostrap = Bootstrap5(app)
# route decorator binds a function to a URL
# https://github.com/TunedTuna/cst205/blob/main/lab15_w10_flask1.py
@app.route('/')
def hello():
  
  return '''
        <p>Anthony: GG </p>
        <p>Flavio : BRB </p>
        <p>James: AFK </p>

        '''
@app.route('/templates')
def t_test():
  return render_template('rodas.html')