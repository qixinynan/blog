echo INIT SERVER WITH DEBUG="$DEBUG"
if [ "$DEBUG" = "on" ]
then
  echo STARTING DEBUG MODE
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver 0.0.0.0:8000
else
  echo STARTING PRODUCT MODE
  python3 manage.py collectstatic --noinput
  python3 manage.py makemigrations
  python3 manage.py migrate
  uwsgi --ini uwsgi.ini
fi