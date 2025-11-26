def clamp_params(values, low=0.0, high=1000.0):
    return [max(low, min(high, v)) for v in values]
