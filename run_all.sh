#!/bin/zsh
echo 'SETTING UP VIRTUAL ENVIRONMENT AND INSTALLING REQUIREMENTS'
python3.9 -m venv venv
. venv/bin/activate
pip install -r requirements.txt > /dev/null 2>&1 &

gunicorn --bind 0.0.0.0:8080 -w 4 src.flask_app.flask_gunicorn_app:app > /dev/null 2>&1 &
echo 'TESTING FLASK + GUNICORN'
python manage.py --server 'Gunicorn/Flask' --port 8080
./kill_pyserver.sh 8080 gunicorn
./kill_process_named.sh Gunicorn

sleep 5

uvicorn --host 0.0.0.0 --port 8081 --workers 4 src.fastapi_app.fastapi_uvicorn_app:app > /dev/null 2>&1 &
echo 'TESTING UVICORN + FASTAPI'
python manage.py --server 'Uvicorn/FastAPI' --port 8081
./kill_pyserver.sh 8081 uvicorn
./kill_process_named.sh Uvicorn
