build:
	docker build -t my_flask_app .

up:
	docker compose up --build -d

down:
	docker compose down

test:
	curl -F 'file=@article.pdf' http://localhost:5000/
