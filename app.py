from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is the about page.'
@app.route('/pypy')
def pypy():
    return '我的下面很大'

if __name__ == '__main__':
    app.run(debug=True)
