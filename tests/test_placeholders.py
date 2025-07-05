def test_echo_functions():
    import sys
    sys.path.append("./notebooks/gwd")
    from LIGO_Echo_Torus_vs_T_HET import torus_echo, thet_echo
    assert torus_echo() == "Placeholder for torus echo computation"
    assert thet_echo() == "Placeholder for T-HET echo computation"
