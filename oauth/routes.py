from oauth import oauth
@oauth.route('/')
@oauth.route('/index')
def index():
    return "Streaming Google Authenticator"
