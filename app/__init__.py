from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/index')
    def index():
        user = {'username': 'Tae'}
        return render_template('index.html', title='Home', user=user)
    # def hello():
    #     return "Hello World!"

    @app.route('/test')
    def bootstrap_index():
        user = {'username': 'Tae'}
        return render_template('bootstrap.html', title='Home', user=user, bootstrap=bootstrap)

    return app
