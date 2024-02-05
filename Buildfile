
docker stop flaskapp
docker rm flaskapp
docker build -t flaskapp .
docker start flaskapp -a
docker run -p 80:80 --name flaskapp