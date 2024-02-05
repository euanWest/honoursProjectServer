docker stop flaskapp
docker rm flaskapp
docker build -t flaskapp .
docker start flaskapp
docker run flask app -p 80:80 --name flaskapp