from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_deleted = db.Column(db.Integer, default=0)

class Expense(db.Model):
    __tablename__ = "expense"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

    amount = db.Column(db.Float, nullable=False)
    
    description = db.Column(db.String(512), default="")
    expense_date = db.Column(db.Date, nullable=False)
    is_deleted = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.relationship("Category", backref="expenses")
    
    @validates('amount')
    def validate_amount(self, key, value):
        if value is None or str(value).strip() == "":
            raise ValueError("Amount cannot be empty.")
        try:
            return float(value)
        except ValueError:
            raise ValueError("Amount must be a valid number.")