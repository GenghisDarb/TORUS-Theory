# Recursion-Based Side-Band Prediction in a Nutshell

## What Are Recursion-Induced Side-Bands?

In structured optical or atomic interference systems described by the TORUS theory, the emergence of side-bands in the Fourier spectrum of pair-correlation functions is predicted. These side-bands result from the recursion-based structure of the system. The most notable side-band appears at $k_1 = k_0(1+1/14)$, where $k_0$ is the primary spatial frequency.

---

## 1. Physical Intuition

The TORUS theory suggests that in systems with recursive symmetry, the fundamental spatial frequency $k_0$ is accompanied by harmonics and side-bands at regular intervals. The side-band at $k_1 = k_0(1+1/14)$ is particularly significant as it corresponds to the 14-layer closure of the TORUS recursion.

- **$k_0$**: Primary spatial frequency (e.g., lattice or Talbot period)
- **$k_1$**: Side-band frequency, as predicted by the recursion

The presence of this side-band serves as a hallmark of the recursive structure inherent in TORUS, distinguishing it from non-recursive systems.

---

## 2. Mathematical Derivation

Consider the pair-correlation function $g^{(2)}(r)$ of a spatial point process, such as the positions of atoms or the detections of photons. The Fourier transform of this function, $G^{(2)}(k)$, exposes the dominant spatial frequencies within the system.

### 2.1. Fourier Transform of Pair Correlation

The Fourier transform is given by:

$$
G^{(2)}(k) = \int g^{(2)}(r) e^{-ikr} dr
$$

For structures that are periodic or quasi-periodic, $G^{(2)}(k)$ will typically show a peak at the primary frequency $k_0$. However, due to the effects of recursion in TORUS, a secondary peak emerges at

$$
k_1 = k_0 \left(1 + \frac{1}{14}\right)
$$

### 2.2. Side-Band Amplitude

The relative amplitude of the side-band, denoted as $A_1$, compared to the main peak $A_0$, is generally small but can be reliably detected. For instance, in synthetic data, a common injected amplitude for the side-band is 7% of that of the main peak:

$$
A_1 = 0.07 \times A_0
$$

### 2.3. Detection Criterion

To identify the presence of the side-band, we analyze the power spectrum defined as $P(k) = |G^{(2)}(k)|^2$. The metric for detection is

$$
\Delta P = 10 \log_{10} \left( \frac{P(k_1)}{P(k_0)} \right )
$$

A system is considered TORUS-POSITIVE if it exhibits a $\Delta P$ value in the range of $-45 < \Delta P < -25$ dB.

---

## 3. Practical Detection Pipeline

The following steps outline the process for detecting the predicted side-band in experimental or simulated data:

1. **Collect (x, y) snapshots** of the system under investigation.
2. **Compute $g^{(2)}(r)$** by analyzing and binning the pairwise distances between points.
3. **Fourier transform** the computed $g^{(2)}(r)$ to obtain $G^{(2)}(k)$.
4. **Identify $k_0$** (the location of the main peak) and $k_1$ (the location of the side-band).
5. **Calculate $\Delta P$** and evaluate it against the detection criterion.

---

## 4. Example SVG Figure

The following SVG graphic illustrates a typical power spectrum showing both the main peak and the side-band:

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
