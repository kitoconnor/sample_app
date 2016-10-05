from flask import Flask, render_template

#this is essentially creating a new app
app = Flask(__name__)

#creating the homepage (group browse)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)

