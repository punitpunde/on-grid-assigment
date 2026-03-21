import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("MYSQL_USER"))
print(os.getenv("MYSQL_PASSWORD"))
print(os.getenv("MYSQL_HOST"))
print(os.getenv("MYSQL_DATABASE"))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('MYSQL_USER', 'root')}:"
        f"{os.getenv('MYSQL_PASSWORD', 'root')}@"
        f"{os.getenv('MYSQL_HOST', '127.0.0.1')}:"
        f"{os.getenv('MYSQL_PORT', '3306')}/"
        f"{os.getenv('MYSQL_DATABASE', 'expense_tracker')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
