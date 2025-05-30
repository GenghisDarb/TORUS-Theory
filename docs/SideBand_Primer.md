# Recursion-Based Side-Band Prediction: A Primer

## Introduction

The TORUS Theory predicts the emergence of side-bands in the Fourier spectrum of pair-correlation functions due to its recursion-based structure. This primer explains the physical intuition, mathematical derivation, and practical detection of the side-band, focusing on the prediction at $k_1 = k_0(1+1/14)$, where $k_0$ is the primary spatial frequency.

---

## 1. Physical Intuition

In a system with recursive symmetry, such as those described by TORUS, the fundamental spatial frequency $k_0$ is not isolated. Instead, the recursive structure induces harmonics and side-bands at predictable offsets. The most robust and universal of these is the side-band at $k_1 = k_0(1+1/14)$, corresponding to the 14-layer closure of the TORUS recursion.

- **$k_0$**: Primary spatial frequency (e.g., lattice or Talbot period)
- **$k_1$**: Side-band frequency predicted by recursion

The side-band is a direct signature of the recursive closure and is not expected in non-recursive (random or classical) systems.

---

## 2. Mathematical Derivation

Let $g^{(2)}(r)$ be the pair-correlation function of a spatial point process (e.g., atom positions, photon detections). Its Fourier transform $G^{(2)}(k)$ reveals dominant spatial frequencies.

### 2.1. Fourier Transform of Pair Correlation

$$
G^{(2)}(k) = \int g^{(2)}(r) e^{-ikr} dr
$$

For a periodic or quasi-periodic structure, $G^{(2)}(k)$ has a peak at $k_0$. In TORUS, recursion modifies the structure so that a secondary peak appears at

$$
k_1 = k_0 \left(1 + \frac{1}{14}\right)
$$

### 2.2. Side-Band Amplitude

The amplitude of the side-band, $A_1$, relative to the main peak $A_0$, is predicted to be small but robust. For synthetic data, a typical injected amplitude is 7%:

$$
A_1 = 0.07 \times A_0
$$

### 2.3. Detection Criterion

Define the power spectrum $P(k) = |G^{(2)}(k)|^2$. The detection metric is

$$
\Delta P = 10 \log_{10} \left( \frac{P(k_1)}{P(k_0)} \right )
$$

A value of $-45 < \Delta P < -25$ dB is considered TORUS-POSITIVE.

---

## 3. Practical Detection Pipeline

1. **Collect (x, y) snapshots** of the system.
2. **Compute $g^{(2)}(r)$** by binning pairwise distances.
3. **Fourier transform** $g^{(2)}(r)$ to obtain $G^{(2)}(k)$.
4. **Locate $k_0$** (main peak) and $k_1$ (side-band).
5. **Compute $\Delta P$** and apply the detection criterion.

---

## 4. Example SVG Figure

Below is a schematic SVG showing the main peak and side-band in the power spectrum:

```svg
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" fill="#fff"/>
  <polyline points="0,180 50,120 100,60 150,40 200,60 250,120 300,180 350,190 400,200" fill="none" stroke="#888" stroke-width="2"/>
  <rect x="140" y="40" width="20" height="140" fill="#4a90e2"/>
  <rect x="180" y="100" width="10" height="80" fill="#e94e77"/>
  <text x="150" y="35" font-size="14" fill="#4a90e2">k₀</text>
  <text x="185" y="95" font-size="14" fill="#e94e77">k₁</text>
  <text x="10" y="20" font-size="16" fill="#333">Power Spectrum |G²(k)|²</text>
  <text x="320" y="195" font-size="12" fill="#333">k</text>
</svg>
```

---

## 5. References

- [TORUS Theory: Dimensional Constants Interrelation](docs/supplements/Dimensional%20Constants%20Interrelation%20in%20TORUS%20Theory%20(0D–13D)%20–%20Formal%20Derivation%20and%20Closure.pdf)
- [Talbot Carpet Data: Zenodo DOI 10.5281/zenodo.3382197](https://zenodo.org/record/3382197)
- [Pair Correlation Analysis in Quantum Gases](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.98.030406)
