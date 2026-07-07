FROM python:3.9.6

# env variables
ENV DATABASE_NAME="book_store"
ENV DATABASE_HOST="postgresql://postgres:password@book_store_db"

# copy the contents of the directory to the /app folder in docker
COPY . /app
WORKDIR /app
RUN pip install -r app/requirements.txt
CMD ["python", "app.py"]

# this seeds the db, keep this command safe so i can use it again 
# cat book_store/seeds/users.sql | docker exec -i book_store_db psql -h localhost -U postgres -f-