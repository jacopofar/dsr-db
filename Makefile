.PHONY: generate_slides
generate_slides:
	@echo "Generating Docker slides..."
	cd docker && npm install && npm run export
	cp docker/slides-export.pdf slides_docker.pdf
	@echo "Generating nosql slides..."
	cd nosql_data && npm install && npm run export
	cp nosql_data/slides-export.pdf slides_nosql.pdf