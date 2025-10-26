from db import Base, engine
from auth.models import User
from tasks.models import Task


print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
