docker run -p 5000\
	   --network net-tp4\
	   --name tp4-app\
	   --mount type=bind,source=$(pwd)/srv/,target=/srv\
	   im-tp4
