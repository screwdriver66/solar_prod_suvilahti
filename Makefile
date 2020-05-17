NAME=solar-production-suvilahti-ml
COMMIT_ID=$(shell git rev-parse HEAD)

build-ml-api-heroku:
			docker build -t registry.heroku.com/$(NAME)/web:$(COMMIT_ID) .

push-ml-api-heroku:
			docker push registry.heroku.com/${HEROKU_APP_NAME}/web:$(COMMIT_ID)
