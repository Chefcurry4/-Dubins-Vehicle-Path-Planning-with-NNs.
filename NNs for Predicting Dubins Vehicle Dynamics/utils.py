import numpy as np

def getInitialState(inf_box, sup_box, size):

    a_samples = np.random.uniform(inf_box, sup_box, size)
    b_samples = np.random.uniform(inf_box, sup_box, size)
    c_samples = np.random.uniform(inf_box, sup_box, size)
    
    samples = np.column_stack((a_samples, b_samples, c_samples))
    return samples


def systemDynamics(x, params):
    h = params[0]
    v = params[1]
    u = params[2]

    component_1 = x[:, 0] + h * v * np.sin(x[:, 2])
    component_2 = x[:, 1] + h * v * np.cos(x[:, 2])
    component_3 = x[:, 2] + h * u

    return np.column_stack((component_1, component_2, component_3))