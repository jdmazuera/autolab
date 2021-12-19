import argparse
import uuid
import pandas as pd
from werkzeug.security import generate_password_hash
from app import db, create_app
from app.auth.models import Users

class CreateUserController:
    
    def __init__(self, username, password):
        self.db_session = db.session
        self.username = username
        self.password = password

    def run_process(self):
        hashed_password = generate_password_hash(self.password, method='sha256')
        new_user = Users(public_id=str(uuid.uuid4()), name=self.username, password=hashed_password, admin=False) 
        self.db_session.add(new_user)  
        self.db_session.commit()

def get_parameters():
    parser = argparse.ArgumentParser("scripts.create_user")
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    args = parser.parse_args()
    return vars(args)

if __name__ == "__main__":
    try:
        app = create_app()
        with app.app_context():
            params = get_parameters()
            process = CreateUserController(**params)
            process.run_process()
    except IndexError as e:
        print(e)
        raise e
    except Exception as e:
        print(e)
        raise e