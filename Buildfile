docker stop flaskapp
docker rm flaskapp
docker build -t flaskapp .
docker start flaskapp
docker run flaskapp -p 80:80 --name flaskapp