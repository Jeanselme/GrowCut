%module matrix

%{
	#include "matrix.h"
%}

%include "matrix.h"

%template(intMatrix) Matrix<int>;
%template(doubleMatrix) Matrix<double>;