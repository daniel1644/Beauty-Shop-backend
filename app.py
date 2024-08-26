# app.py
from app import create_app
# from dotenv import load_dotenv
# load_dotenv()

app = create_app('development')

if __name__ == "__main__":
    app.run(port=5555, debug=True)