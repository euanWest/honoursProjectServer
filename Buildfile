docker build -t flaskapp .
docker tag flaskapp euanWest/flaskapp
docker push euanWest/flaskapp
docker stop flaskapp
docker rm flaskapp
docker start flaskapp
docker run -p 80:80 --name flaskapp euanWest/flaskapp