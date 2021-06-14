from flask import Flask, render_template


mApp = Flask(__name__)

@mApp.route('/')
def index():
    return render_template('index.html')


if __name__=='__main__':
    mApp.run(debug=True)