---
layout: post
title: Learning notes (Draft)
categories: cheatsheet
---
ns may remain terse. Analogy is often employed to comphrehend the concept. The documentation is not meant to be used as a tutorial. The content is updated regularly as I am taking physics and materials science courses at Columbia University.

## To do

- To-do add 1D, 2D, 3D DOS derivation for free electron metals

## Table of contents

- [To do](#to-do)
- [Table of contents](#table-of-contents)
- [Electrons (Spring 2024, MSAE4203)](#electrons-spring-2024-msae4203)
  - [Classical mechanics](#classical-mechanics)
    - [Hamiltonian function](#hamiltonian-function)
    - [Force and motion](#force-and-motion)
    - [Recover kinematics from Hamiltonian](#recover-kinematics-from-hamiltonian)
    - [Equation of motion for any observable](#equation-of-motion-for-any-observable)
  - [1D particle in a box](#1d-particle-in-a-box)
  - [Space and momentum representation (Not finished)](#space-and-momentum-representation-not-finished)
- [Condensed Matter Physics (Spring 2024, PHYS6057)](#condensed-matter-physics-spring-2024-phys6057)
- [Electronic \& Magnetic Properties of Solids (Fall 2023, MSAE 4206)](#electronic--magnetic-properties-of-solids-fall-2023-msae-4206)
  - [Fermi energy](#fermi-energy)
    - [Energy scale](#energy-scale)
    - [Implication for lattice distortion](#implication-for-lattice-distortion)
    - [Implication for electrical conductivity](#implication-for-electrical-conductivity)
  - [Importance of symmetry](#importance-of-symmetry)
    - [How to detect symmetry breaking](#how-to-detect-symmetry-breaking)
  - [Density of states](#density-of-states)
    - [What is state?](#what-is-state)
    - [Why is volume relevant?](#why-is-volume-relevant)
    - [Total number of states per unit volume](#total-number-of-states-per-unit-volume)
  - [Quantum gas](#quantum-gas)
- [Materials Thermodynamics and Phase Diagrams (Fall 2023)](#materials-thermodynamics-and-phase-diagrams-fall-2023)
  - [Maxwell-Boltzmann distribution](#maxwell-boltzmann-distribution)
    - [Formula](#formula)
    - [Average velocity](#average-velocity)
- [Kinetics](#kinetics)
- [Phonons](#phonons)
- [Electrons - Writing a draft](#electrons---writing-a-draft)
  - [Basic notations](#basic-notations)
    - [Delta function](#delta-function)
    - [Position representation in continous basis](#position-representation-in-continous-basis)
    - [Hamiltonian in discrete position space](#hamiltonian-in-discrete-position-space)
  - [Manipulation](#manipulation)
  - [Hartree-Fock](#hartree-fock)
    - [Slater determinant](#slater-determinant)
  - [Hartree-Fock](#hartree-fock-1)
    - [Hartree-Fock approximation](#hartree-fock-approximation)
    - [Single and two particle operator](#single-and-two-particle-operator)
    - [Hartree-Fock functional](#hartree-fock-functional)
    - [Constraint on wavefunction](#constraint-on-wavefunction)
    - [Derivative](#derivative)
  - [Hatree](#hatree)
  - [Hatree-Fock](#hatree-fock)
    - [Hatree-Fock in a basis](#hatree-fock-in-a-basis)

Notes are mainly derived from **MSAE E4203** from Columbia University

## Electrons (Spring 2024, MSAE4203)

References
- **Solid State Physics**, Ashcroft and Mermin
- **Principles Of Quantum Mechanics**, Shankar

### Classical mechanics

#### Hamiltonian function

The Hamiltonian function captures both the kinetic and potential energy of a physical system.

$$
H(x, p) = T(p) + V(x) = \frac{p^2}{2m} + V(x)
$$

#### Force and motion

$$
F = \dot{p} = ma = m\ddot{x} = - \frac{\partial V(x)}{\partial x}
$$

The negative sign indicates that the force acts in the direction of decreasing potential energy. An apple falls from a tree and gains momentum and speed towards the Earth. It has a deal of potential energy. As the apple falls and reaches near the ground, the potential energy reaches zero. Hence, the apple "moves" in the direction that lowers gravitational potential energy.


#### Recover kinematics from Hamiltonian

From the Hamiltonian equation, we may recover force and velocity by differentiating the hamiltonian with respect to time and momentum:

$$
 \frac{\partial H}{\partial p} = \frac{p(t)}{m} = v = \frac{\partial x}{\partial t}
$$

$$
-\frac{\partial H}{\partial x} = -\frac{\partial V(x)}{\partial x} = F = - \frac{\partial p}{\partial t}
$$

#### Equation of motion for any observable

We are interested in knowing how certain physical variables such as momentum and time change as a function of time.

$$
A(x(t), p(t))
$$

We can generate an equation of motion for any observable such as energy, momentum, number of particles, etc. that depends on position and momentum via the chain rule:

$$
\frac{d}{dt} A(x(t), p(t)) = \frac{\partial A}{\partial x} \frac{\partial x}{\partial t} + \frac{\partial A}{\partial p} \frac{\partial p}{\partial t}
$$

$$
\frac{d}{dt} A(x, p) = \frac{\partial A}{\partial x} \frac{\partial H}{\partial p} - \frac{\partial H}{\partial x} \frac{\partial A}{\partial p} \equiv \{ A, H \}
$$

For position


$$
\dot{x}(t) = \{ x, H \} = \frac{\partial x}{\partial p} \frac{\partial H}{\partial x} - \frac{\partial H}{\partial p} {\frac{\partial x}{\partial x}} = \frac{\partial H}{\partial p} = \frac{p}{m}
$$

For momentum

$$
\dot{p}(t) = \{ p, H \} = \frac{\partial p}{\partial p} \frac{\partial H}{\partial x} - \frac{\partial H}{\partial p} \frac{\partial p}{\partial x} = -\frac{\partial H}{\partial x} = -\frac{\partial V(x)}{\partial x}
$$

### 1D particle in a box

The "particle in a box" model describes a particle free to move in a small space surrounded by impenetrable barriers. We consider the box to be one-dimensional with a length \( L \).

The potential energy inside the box is defined as:

$$
V(x) = 
\begin{cases} 
0 & \text{for } 0 < x < L \\
\infty & \text{otherwise}

\end{cases}
$$

The time-independent Schrödinger equation for this system is:

$$
-\frac{\hbar^2}{2m} \frac{d^2 \psi(x)}{dx^2} + V(x) \psi(x) = E \psi(x)
$$

Inside the box, this simplifies to:

$$
-\frac{\hbar^2}{2m} \frac{d^2 \psi(x)}{dx^2} = E \psi(x)
$$

The general solution to this equation is:

$$
\psi(x) = A \sin(kx) + B \cos(kx)
$$

Applying the boundary conditions $\psi(0) = 0$ and $\psi(L) = 0$, we find that $B = 0$ and $kL = n\pi$, where $n$ is a positive integer. Thus, the allowed energy levels are quantized, given by:

$$
E_n = \frac{n^2\pi^2\hbar^2}{2mL^2} =  \frac{n^2h}{8mL^2}
$$

and the normalized wave functions are:

$$
\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right)
$$

$$
n = 1, 2, 3, \ldots.
$$

The probability density

$$
|\psi_n(x)|^2 = \frac{2}{L} \sin^2\left(\frac{n\pi x}{L}\right)
$$

gives the probability of finding the particle at a position $x$ within the box.

### Space and momentum representation (Not finished)

$$
\psi(x) = \langle x|\psi\rangle
$$

$$
\psi^*(x) = \langle\psi|x\rangle
$$

Identity operator for finite and infinite systems

$$
  \hat{1} = \sum_{\ell} |\ell\rangle\langle\ell|, \quad \hat{1} = \int |\ell\rangle\langle\ell|d\ell 
$$

$$
\langle x|\hat{x}|x'\rangle = x\delta(x - x'),
$$

$$ \langle x|\hat{p}|x'\rangle = -i\hbar\frac{\delta}{\delta x}\delta(x - x')
$$

## Condensed Matter Physics (Spring 2024, PHYS6057)

## Electronic & Magnetic Properties of Solids (Fall 2023, MSAE 4206)

### Fermi energy

#### Energy scale

Fermi energy $E_F$ is the highest occupied quantum state energy at $T= 0\,K$. Fermi energy of copper at room temperature is approximately $7 eV$, much greater than $E_{KE}$ of $25\, meV$ at room temperature. Therefore, most materials exist in the ground state and DFT result at $0\, K$ is appropriate.

#### Implication for lattice distortion

The energy required to destory the lattice of NaCl is approximately $90\, meV$ prevent reaching the $E_F$ level without distorting the lattice.

#### Implication for electrical conductivity

At absolute zero temperature, all electrons are occupied in all energy states to the $E_F$ level. Electrons at room temperature, in constrast, may be excited above the $E_F$ level. These electrons may contribute to electrical conduction.

### Importance of symmetry

According to Noether's theory, every symmetry has a corresponding conservation law. Translational, rotational, and temporal symmetries conserve linear momentun, angular momentum, and energy, respectively.

It is said that breaking a symmetry leads to the **emergence** of new collective excitations and behaviors. From a liquid to a solid, continuous translation symmetry is broken and phonons emerge.

#### How to detect symmetry breaking

Atomic density may change during a phase transition. Ice density is is lower than water density.

### Density of states

#### What is state?

In the 1-dimensional particle in a box problem, every quantum state is non-degenerate, meaning each wavefunction corresponds to a unique energy level. However, there can be multiple states with the same energy level due to degeneracy in other physical systems.

To accurately describe physical phenomena in writing, we aim to utilize all available information in the system. Here, we can consider the number of states available at a particular energy and the volume of the substance given.

#### Why is volume relevant?

The number of states at a given energy depends on the volume of the substance. An analogy of a room filled with chairs can help visualize this concept: a person may occupy a seat in more ways in a larger room.

At each energy, we would expect different numbers of states available. For example, at absolute zero temperature, we would expect only 1 state at the ground state, but at finite temperature, we would expect more states.

We use use the following equation called the density of states (DOS)

$$
D(E) = \frac{d N(E)}{dE}
$$

to represent the number of states available at a given energy where $N$ is the total number of states **per unit energy per unit volume**. $states/eV\cdot m^{-3}$

In a typical three-dimensional (3D) metal, higher energy levels allow electrons to explore a greater range of available states with the following relation of

> To-do add 1D, 2D, 3D DOS derivation for ideal metals

$$
N \approx \sqrt E.
$$

As $E$ increases, the slope decreases and converges towards zero for an ideal 3D metal. The DOS curve initially rises steeply at lower energies and then gradually flattens out as energy increases.

  To justify with an analogy, at lower energies, the slope from $N = 1 \to 2$ within a finite $E$ interval is greater than the slope from $N = 100 \to 101$ in the same $E$ interval at higher energies.

#### Total number of states per unit volume

We may determine the total number of states per unit volume with the following equation of

$$
N(E) = \int_{E_0}^{E} D(E') \, dE',
$$

where $E'$ is an integration variable and $E_0$ is the lowest energy available. $E'$ was used to avoid confusion with $E$ which is the upper limit of energy.

### Quantum gas

For a system of $N$ identical quantum particles with weak or non-interaction (such as bosons or fermions), the total partition function can be approximated using the partition function for a single particle raised to the power of $N$ given by:

$$
Z^{(N)} \approx \sum_{i=1}^N Z^{(1)}_i
$$

where

$$Z^{(1)} = \sum e^{-\beta E_i}.
$$

## Materials Thermodynamics and Phase Diagrams (Fall 2023)

### Maxwell-Boltzmann distribution

#### Formula

The distribution describes the distribution of speeds of particles in a gas at $$T$$, given by:

$$
f(v) = 4\pi \left( \frac{m}{2\pi k_B T} \right)^{\frac{3}{2}} v^2 e^{-\frac{mv^2}{2k_B T}},
$$

where

- $f(v)$ is the probability density function of finding a particle with speed $v$.
- $m$ is the mass of the particle.
- $k_B$ is the Boltzmann constant.
- $T$ is the temperature of the gas in Kelvin.
- $v$ is the speed of the particle.

#### Average velocity

$$ P_{\text{total}} = 1 = \sum_{i=1}^{N} P(v_i) \to \int_0^{\infty} f(v) \, dv $$ 

$$ \langle v \rangle = \sum_{i=1}^{N} v_i \cdot P(v_i) \to \int_0^{\infty} v \cdot f(v) \, dv $$


## Kinetics

## Phonons

## Electrons - Writing a draft

**The following materials borrowed from the MSAE 4203 course materials and books**

In quantum mechanics, states are represented by vectors in a complex vector space. The inner product between any two state vectors gives a measure of the overlap between them.

If two state vectors are orthogonal, their inner product is zero, indicating they are completely distinct states.

State vectors are orthogonal. To capture the left expresion mathmatically, we use the expression of $\delta(x'-x)$ which states it is zero everywhere except the argument is zero as folows:

### Basic notations
$$
| V \rangle = \sum_{i}^n v_{i}| i \rangle
$$

$$
| W \rangle = \sum_{j}^n w_{j}| j \rangle
$$

$$
\langle V | W \rangle = \sum_{i}^n \sum_{j}^n v_{i}^*| w_{j} \langle i|j\rangle = =  \sum_i v_i^* w_i
$$

due to orthogonality where $i=j$ and if $i\not ={j}$ all terms become $0$.


#### Delta function

$$
\langle x|x'\rangle = \delta(x'-x), \quad \langle p|p'\rangle = \delta(p'-p).
$$

> Q. Why is the Kronecker delta used? The Kronecker delta, denoted as $\delta_{ij}$, is a discrete analog of the Dirac delta function.

> Q. Why is continuous space not used in practice? Continuous problems often require analytical expressions. Continous problems can be approximated into discrete set of points. With discrete points, we may apply numerical methods such as finite difference, Monte Carlo, etc. to solve problems.

$$
\hat{I} = \int dx \langle{x}\rangle{x} \approx \sum_i \langle{u_i}\rangle{u_i}.
$$

The identity operator can be used to discretize the hamiltonian operator:

$$
\hat{H} = \hat{I}\hat{H}\hat{I} \approx \left( \sum_{i} |u_i\rangle\langle u_i| \right) \hat{H} \left( \sum_{j} |u_j\rangle\langle u_j| \right) = \sum_{ij} |u_i\rangle\langle u_i| \hat{H} |u_j\rangle\langle u_j|
$$


#### Position representation in continous basis

We are still working in the continous space. 


This is effectively a mathematical trick that allows us to pull the wavefunction $\psi$ out of the integral at the specific point $x'$. We replace $x'$ with $x$ since they are at the same point.

$$
\langle x | \hat{H} | \psi \rangle = \int dx' \left[ -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} \delta(x - x') + V(x') \delta(x - x') \right] \psi(x') = E\psi(x)
$$

This is the "selector" operation:

$$
\int f(x') \delta(x - x') \, dx' = f(x)
$$

Which allows us to get the following expression

$$
\left[ -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V(x) \right] \psi(x) = E\psi(x)
$$

#### Hamiltonian in discrete position space

First, we want to project the time-indepeneent problem onto position representation. We achieve by projecting onto the position state vector with the following transformation:

$$
\hat{H} | \psi \rangle = E | \psi \rangle \to \langle x | \hat{H} | \psi \rangle = \langle x | E | \psi \rangle \to \langle x | \hat{H} | \psi \rangle = E\psi(x).
$$


$$
\hat{H} \approx
\begin{bmatrix}
\langle{u_1} | \hat{H} | {u_1}  \rangle& \langle{u_1} | \hat{H} | {u_2}  \rangle& \langle{u_1} | \hat{H} | {u_3}  \rangle\\
\langle{u_2} | \hat{H} | {u_1}  \rangle& \langle{u_2} | \hat{H} | {u_2}  \rangle& \langle{u_2} | \hat{H} | {u_3}  \rangle\\
\langle{u_3} | \hat{H} | {u_1}  \rangle& \langle{u_3} | \hat{H} | {u_2}  \rangle& \langle{u_3} | \hat{H} | {u_3}  \rangle\\
\end{bmatrix},

$$

with each element

$$
\langle u_a | \hat{H} | u_b \rangle = \int dx \langle u_a | x \rangle \left( -\frac{\hbar^2}{2m} \nabla^2 \right) \langle x | u_b \rangle + \int dx V(x) \langle u_a | x \rangle \langle x | u_b \rangle
$$

where

$$
\langle u_b | x \rangle = u_b^*(x), \langle x | u_b \rangle = u_b(x)
$$

Therefore

$$
\begin{align*}
\langle u_a | \hat{H} | u_b \rangle &= \int dx \, \langle u_a | x \rangle \left( -\frac{\hbar^2}{2m} \nabla^2 \right) \langle x | u_b \rangle + \int  dx \, V(x) \langle u_a | x \rangle \langle x | u_b \rangle \\
&= \int dx \, u_a^*(x) \left( -\frac{\hbar^2}{2m} \nabla^2 \right) u_b(x) + \int dx \, V(x) u_a^*(x) u_b(x)
\end{align*}
$$

### Manipulation



$$
\hat{H} | c \rangle = E \hat{S} | c \rangle \leftrightarrow \hat{S}^{-\frac{1}{2}} \hat{H} \hat{S}^{-\frac{1}{2}} | c' \rangle = E | c' \rangle
$$


Show

$$
1 = \int dr |r\rangle \langle r|
$$

Solution

$$
\begin{align*}
1 &=\int dr \ |\psi(\vec{r})|^2 \\
1  &=\int dr \ | \langle V |\vec{r}\rangle \langle \vec{r}| V\rangle\\
1  &= \langle V| V\rangle \int dr\ |\vec{r}  \rangle \langle \vec{r}|\\
1 &= \int dr |r\rangle \langle r| \\
\end{align*}
$$

### Hartree-Fock

It is used to determine the ground state energy of a quantum many-body problem.

A slater determinant is used to fulfill the anti-symmetry requirement. 

$$
\psi(1,2) = 1s\alpha(1)1s\beta(2)
$$

$$
\psi(2,1) = 1s\alpha(2)1s\beta(1)
$$

Both $\psi(1,2)$ and $\psi(2,1)$ are equally valid but they are indistinguishable. Therefore, we must take the linear combinations of them.

$$
\Psi_1(1,2) =  \psi(1,2) + \psi(2,1) = 1s\alpha(1)1s\beta(2) + 1s\alpha(2)1s\beta(1)
$$

$$
\Psi_2(1,2) =  \psi(1,2) - \psi(2,1) = 1s\alpha(1)1s\beta(2) - 1s\alpha(2)1s\beta(1)
$$

In real life, $\Psi_2(1,2)$ turn out to be what we use and it satisfies the anti-symmetry relation below

> $1s\alpha$ and $1s\beta$ represent $\Psi_{100 \frac{1}{2}}$ and $\Psi_{100 -\frac{1}{2}}$

$$
\Psi_2(2, 1) = \psi(2, 1) - \psi(1, 2) = -\Psi_2(1,2)
$$

Electronic wave functions are anti-symmetric when two electrons interchange.

#### Slater determinant

It is used to represent the anti-symmetry and linear combination requirement shown below

$$
\Psi(1,2) =\begin{vmatrix}
1s\alpha(1) & 1s\beta(1) \\
1s\alpha(2) & 1s\beta(2) \\
\end{vmatrix}
$$

and normalized as

$$
\Psi(1,2) = \frac{1}{\sqrt{2!}}\begin{vmatrix}
1s\alpha(1) & 1s\beta(1) \\
1s\alpha(2) & 1s\beta(2) \\
\end{vmatrix}
$$

For a lithium atom

$$
\Psi(1,2, 3) = \frac{1}{\sqrt{3!}}\begin{vmatrix}
1s\alpha(1) & 1s\beta(1) & 2s\alpha(1) \\
1s\alpha(2) & 1s\beta(2) & 2s\alpha(2) \\
1s\alpha(3) & 1s\beta(3) & 2s\alpha(3) \\
\end{vmatrix}
$$

### Hartree-Fock

Hamiltonian for N-electron system

$$
\hat{H} = \sum_{i=1}^{N} \left( \frac{1}{2} \mathbf{p}_i^2 + V(\mathbf{r}_i) \right) + \sum_{i<j} \frac{1}{|\mathbf{r}_i - \mathbf{r}_j|}
$$

If we consider N=3

$$
\hat{H} = \frac{1}{2} (\mathbf{p}_1^2 + \mathbf{p}_2^2 + \mathbf{p}_3^2) + V(\mathbf{r}_1) + V(\mathbf{r}_2) + V(\mathbf{r}_3) + \frac{1}{|\mathbf{r}_1 - \mathbf{r}_2|} + \frac{1}{|\mathbf{r}_1 - \mathbf{r}_3|} + \frac{1}{|\mathbf{r}_2 - \mathbf{r}_3|}
$$

#### Hartree-Fock approximation

Rather than employing a product space, we aim to determine the optimal $\Psi$ by utilizing a product of individual electron states $\psi_a$, $\psi_b$, $\psi_c$. The many-body wavefunction for a system of electrons can be described as a single Slater determinant. This corresponds to an antisymmetrized product of one-electron wavefunctions, also known as orbitals. The approximation is shown below 

from

$$
|\psi_a \psi_b \psi_c \rangle = |\psi_a \rangle \otimes |\psi_b \rangle \otimes |\psi_c \rangle
$$

to

$$
\Psi(\mathbf{r}_1, \mathbf{r}_2, \mathbf{r}_3) = \psi_a(\mathbf{r}_1)\psi_b(\mathbf{r}_2)\psi_c(\mathbf{r}_3)
$$

Now, our job is to find the very best $\Psi$. We will see an iterative method to solve for $\Psi$.

> What is a Hilbert space? A Hilbert space is an infinite-dimensional vector space often used in quantum mechanics to represent state vectors, including wavefunctions. It is characterized by completeness and an inner product structure. While theoretically infinite-dimensional, in practice, we typically use finite-dimensional subspaces or discrete basis sets for calculations, to approximate the physics of quantum systems effectively.

#### Single and two particle operator

$$
(\psi_a \psi_b \psi_c | \hat{T}_1 | \psi_a \psi_b \psi_c) 
= \langle \psi_a | \otimes \langle \psi_b | \otimes \langle \psi_c | \hat{T} \otimes \mathbb{1} \otimes \mathbb{1} | \psi_a \rangle \otimes | \psi_b \rangle \otimes | \psi_c \rangle
$$

But $\hat{T}_{1}$ operators on a single particle wavefunction.
$$
(\psi_a \psi_b \psi_c | \hat{T}_1 | \psi_a \psi_b \psi_c) 
= (\psi_a | \hat{T}_1 | \psi_a) 
$$

where

$$ 
(\psi_a | \hat{T}_1 | \psi_a)  = -\frac{1}{2} \int d^3 r \, \psi_a^*(\mathbf{r}) \nabla^2 \psi_a(\mathbf{r})
$$

Two-particle operator pick out two wavefunctions.

$$
(\psi_a \psi_b \psi_c | \hat{r}_{12}^{-1} | \psi_a \psi_b \psi_c)
= (\psi_a \psi_b | \hat{r}_{12}^{-1} | \psi_a \psi_b)
$$

$$
\hat{r}_{ij} \equiv |\mathbf{r}_i - \mathbf{r}_j|
$$

$$
(\psi_a \psi_b | \hat{r}_{12}^{-1} | \psi_a \psi_b )
= \int d^3 r_1 d^3 r_2 \frac{\psi_a^*(r_1) \psi_b^*(r_2)} {\hat{r}_{12}} \psi_a(\mathbf{r_1}) \psi_b(\mathbf{r_2})
$$

#### Hartree-Fock functional


$$
\mathcal{F}[\psi_a(\mathbf{r}_1), \psi_b(\mathbf{r}_2), \psi_c(\mathbf{r}_3)] = \langle \psi_a \psi_b \psi_c | \hat{H} | \psi_a \psi_b \psi_c \rangle
$$

$$
\mathcal{F} [\psi_a(\mathbf{r}_1), \psi_b(\mathbf{r}_2), \psi_c(\mathbf{r}_3)] 
= F_1^{(1)} + F_2^{(2)}
$$


where 

$$
\mathcal{F}_1^{(1)} = 

\langle \psi_a | \hat{T}_1
+ \hat{V}_1 | \psi_a \rangle + \langle \psi_b | \hat{T}_2
+ \hat{V}_2 | \psi_b \rangle + \langle \psi_c | \hat{T}_3
+ \hat{V}_3 | \psi_c \rangle 
$$

$$
\mathcal{F}_2^{(2)} =
   \left( \psi_a \psi_b | \hat{r}_{12}^{-1} | \psi_a \psi_b \right)
 + \left( \psi_a \psi_c | \hat{r}_{13}^{-1} | \psi_a \psi_c \right)
 + \left( \psi_b \psi_c | \hat{r}_{23}^{-1} | \psi_b \psi_c \right)
$$


#### Constraint on wavefunction

Lagrange multipliers are used to impose the constraint that the wave functions (orbitals) must be orthonormal. When we minimize the energy functional to find the best wave functions, we must take into these constraints. To learn more, look into the Farmer problem problem.

$$
\mathcal{F}' = \mathcal{F} 
- \sum_{i,j} \lambda_{ij} (\langle \psi_i | \psi_j \rangle
- \delta_{ij})
$$

By the setting the derivative of $\mathcal{F}'$ with respect to each $\psi_i$ and each langrange multipler $\lambda_{ij}$
, we obtain a set of equations that can be solved self-consistently.

*At the moment, I am not sure how the above general equation is related to the following.*

$$
\mathcal{F}' = \mathcal{F} - \epsilon_a \langle\psi_a|\psi_b\rangle - \epsilon_b \langle\psi_b|\psi_b\rangle - \epsilon_c \langle\psi_c|\psi_c \rangle
$$

#### Derivative

Differentaite $\mathcal{F}'$ with respect to each wavefunction likse

$$
\frac {\delta \mathcal{F}'}{\delta \psi_a^*},
\frac {\delta \mathcal{F}'}{\delta \psi_b^*},
\frac {\delta \mathcal{F}'}{\delta \psi_c^*} = 0
$$

Recall

$$
(\psi_a \psi_b | \hat{r}_{12}^{-1} | \psi_a \psi_b )
= \int d^3 r_1 d^3 r_2 \frac{\psi_a^*(r_1) \psi_b^*(r_2)} {\hat{r}_{12}} \psi_a(\mathbf{r_1}) \psi_b(\mathbf{r_2})
$$

### Hatree

$$
\left[ -\frac{1}{2} \nabla^2_1 + V(r_1) - \epsilon_a \right] \psi_a(r_1) + \int d^3r_2 \frac{\psi_b^*(r_2)\psi_b(r_2)}{r_{12}} + \int d^3r_3 \frac{\psi_c^*(r_3)\psi_c(r_3)}{r_{13}} \psi_a(r_1) = 0
$$

$$
\left[ -\frac{1}{2} \nabla^2_2 + V(r_2) - \epsilon_b \right] \psi_b(r_2) + \int d^3r_1 \frac{\psi_a^*(r_1)\psi_a(r_1)}{r_{12}} + \int d^3r_3 \frac{\psi_c^*(r_3)\psi_c(r_3)}{r_{23}} \psi_b(r_2) = 0
$$

$$
\left[ -\frac{1}{2} \nabla^2_3 + V(r_3) - \epsilon_c \right] \psi_c(r_3) + \int d^3r_1 \frac{\psi_a^*(r_1)\psi_a(r_1)}{r_{13}} + \int d^3r_2 \frac{\psi_b^*(r_2)\psi_b(r_2)}{r_{23}} \psi_c(r_3) = 0
$$

### Hatree-Fock

In the Hatree approximation, Eigenvectors are not anti-symmetric when two particles are changed.


Because the total wavefunction is a tensor product of a spatial part and a spin part, the inner product separates into the product of the inner products of the respective spatial and spin parts:



$$
|\psi_a\rangle = | \chi_{a_0} \rangle \otimes | \xi_{a_1} \rangle \text{ where } a_1 \in \{\uparrow, \downarrow\}, \langle \xi_{i} | \xi_{j} \rangle = \delta_{ij}
$$

Express the inner product as the product of the inner products of the spatial and spin parts:

$$
\begin{align*}
\langle \psi_b | \psi_a \rangle &= \langle \chi_{b_0} \otimes \xi_{b_1} | \chi_{a_0} \otimes \xi_{a_1} \rangle \\
&= \langle \chi_{b_0} | \chi_{a_0} \rangle \langle \xi_{b_1} | \xi_{a_1} \rangle \\
&= \delta_{b_1 a_1} \langle \chi_{b_0} | \chi_{a_0} \rangle
\end{align*}
$$



Recall the product Fock space.

$$
|\psi_a \psi_b \psi_c ) = |\psi_a \rangle \otimes |\psi_b \rangle \otimes |\psi_c \rangle
$$

Using the Hatree-Fock approximation, we will account for the anti-symmetry relation and noramlize it. There are $3!$ ways to permute a 3-electron system. We have the following wavefunction. 

$$
|\psi_a \psi_b \psi_c \rangle
= \frac{1}{\sqrt{6}} \left( | \psi_a \psi_b \psi_c) - | \psi_a \psi_c \psi_b ) - | \psi_b \psi_a \psi_c ) + | \psi_b \psi_c \psi_a ) + | \psi_c \psi_a \psi_b ) - | \psi_c \psi_b \psi_a ) \right)
$$

$$
\begin{align*}
F = \frac{1}{6} \Bigl[ 
&2\langle \psi_a | \hat{T}_1 + \hat{V}_1 | \psi_a \rangle + 2\langle \psi_a | \hat{T}_2 + \hat{V}_2 | \psi_a \rangle + 2\langle \psi_a | \hat{T}_3 + \hat{V}_3 | \psi_a \rangle + \\
&2\langle \psi_b | \hat{T}_1 + \hat{V}_1 | \psi_b \rangle + 2\langle \psi_b | \hat{T}_2 + \hat{V}_2 | \psi_b \rangle + 2\langle \psi_b | \hat{T}_3 + \hat{V}_3 | \psi_b \rangle + \\
&2\langle \psi_c | \hat{T}_1 + \hat{V}_1 | \psi_c \rangle + 2\langle \psi_c | \hat{T}_2 + \hat{V}_2 | \psi_c \rangle + 2\langle \psi_c | \hat{T}_3 + \hat{V}_3 | \psi_c \rangle + \\
&2( \psi_a \psi_b | \hat{r}_{12}^{-1} | \psi_a \psi_b ) + 2( \psi_a \psi_b | \hat{r}_{13}^{-1} | \psi_a \psi_b ) + 2( \psi_a \psi_b | \hat{r}_{23}^{-1} | \psi_a \psi_b ) + \\
&2( \psi_a \psi_c | \hat{r}_{12}^{-1} | \psi_a \psi_c ) + 2( \psi_a \psi_c | \hat{r}_{13}^{-1} | \psi_a \psi_c ) + 2( \psi_a \psi_c | \hat{r}_{23}^{-1} | \psi_a \psi_c ) + \\
&2( \psi_b \psi_c | \hat{r}_{12}^{-1} | \psi_b \psi_c ) + 2( \psi_b \psi_c | \hat{r}_{13}^{-1} | \psi_b \psi_c ) + 2( \psi_b \psi_c | \hat{r}_{23}^{-1} | \psi_b \psi_c ) - \\
&2( \psi_b \psi_a | \hat{r}_{12}^{-1} | \psi_b \psi_a ) - 2( \psi_b \psi_a | \hat{r}_{13}^{-1} | \psi_b \psi_a ) - 2( \psi_b \psi_a | \hat{r}_{23}^{-1} | \psi_b \psi_a ) - \\
&2( \psi_c \psi_a | \hat{r}_{12}^{-1} | \psi_c \psi_a ) - 2( \psi_c \psi_a | \hat{r}_{13}^{-1} | \psi_c \psi_a ) - 2( \psi_c \psi_a | \hat{r}_{23}^{-1} | \psi_c \psi_a ) - \\
&2( \psi_c \psi_b | \hat{r}_{12}^{-1} | \psi_c \psi_b ) - 2( \psi_c \psi_b | \hat{r}_{13}^{-1} | \psi_c \psi_b ) - 2( \psi_c \psi_b | \hat{r}_{23}^{-1} | \psi_b \psi_c ) \Bigr]
\end{align*}
$$

Collected and simplified to 

$$
\begin{align*} F = \langle \psi_a | \hat{T} + \hat{V} | \psi_a \rangle + \langle \psi_b | \hat{T} + \hat{V} | \psi_b \rangle + \langle \psi_c | \hat{T} + \hat{V} | \psi_c \rangle \\
& + (\psi_a \psi_b | \hat{r}_{ij}^{-1} | \psi_a \psi_b) + (\psi_a \psi_c | \hat{r}_{ij}^{-1} | \psi_a \psi_c) + (\psi_b \psi_c | \hat{r}_{ij}^{-1} | \psi_b \psi_c) \\
* - (\psi_b \psi_a | \hat{r}_{ij}^{-1} | \psi_a \psi_b) - (\psi_c \psi_a | \hat{r}_{ij}^{-1} | \psi_a \psi_c) - (\psi_c \psi_b | \hat{r}_{ij}^{-1} | \psi_b \psi_c)
\end{align*}
$$




$$
F' = \langle \psi_a | \hat{T} + \hat{V} | \psi_a \rangle + \langle \psi_b | \hat{T} + \hat{V} | \psi_b \rangle + \langle \psi_c | \hat{T} + \hat{V} | \psi_c \rangle \\
+ (\psi_a \psi_b | \hat{r}_{ij}^{-1} | \psi_a \psi_b) + (\psi_a \psi_c | \hat{r}_{ij}^{-1} | \psi_a \psi_c) + (\psi_b \psi_c | \hat{r}_{ij}^{-1} | \psi_b \psi_c) \\
- (\psi_b \psi_a | \hat{r}_{ij}^{-1} | \psi_a \psi_b) - (\psi_c \psi_a | \hat{r}_{ij}^{-1} | \psi_a \psi_c) - (\psi_c \psi_b | \hat{r}_{ij}^{-1} | \psi_b \psi_c) \\
- \varepsilon_a \langle \psi_a | \psi_a \rangle - \varepsilon_b \langle \psi_b | \psi_b \rangle - \varepsilon_c \langle \psi_c | \psi_c \rangle

$$


$$
\left[ -\frac{1}{2} \nabla^2 + V(r) - \varepsilon_a + \int d^3r' \frac{\psi_b^*(r')\psi_b(r')}{|r - r'|} + \int d^3r' \frac{\psi_c^*(r')\psi_c(r')}{|r - r'|} \right] \psi_a(r) \\
- \int d^3r' \frac{\psi_b^*(r')\psi_a(r')\psi_b(r)}{|r - r'|} - \int d^3r' \frac{\psi_c^*(r')\psi_a(r')\psi_c(r)}{|r - r'|} = 0
$$


$$
\left[ -\frac{1}{2} \nabla^2 + V(\mathbf{r}) + \int d^3r' \, \frac{\rho_b(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|} + \int d^3r' \, \frac{\rho_c(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|} \right] \psi_a(\mathbf{r}) - \int d^3r' \, \frac{\psi_b^*(\mathbf{r}')\psi_a(\mathbf{r}')\psi_b(\mathbf{r})}{|\mathbf{r} - \mathbf{r}'|} - \int d^3r' \, \frac{\psi_c^*(\mathbf{r}')\psi_a(\mathbf{r}')\psi_c(\mathbf{r})}{|\mathbf{r} - \mathbf{r}'|} = \varepsilon_a \psi_a(\mathbf{r})

$$


$$
\begin{align*}
\left[ -\frac{1}{2} \nabla^2 + V(\mathbf{r}) \right] \psi_a(\mathbf{r}) + &\int d^3r' \, \frac{\rho_b(\mathbf{r}') - \psi_b^*(\mathbf{r}')\hat{P}_{ab}\psi_b(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|} \psi_a(\mathbf{r}) \\
+ &\int d^3r' \, \frac{\rho_c(\mathbf{r}') - \psi_c^*(\mathbf{r}')\hat{P}_{ac}\psi_c(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|} \psi_a(\mathbf{r}) = \varepsilon_a \psi_a(\mathbf{r})
\end{align*}
$$





#### Hatree-Fock in a basis

Wavefunctions are expressed in terms of a basis set.

The following is a one-electron wavefunction. The basis wavefunctions are not orthogonal in general. We will use the variational method to solve for $\psi(\textbf{r})$ of

$$
\psi_a(\textbf{r}) = \sum_{\alpha}C_{a\alpha}\phi_\alpha^{a}(\textbf{r}),
$$

where it represents a molecular orbital consisted of various  quantum number sets indicated by $\alpha$.

> The vector $\\textbf{r}$ is needed to define the x, y, z, coordinates in space

- $\psi_a(\textbf{r})$ - wavefunction for $a$ molecular orbital at position $\textbf{r}$.
- $a$ - $a^{th}$ molecular orbital, used for bookkeeping
- $C_{ca}$ - variational coefficients of $a^{th}$ molcular orbital
- $\phi_\alpha$ - non-orthogonal basis functions
- $\alpha$ - space quantum number set
- $\sigma$ - spin of $\alpha$ or $\beta$

We want to set up matrix elements of a HF hamiltonian 


$$
H^{hf} = 
-\frac{1}{2} \nabla^2
+ V(\textbf{r})
+ \int d^3 \textbf{r}' \frac{\rho(\textbf{r}')
- \sum_i \psi_i^*(\textbf{r}') \hat{P} \psi_i (\textbf{r}')}{|\textbf{r} - \textbf{r}'|}
$$

Split into non-interacting and many-body parts below

$$
H^{hf} = H_o + \hat{F}
$$

where

$$
H_o =  -\frac{1}{2} \nabla^2 + V(\textbf{r})
$$

$$
\hat{F} = \int d^3 \textbf{r}' \frac{\rho(\textbf{r}')
- \sum_i \psi_i^*(\textbf{r}') \hat{P} \psi_i (\textbf{r}')}{|\textbf{r} - \textbf{r}'|}
$$

where $\rho(\textbf{r}')$ denotes the charge density, $\psi_i^*(\textbf{r}')$ and $\psi_i(\textbf{r}')$ are the complex conjugate wave functions, and $\hat{P}$ is an operator acting on these wave functions.

> What is $\hat{P}$ operator? Not sure at the moment.

$$  
H_{o, \alpha\beta} =
\langle \phi^\sigma_\alpha | \hat{T} | \phi^\sigma_\alpha \rangle 
+
\langle \phi^\sigma_\alpha | \hat{V} | \phi^\sigma_\alpha \rangle
$$

Therefore 

$$
\begin{align*}
H_{\alpha \beta}^{hf, \sigma} &= \int d^3 r \ \psi_\alpha^{\sigma*} H^{hf} \phi^\sigma_\beta (\textbf{r}) \\

&= \int d^3 r \ \psi_\alpha^{\sigma*} (H_o + \hat{F}) \phi^\sigma_\beta (\textbf{r})
\end{align*}
$$

where $\hat{T}$ represents the kinetic energy operator, $\hat{V}$ the potential energy operator, and $\phi^\sigma_\alpha$ are the spin orbitals.