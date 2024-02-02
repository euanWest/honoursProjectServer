
docker stop flaskapp
docker rm flaskapp
docker build -t flaskapp .
docker run -it -d -p 80:80 --name flaskapp