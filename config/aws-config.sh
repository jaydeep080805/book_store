# # move into the dir
# cd book_store

# make sure the last instance is stopped so the port isn't used
# docker stop book_store_app_container

# # delete the container
# docker container rm book_store_app_container

docker rm -f book_store_app_container

# build the docker container
docker build -t book_store .

# run the server
docker run --name book_store_app_container -p 5001:5001 --network book_store_network book_store