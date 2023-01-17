from app import create_app
from console import create_manager

app = create_app()
manager = create_manager(app)

if __name__ == '__main__':
    manager.run()
