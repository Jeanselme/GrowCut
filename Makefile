export PY = python3.4
export PWD = $(pwd)

export AUTOMATON =Automaton/
export empty=
EXEC = main.py

all: run

run: 
	@(cd $(AUTOMATON) && $(MAKE) && cd ../ && $(PY) $(EXEC))

clean:
	@(cd $(AUTOMATON) && $(MAKE) $@)
	rm -f -d -r __pycache__