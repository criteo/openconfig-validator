.PHONY: build

build:
	./build.sh

clean:
	rm -rf openconfig_validator/bin

update_bindings:
	./update_bindings.sh

test:
	pytest tests/
