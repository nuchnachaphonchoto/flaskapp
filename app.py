from flask import Flask, render_template, session, redirect, url_for, request
app = Flask(__name__)
app.secret_key = 'Hvxc45sdf56sdfsa4gyyk7G49qTbjc81xdsda'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html',username = username)
    else:
        return render_template('notlogged.html')
        
@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return render_template('login.html')

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)