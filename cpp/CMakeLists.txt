cmake_minimum_required(VERSION 3.20)
project(fast_ops)

set(CMAKE_CXX_STANDARD 17)

find_package(pybind11 REQUIRED)

pybind11_add_module(fast_ops bindings.cpp fast_ops.cpp)
