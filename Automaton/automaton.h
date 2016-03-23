#ifndef __AUTOMATON_H
#define __AUTOMATON_H

#include <utility>
#include <deque>
#include <vector>

#include "matrix.h"

using namespace std;

class Automaton {

private:
    // Matrix of floats which contains the strength of each pixel
    Matrix<float>  strength;
    // Matrix of ints which contains the number of loop executed 
    // on each pixel
    Matrix<int> loop;

    // Caracteristics of the image
    int height;
    int width;
    vector< vector<int> > image;

    // Queue for pixels to compute
    deque< pair<int, int> > listPoint;
    // Queue for pixels around the current computed pixel
    deque< pair<int, int> > listNeight;

public:
    // Constructor
    Automaton (int height, int width, vector< vector<int> > image)
        {
            this->height = height;
            this->width = width;

            this->image = image;

            this->strength = Matrix<float>(height, width, 0);
            this->loop = Matrix<int>(height, width, 0);
        }
    
    // Destructor
    ~Automaton() {}

    // Add the pixel in the foreground and associate the max strength
    void addForeground(const int &x, const int &y);

    // Add the pixel in the background and associate the min strength (negative max)
    void addBackground(const int &x, const int &y);

    // Remove the pixel from the queue and associate a null strength
    void erase(const int &x, const int &y);

    // Execute the growcut algorithm
    vector<float> compute(int iteration);

private:

    // Add the neighbour of the point
    void addNeighbour(const int &x, const int &y);
    
    // Add the point to the list only if it is possible
    void addIf(const int &x, const int &y);

    // Compute the coloric norm between two points
    float norm(const int &x1, const int &y1, const int &x2, const int &y2);
};

#endif
