#ifndef __MATRIX_H
#define __MATRIX_H

#include <vector>
#include <iostream>

template<class type>
class Matrix {
    private:
        int row;
        int col;
        std::vector<type> data;

    public:
        Matrix() {}

        Matrix(int row, int col, type init){
            this->row = row;
            this->col = col;
            this->data.assign(row * col, init);
        }

        void change(const int &x, const int &y, const type &value) {
            data[y * col + x] = value;
        }
        
        void increase(const int &x, const int &y) {   
            data[y * col + x] ++;
        }

        type &operator()(const int &x, const int &y) {
            return data[y * col + x];
        }

        void _print() {
            for (int i = 0; i < row; ++i)
            {
                for (int j = 0; j < col; ++j)
                {
                    std::cout << data[i * col + j];
                }
                std::cout << std::endl;
            }
        }

        std::vector<type> getData() {
            return data;
        }
};

#endif