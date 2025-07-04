import math, torus_cli

def test_fourteen_cycle_identity():
    ident = torus_cli.recursion_closure_demo()  # write helper if absent
    assert math.isclose(ident, 1.0, rel_tol=1e-9)
