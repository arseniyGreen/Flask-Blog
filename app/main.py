from flask import Flask, render_template

site = Flask(__name__)
site.config.from_object('config')

@site.route('/')
@site.route('/index')
def index():
    user = { 'nickname' : 'arseniy' }

    posts = [
        {
            'author': {'nickname' : 'Arseniy Arkadskov'},
            'body': 'Hello from my blog!'
        },
        {
            'author': {'nickname' : 'Diana Repina'},
            'body' : "My amazing post!"
        }
    ]

    return render_template("index.html",
                           title = "Home",
                           user=user,
                           posts = posts)


if __name__ == '__main__':
    site.run()