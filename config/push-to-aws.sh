# echo "test"

# copy the contents locally to the aws server
scp -r -i ~/.ssh/jaydeep_cloud_deployment.pem \
*.py lib requirements.txt Dockerfile seeds templates static config \
ec2-user@52.56.152.77:~/book_store # this makes sure its sent to the book store

# connect to the aws server
# ssh -i ~/.ssh/jaydeep_cloud_deployment.pem ec2-user@52.56.152.77 


# the first EOF is to tell shell to keep reading until it reaches the EOF line
# essentially replacing {} in programming languages
ssh -i ~/.ssh/jaydeep_cloud_deployment.pem ec2-user@52.56.152.77 << EOF
    cd book_store
    bash config/aws-config.sh
EOF
