if [ "$1" = "build" ]
then
  echo "run with build mode";
  docker-compose up
else
  echo "run with debug mode";
  docker-compose run -e DEBUG=on -p 8000:8000 app
fi