SW = swig
CC = g++

SFLAG = -c++ -python
GFLAG = -O2 -fPIC -I/usr/include/$(PY)

SWIG_I = $(wildcard *.i)
WRAP = $(SWIG_I:.i=_wrap.cxx)
LIB = $(WRAP:_wrap.cxx=.so)

DEST =$(subst $(AUTOMATON),$(empty),$(PWD)/)
RES = $(addprefix $(DEST)_,$(LIB))
RES += $(addprefix $(DEST),$(SWIG_I:.i=.py))

all: $(LIB)

%.so: %.o %_wrap.o
	$(CC) -shared $^ -o $(DEST)_$@

%.so: %_wrap.o
	$(CC) -shared $< -o $(DEST)_$@

%_wrap.o: %_wrap.cxx
	$(CC) $(GFLAG) -c $< -o $@

%_wrap.cxx: %.i
	$(SW) $(SFLAG) -outdir $(DEST)  $< 

%.o: %.cc
	$(CC) $(GFLAG) -c $< -o $@

clean:
	rm -f *.o *.cxx $(RES)