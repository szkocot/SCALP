from src.app import app
import config

if __name__ == '__main__':
    app.secret_key = config.CSRF_SESSION_KEY
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
