IMAGE := devops-projects
PORT := 5000

.PHONY: build run test shell clean

build:
	docker build -t $(IMAGE) .

run:
	docker run --rm -p $(PORT):$(PORT) $(IMAGE)

test:
	docker run --rm $(IMAGE) python3 -m pytest

shell:
	docker run --rm -it $(IMAGE) /bin/bash

clean:
	-docker rmi $(IMAGE)
