name='mongo'
[[ $(docker ps -f "name=$name" --format '{{.Names}}') == $name ]] ||
docker run --rm -d -p 27017:27017 -v $PWD/data:/data/db --name mongo mongo
name='stanford'
[[ $(docker ps -f "name=$name" --format '{{.Names}}') == $name ]] ||
docker run -d --rm -p 9000:9000 --name stanford nlpbox/corenlp
docker run -it --rm -e mongo_ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mongo) -e stanford_ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' stanford) -v $PWD:/directory -p 5000:5000 --name legalnlp jeremycollinsmpi/legalnlp:light /bin/bash

