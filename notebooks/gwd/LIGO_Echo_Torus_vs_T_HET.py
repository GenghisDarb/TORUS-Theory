"""Module for LIGO Echo Torus vs T-HET analysis."""

from typing import Dict, Any
import numpy as np
from scipy.signal import filtfilt, welch
from gwd._prep import _safe_butter


def _prep(
    strain: np.ndarray, fs: float, fl: float = 20.0, fh: float = 1024.0
) -> np.ndarray:
    """Simple time-domain whitening & Butterworth band-pass."""
    try:
        # Ensure frequencies are normalized and within valid range
        nyquist = fs / 2
        low = fl / nyquist
        high = fh / nyquist

        if not (0 < low < 1 and 0 < high < 1):
            raise ValueError(
                "Filter frequencies must be between 0 and Nyquist frequency."
            )

        # Debugging statements to inspect values
        print(f"Low cutoff frequency: {low}")
        print(f"High cutoff frequency: {high}")
        print(f"Strain array shape: {strain.shape}")

        # Validate frequency range before passing to butter
        if not isinstance(low, float) or not isinstance(high, float):
            raise TypeError("Cutoff frequencies must be floats.")

        # Debugging Butterworth filter inputs
        print(f"Calling butter with: order=4, frequencies={[low, high]}, btype='band'")

        # Corrected Butterworth filter implementation
        try:
            b, a = _safe_butter(low=low, high=high, fs=fs, order=4)
            print(f"Butterworth filter coefficients: b={b}, a={a}")
        except Exception as butter_error:
            print(f"Error in butter function: {butter_error}")
            raise

        bp = filtfilt(b, a, strain)
        f, Pxx = welch(bp, fs, nperseg=int(fs * 2))
        psd = np.interp(np.fft.rfftfreq(len(bp), 1 / fs), f, Pxx)
        w = np.fft.irfft(np.fft.rfft(bp) / np.sqrt(psd))
        return w
    except Exception as e:
        print(f"Error in Butterworth filter: {e}")
        return np.zeros_like(strain)


############################################
# TORUS echo – structured 1/14 harmonic search
############################################
def torus_echo(
    strain: np.ndarray,
    fs: float,
    merger_time: float,
    tau_base: float,
    snr_thresh: float = 5.0,
) -> Dict[str, Any]:
    """
    Detect TORUS-predicted echoes:   τ_k = (tau_base/14) * k   (k = 1,2,…)
    Parameters
    ----------
    strain : array
        Whitened strain centred on the merger event.
    fs : float
        Sample rate (Hz).
    merger_time : float
        Index (s) of t=0 merger peak in 'strain'.
    tau_base : float
        Base recursion period τ (s) returned by ringdown fit.
    """
    w = _prep(strain, fs)
    nt = len(w)
    t = np.arange(nt) / fs - merger_time

    # build template sum of decaying sinusoids at harmonic delays
    template = np.zeros_like(w)
    for k in range(1, 8):  # first 7 harmonics
        delay = (tau_base / 14) * k
        idx = int(round((delay + merger_time) * fs))
        if 0 <= idx < nt:
            template[idx:] += np.exp(-(t[idx:] / 0.02)) * np.sin(
                2 * np.pi * 150 * t[idx:]
            )

    snr = np.dot(w, template) / np.linalg.norm(template)
    verdict = "TORUS-POSITIVE" if snr >= snr_thresh else "TORUS-NEGATIVE"
    return dict(
        snr=snr,
        verdict=verdict,
        tau_base=tau_base,
        template_norm=np.linalg.norm(template),
    )


############################################
# T-HET echo – entropic boundary model
############################################
def thet_echo(
    strain: np.ndarray,
    fs: float,
    R_km: float,
    epsilon: float = 1e-3,
    snr_thresh: float = 5.0,
) -> Dict[str, Any]:
    """
    Implements τ_echo = 2 R ln(1/ε)  (T-HET Eq. ~70).
    R in kilometres; ε is dimensionless boundary parameter.
    """
    tau_echo = 2 * (R_km * 1e3) * np.log(1 / epsilon) / 3e8  # convert km→m, c≈3e8
    w = _prep(strain, fs)
    nt = len(w)
    t = np.arange(nt) / fs

    # damped-sinusoid echo template
    delay_idx = int(round(tau_echo * fs))
    template = np.zeros_like(w)
    if delay_idx < nt:
        template[delay_idx:] = np.exp(-(t[: nt - delay_idx] / 0.03)) * np.sin(
            2 * np.pi * 150 * t[: nt - delay_idx]
        )

    snr = np.dot(w, template) / np.linalg.norm(template)
    verdict = "T-HET-POSITIVE" if snr >= snr_thresh else "T-HET-NEGATIVE"
    return dict(snr=snr, verdict=verdict, tau_echo=tau_echo)


# -------------------------------------------------------------------------
# Example stub for a CLI entry-point
if __name__ == "__main__":
    print("Module imported; integrate with LIGO strain loader elsewhere.")
