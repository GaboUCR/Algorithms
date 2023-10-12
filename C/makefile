# Makefile for compiling LinkedList.c and creating the 'out' executable

# Compiler
CC = gcc

# Source file
SOURCE = LinkedList.c

# Executable name
OUTPUT = out

all: compile run clean

compile:
	$(CC) $(SOURCE) -o $(OUTPUT)

run: $(OUTPUT)
	./$(OUTPUT)

clean:
	rm -f $(OUTPUT)

.PHONY: all clean
