pipreqs:
	pipreqs --ignore venv --force

install:
	pip3 install -r requirements.txt

run:
	FLASK_APP=app/app.py flask run --host=0.0.0.0 --port=5001 --debug