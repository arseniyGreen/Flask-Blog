from main import site

@site.route('/')
def start():
    return 'Hello world!'

@site.route('/index')
def index():
    return 'Hello world!'