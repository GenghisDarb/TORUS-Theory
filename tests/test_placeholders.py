def test_echo_functions():
    import numpy as np
    from notebooks.gwd.LIGO_Echo_Torus_vs_T_HET import torus_echo, thet_echo
    assert abs(torus_echo(np.array([0]))[0]) < 1e-6
