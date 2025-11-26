#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
double fast_amplitude(const std::vector<double>& params);

namespace py = pybind11;

PYBIND11_MODULE(fast_ops, m) {
    m.def("fast_amplitude", &fast_amplitude, "Compute amplitude quickly");
}
