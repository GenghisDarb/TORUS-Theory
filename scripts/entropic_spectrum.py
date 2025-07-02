import numpy as np

def thet_tt(ell, *, alpha=0.07, beta=1.8, l_damp=250):
    """Entropic-modal T-HET TT power spectrum (normalized to μK²)."""
    # Baseline envelope ~ Planck first peak
    env = 6000 * np.exp(-0.00025*(ell-220)**2)
    # Entropic damping & phase modulation
    osc = 1 + alpha * np.sin(beta * np.log(ell/l_damp))
    return env * osc
