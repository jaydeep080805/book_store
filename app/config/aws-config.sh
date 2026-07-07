# # move into the dir
# cd book_store

# make sure the last instance is stopped so the port isn't used
# docker stop book_store_app_container

# # delete the container
# docker container rm book_store_app_container

source .env

docker rm -f book_store_app_container

docker system prune | y

# build the docker container
docker build -t book_store .

# run the server
docker run --name book_store_app_container -p $EC2_PORT:$EC2_PORT --network book_store_network book_store