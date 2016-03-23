%module automaton
%{
	#include "matrix.h"
	#include "automaton.h"
%}

%import "matrix.i"

%include stl.i
namespace std {
	%template(IntVector) 	vector<int>;
	%template(FloatVector) 	vector<float>;
	%template(RGBVector)    vector< vector<int> >;
}

%include "automaton.h"