#include <vector>
#include <cmath>

double fast_amplitude(const std::vector<double>& params) {
    double sum = 0.0;
    for (auto v : params) sum += v;
    double denom = params.size() + 1.0;
    return std::tanh(sum / denom);
}
