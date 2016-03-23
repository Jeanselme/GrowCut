#include "automaton.h"
#include <iostream>
#include <math.h>

void Automaton::addForeground(const int &x, const int &y) {
    strength.change(x,y,1.);
    loop.increase(x,y);
    listPoint.push_back(make_pair(x,y));
}

void Automaton::addBackground(const int &x, const int &y) {
    strength.change(x,y,-1.);
    loop.increase(x,y);
    listPoint.push_back(make_pair(x,y));
}

void Automaton::erase(const int &x, const int &y){
    strength.change(x,y,0.);
    loop.change(x,y,0);
    for(deque< pair<int, int> >::iterator i = listPoint.begin(); i != listPoint.end(); ++i) {
        if (i->first == x && i->second == y) {
            listPoint.erase(i);
            break;
        }
    }
}

void Automaton::addNeighbour(const int &x, const int &y){
    addIf(x-1,y);
    addIf(x-1,y-1);
    addIf(x-1,y+1);
    addIf(x+1,y);
    addIf(x+1,y-1);
    addIf(x+1,y+1);
    addIf(x,y-1);
    addIf(x,y+1);
}

void Automaton::addIf(const int &x, const int &y){
    if (0 <= x && x < width && 0 <= y && y < height) {
        if (loop(x,y) == 0) {
            // Point is not computed for now (strength = 0.0)
            listPoint.push_back(make_pair(x,y));
            loop.increase(x,y);
        } else {
            listNeight.push_back(make_pair(x,y));
        }
    }
}

vector<float> Automaton::compute(int iteration) {
    loop = Matrix<int>(height, width, 0);
    // Loop while it remains points to compute
    while ((!listPoint.empty())) {
        pair<int, int> point = listPoint.front();

        int point_x = point.first;
        int point_y = point.second;

        addNeighbour(point_x,point_y);

        // Compute the strength of the current point
        while (! listNeight.empty()) {
            pair<int, int> neight = listNeight.front();
            
            int neight_x = neight.first;
            int neight_y = neight.second;

            float n = norm(point_x, point_y, neight_x, neight_y);

            if (n*(fabs(strength(neight_x, neight_y))) > fabs(strength(point_x, point_y))) {
                strength.change(point_x, point_y, n*strength(neight_x, neight_y));
            } else if (fabs(n*(strength(point_x, point_y))) > fabs(strength(neight_x, neight_y))) {
                if (strength(point_x, point_y)*strength(neight_x, neight_y) < 0 && loop(neight_x, neight_y) < iteration) {
                    listPoint.push_back(make_pair(neight_x, neight_y));
                    loop.increase(neight_x, neight_y);
                }
            }
            listNeight.pop_front();
        }
        listPoint.pop_front();
    }
    return strength.getData();
}

float Automaton::norm(const int &x1, const int &y1, const int &x2, const int &y2) {
    int pixel = (y1*width) + x1;
    vector<int> RGB1 = image[pixel];

    pixel = (y2*width) + x2;
    vector<int> RGB2 = image[pixel];

    int R = RGB1[0] - RGB2[0];
    int G = RGB1[1] - RGB2[1];
    int B = RGB1[2] - RGB2[2];

    return 1. - (sqrt(pow(R,2) + pow(G,2) + pow(B,2))/(sqrt(3)*255));
}

