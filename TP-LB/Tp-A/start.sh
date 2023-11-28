docker build -t im-nginx-lb

mkdir shared1

mkdir shared2

mv index.html shared1

mv index.html shared2

docker run -d -p 81:80 --name nginx1 \
	--mount type=bind,source="$(pwd)"/shared1,target=/usr/share/nginx/html/ \
	nginx:latest


docker run -d -p 82:80 --name nginx2 \
        --mount type=bind,source="$(pwd)"/shared2,target=/usr/share/nginx/html/ \
        nginx:latest

docker run -d -p 83:80 --name nginx3 im-nginx-lb 


