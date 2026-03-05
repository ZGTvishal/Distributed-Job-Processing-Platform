from db.session import engine
from db.base import Base

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done")