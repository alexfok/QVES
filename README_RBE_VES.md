# RBE-Based Quantum Visual Encryption Scheme (Q-VES)

Implementation based on the paper:  
**"Quantum Perfect Output VES in Spite of Swarm Byzantine Participants"**  
By: Shlomi Dolev, Alexander Fok, Michael Segal  
Ben-Gurion University of the Negev

## Overview

This implementation provides the **exact quantum VES design from your paper**, using:

- **Random Basis Encryption (RBE)** for information-theoretically secure pixel encoding
- **Three-party distributed protocol** (Participants A, B, C)
- **CNOT-based homomorphic matching** without revealing the secret image
- **Byzantine-resilient architecture** with majority voting
- **No-cloning theorem protection**

## Key Innovation: RBE vs Traditional Encryption

### Random Basis Encryption (RBE)

Unlike traditional Quantum One-Time Pad (QOTP) which uses only 4 Pauli gates, RBE uses a **continuously parameterized space** of quantum bases:

```
Encryption: |ψ⟩ = K_{θ,φ} |b⟩

where K_{θ,φ} = [cos(θ/2)              sin(θ/2)          ]
                 [e^{iφ}sin(θ/2)  -e^{iφ}cos(θ/2)]

θ ∈ [0, 2π]
φ ∈ {-π/2, +π/2}
```

**Advantages:**
- Higher entropy per bit (continuous vs discrete basis)
- Better protection against weak quantum measurements
- Non-interactive homomorphic evaluation
- Perfect information-theoretic security

## System Architecture

### Three-Party Protocol

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│Participant A│         │Participant C│         │Participant B│
│  (Encoder)  │         │ (Matcher)   │         │ (Decoder)   │
└──────┬──────┘         └──────┬──────┘         └──────┬──────┘
       │                       │                       │
       │  QT[i] = K|T[i]⟩     │                       │
       ├──────────────────────>│                       │
       │                       │                       │
       │  (θ, φ) keys          │                       │
       ├───────────────────────────────────────────────>│
       │                       │                       │
       │                       │ Observes C[i]         │
       │                       │                       │
       │                       │ Apply CNOT if C[i]=1  │
       │                       │                       │
       │                       │  QT'[i]               │
       │                       ├───────────────────────>│
       │                       │                       │
       │                       │                       │ RBE.Dec
       │                       │                       │ Measure
       │                       │                       │
       │                       │<──────────────────────┤
       │                       │   Match if |0⟩        │
```

### Participant Roles

**Participant A (Encoder):**
- Encrypts each pixel: `QT[i] = K_{θ,φ} |T[i]⟩`
- Distributes encrypted qubits to C
- Sends encryption keys `(θ, φ)` to B
- Stores quantum ciphertext

**Participant C (Matcher):**
- Observes candidate image pixels `C[i]`
- Applies conditional CNOT:
  - If `C[i] = 0`: no operation
  - If `C[i] = 1`: apply CNOT (flips qubit)
- Forwards transformed qubit to B
- **Never learns the secret pixel value**

**Participant B (Decoder):**
- Holds all RBE decryption keys
- Applies `K†_{θ,φ}` to decrypt
- Measures in computational basis
- Determines match: **Match if result = |0⟩**

## Matching Protocol

### Step-by-Step Process

For each pixel `i`:

1. **A encrypts:** `QT[i] = K_{θ,φ} |T[i]⟩`
2. **A → C:** Sends encrypted qubit `QT[i]`
3. **C observes:** Candidate pixel `C[i] ∈ {0,1}`
4. **C transforms:**
   ```
   QT'[i] = {
     QT[i]         if C[i] = 0
     CNOT(QT[i])   if C[i] = 1
   }
   ```
5. **C → B:** Sends `QT'[i]`
6. **B decrypts:** Applies `K†_{θ,φ}` and measures
7. **B decides:** Match if measurement yields `|0⟩`

### Mathematical Proof (from paper)

**Lemma:** `RBE.Dec(QT'[i]) = 0 ⟺ T[i] = C[i]`

**Proof:**
```
After encryption: QT[i] = K_{θ,φ}|T[i]⟩

After C's CNOT:
QT'[i] = {
  K_{θ,φ}|T[i]⟩       if C[i] = 0
  K_{θ,φ}|T[i] ⊕ 1⟩   if C[i] = 1
}

After B's decryption:
K†_{θ,φ} QT'[i] = |T[i] ⊕ C[i]⟩

Result = 0 ⟺ T[i] ⊕ C[i] = 0 ⟺ T[i] = C[i]
```

## Byzantine Resilience

To tolerate Byzantine (malicious) participants, the system uses **multiple C participants** with majority voting:

```
┌───┐
│ A │───┐
└───┘   │
        ├──> C[1] ──┐
        ├──> C[2] ──┤
        ├──> C[3] ──┼──> B (Majority Vote)
        ├──> C[4] ──┤
        └──> C[5] ──┘
```

**Tolerance:** System tolerates up to `⌊(M-1)/2⌋` Byzantine participants out of M total C participants.

**Example:** With M=5 participants, tolerates up to 2 Byzantine nodes.

## Security Features

### 1. Information-Theoretic Security

- **No computational assumptions:** Secure against adversaries with unlimited computational power
- **Perfect secrecy:** Without the correct basis `(θ, φ)`, any measurement yields uniformly random results
- **Independent encryption:** Each pixel uses a fresh random basis

### 2. Quantum Protection

- **No-Cloning Theorem:** Quantum states cannot be copied → prevents unauthorized duplication
- **Measurement Disturbance:** Any eavesdropping attempt disturbs the quantum state (detectable)
- **Weak Measurement Resilience:** Continuous basis space prevents partial information leakage

### 3. Distributed Security

- **Role Separation:** No single participant has complete information
  - A has encrypted qubits but not keys
  - B has keys but not original qubits
  - C has neither secret nor keys
- **Homomorphic Operations:** C can process without decrypting

## Implementation Files

### Core Implementation

1. **`rbe_quantum_ves.py`** - Full quantum implementation using Qiskit
   - `RBEEncoder`: Implements RBE encryption/decryption
   - `QuantumVESParticipantA`: Encoder class
   - `QuantumVESParticipantB`: Decoder class  
   - `QuantumVESParticipantC`: Matcher class
   - `QuantumVESSystem`: Complete protocol
   - `ByzantineResilientQVES`: Multi-party system

2. **`rbe_ves_demo_simple.py`** - Simplified demonstration (no Qiskit required)
   - Shows protocol logic
   - Step-by-step explanation
   - No quantum simulation needed

### Legacy Files (Generic VES)

- `quantum_ves.py` - Generic quantum VES (not paper-specific)
- `quantum_network_ves.py` - Generic network VES (not paper-specific)
- `examples_demo.py` - Generic examples

**Note:** Use `rbe_quantum_ves.py` for the paper-specific implementation.

## Installation

### Quick Start (Simplified Demo)

No installation needed - uses only NumPy:

```bash
python3 rbe_ves_demo_simple.py
```

### Full Quantum Simulation

1. Create virtual environment:
```bash
chmod +x setup.sh
./setup.sh
```

2. Or manually:
```bash
python3 -m venv qves_env
source qves_env/bin/activate
pip install -r requirements.txt
```

3. Run quantum simulation:
```bash
python3 rbe_quantum_ves.py
```

## Usage Examples

### Basic Usage

```python
from rbe_quantum_ves import QuantumVESSystem
import numpy as np

# Create secret image
secret = np.array([[1, 0], [0, 1]])

# Initialize system
qves = QuantumVESSystem()

# Setup (A encrypts, distributes to B and C)
qves.setup_secret_image(secret)

# Perform matching
candidate = np.array([[1, 0], [1, 1]])
matches, percentage = qves.perform_matching(candidate)

print(f"Match: {percentage}%")
```

### Byzantine-Resilient Matching

```python
from rbe_quantum_ves import ByzantineResilientQVES

# Initialize with 5 C participants
qves = ByzantineResilientQVES(n_c_participants=5)
qves.setup_secret_image(secret)

# Perform matching with 2 Byzantine participants
byzantine_indices = [1, 3]
matches, percentage = qves.perform_byzantine_resilient_matching(
    candidate, byzantine_indices=byzantine_indices
)
```

## Running on IBM Quantum Hardware

### Setup IBM Quantum Account

1. Create account at https://quantum.cloud.ibm.com/
2. Get API token from account settings
3. Save token:

```python
from qiskit_ibm_runtime import QiskitRuntimeService

QiskitRuntimeService.save_account(
    token='YOUR_IBM_QUANTUM_TOKEN',
    channel='ibm_quantum'
)
```

### Execute on Real Quantum Computer

```python
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit import transpile

# Load service
service = QiskitRuntimeService()

# Get backend
backend = service.backend('ibm_brisbane')  # or another available backend

# Transpile circuit for hardware
qc = participant_A.get_encrypted_pixel(0)
transpiled = transpile(qc, backend=backend)

# Execute
job = backend.run(transpiled, shots=1024)
result = job.result()
```

## Performance Metrics

### Circuit Complexity

For an image with N pixels:

| Metric | Complexity | Example (4×4 image) |
|--------|------------|---------------------|
| Qubits per pixel | 1 | 16 total qubits |
| RBE gates per pixel | 1 unitary | 16 RBE operations |
| CNOT operations | ≤ N | ≤ 16 CNOTs |
| Circuit depth | O(1) per pixel | Constant depth |

### Byzantine Resilience

| M (C participants) | Tolerated Byzantine | Required Honest |
|--------------------|---------------------|-----------------|
| 3 | 1 | 2 |
| 5 | 2 | 3 |
| 7 | 3 | 4 |
| 2k+1 | k | k+1 |

## Comparison: Paper vs Generic Implementation

| Feature | RBE-VES (Paper) | Generic VES |
|---------|----------------|-------------|
| Encryption | RBE with continuous basis | Various methods |
| Participants | 3 roles (A, B, C) | 2 shares |
| Matching | Homomorphic CNOT | Classical XOR |
| Byzantine Resilience | Yes (majority vote) | No |
| Security | Information-theoretic | Varies |
| Basis Space | Continuous [0, 2π] | Discrete (4 states) |

## Applications

Based on your paper, the main application is:

### UAV Swarm Target Search

**Scenario:** A swarm of UAVs searches for a target specified by a secret reference image.

**Requirements:**
- UAVs must match observed images to the secret reference
- Secret image must remain confidential
- System must tolerate compromised/faulty UAVs
- No centralized reconstruction needed

**Solution using RBE-VES:**
1. Dealer encrypts target image using RBE
2. UAVs receive encrypted qubits (as Participant C)
3. Ground station holds decryption keys (Participant B)
4. UAVs observe environment and apply conditional CNOT
5. Ground station aggregates results via majority vote
6. System remains secure even if some UAVs are compromised

## References

### Main Paper

Dolev, S., Fok, A., & Segal, M. "Quantum Perfect Output VES in Spite of Swarm Byzantine Participants"

### RBE Reference

Bitan, D., & Dolev, S. (2023). "Randomly Choose an Angle Immense Encryption with Quantum-Secured Keys"

### Quantum Computing

- Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*
- IBM Quantum Documentation: https://docs.quantum.ibm.com/

## Citation

If you use this implementation in your research:

```bibtex
@article{dolev2025quantum_ves,
  title={Quantum Perfect Output VES in Spite of Swarm Byzantine Participants},
  author={Dolev, Shlomi and Fok, Alexander and Segal, Michael},
  journal={[Journal Name]},
  year={2025},
  institution={Ben-Gurion University of the Negev}
}
```

## Support

For questions about the implementation:
- Email: alexfok@post.bgu.ac.il
- Institution: Ben-Gurion University
- Research Group: Distributed Computing & Quantum Cryptography

## License

This project is part of PhD research at Ben-Gurion University of the Negev.

## Acknowledgments

- Israeli Science Foundation (Grant No. 465/22)
- Army Research Office (Grant W911NF-22-1-0225)
- Rita Altura Trust Chair in Computer Science
- IBM Quantum for quantum computing access

---

**Last Updated:** November 14, 2025  
**Version:** 1.0 (Paper Implementation)  
**Status:** Research Implementation


