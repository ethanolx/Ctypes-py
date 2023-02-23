.PHONY: all build clean run
.SILENT: all run
CC := gcc
CCFLAGS := -shared 
EXTENSION := pyd

all: build run

run: lib.${EXTENSION}
	python .

build: lib.h lib.c
	${CC} ${CCFLAGS} lib.c -o lib.${EXTENSION}

clean:
	rm *.${EXTENSION}
