from app import create_app, db
from sqlalchemy.sql import text  # Import the text function for raw SQL

app = create_app()

with app.app_context():
    try:
        # Test database connection using `engine.connect`
        with db.engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))  # Use `text` for the query
            for row in result:
                print("Database connection successful! Test query result:", row)
    except Exception as e:
        print("Database connection failed:", e)
