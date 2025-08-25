from flask import Flask
from routes.tasks import tasks_bp

def create_app():
    app = Flask(__name__)
    
    # đăng ký blueprint
    app.register_blueprint(tasks_bp, url_prefix="/api/tasks")
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
#cicd test