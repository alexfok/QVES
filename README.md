# Quantum Visual Encryption Scheme (Q-VES)

A comprehensive implementation of quantum-based Visual Encryption Scheme (VES) using IBM Qiskit for secure image encryption and distribution over quantum networks.

## Overview

This project implements quantum approaches to visual cryptography, providing:

- **Quantum Visual Secret Sharing (QVSS)**: Encoding images into quantum states using superposition and entanglement
- **Entanglement-Based Distribution**: Utilizing Bell states and GHZ states for share distribution
- **Quantum Network Integration**: Distributing shares across quantum networks using quantum teleportation
- **Threshold Schemes**: (k, n) threshold secret sharing where k shares are required for reconstruction
- **Security Analysis**: Leveraging quantum properties like no-cloning theorem and entanglement for enhanced security

## Key Features

### Quantum Advantages

1. **No-Cloning Theorem**: Quantum shares cannot be copied without detection
2. **Entanglement**: Provides correlation between shares while maintaining individual randomness
3. **Quantum Teleportation**: Secure share distribution without physical transmission
4. **Eavesdropping Detection**: Bell inequality violations detect interception attempts
5. **Perfect Secrecy**: Single shares provide zero information about the original image

### Implemented Methods

- **XOR-Based Quantum Sharing**: Classical XOR enhanced with quantum superposition
- **Bell State Sharing**: Maximally entangled pairs for two-party sharing
- **GHZ State Sharing**: Multi-party entanglement for n-party protocols
- **W-State Threshold**: (k, n) threshold schemes using W-states
- **Quantum Teleportation**: Distribution protocol using EPR pairs

## Installation

### Prerequisites

- Python 3.8 or higher
- IBM Qiskit 1.0 or higher

### Setup

```bash
# Create virtual environment (recommended)
python -m venv qves_env
source qves_env/bin/activate  # On Windows: qves_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Example

```python
from quantum_ves import QuantumVES, create_sample_image

# Create a binary image
image = create_sample_image('cross', size=(4, 4))

# Initialize Q-VES
qves = QuantumVES(image_size=image.shape)

# Create quantum shares
qc1, qc2, share1, share2 = qves.xor_based_sharing(image)

# Reconstruct image
reconstructed = qves.classical_xor_reconstruct(share1, share2)

print(f"Reconstruction successful: {np.array_equal(image, reconstructed.reshape(image.shape))}")
```

### Entangled Shares

```python
# Create maximally entangled shares using Bell states
entangled_circuit = qves.create_entangled_shares(image)

print(f"Circuit uses {entangled_circuit.num_qubits} qubits")
print(f"Circuit depth: {entangled_circuit.depth()}")
```

### Quantum Network Distribution

```python
from quantum_network_ves import QuantumNetworkVES

# Initialize network with 3 nodes
qn_ves = QuantumNetworkVES(n_nodes=3)

# Distribute shares via quantum teleportation
distribution_log = qn_ves.distribute_shares_via_teleportation(image)

# Create GHZ states for multi-party sharing
ghz_circuit = qn_ves.entanglement_distribution(image)
```

### Threshold Secret Sharing

```python
from quantum_ves import QuantumVisualSecretSharing

# (2, 3) threshold: any 2 of 3 shares can reconstruct
qvss = QuantumVisualSecretSharing(threshold=2, total_shares=3)

# Create shares for a pixel
shares = qvss.create_gf2_shares(secret_pixel=1)

# Reconstruct with any 2 shares
reconstructed = shares[0] ^ shares[1]  # XOR any two shares
```

## Running Demonstrations

### Run Basic Q-VES Demo

```bash
python quantum_ves.py
```

This demonstrates:
- XOR-based quantum sharing
- Entangled share creation
- Image reconstruction
- Circuit visualization

### Run Quantum Network Demo

```bash
python quantum_network_ves.py
```

This demonstrates:
- Quantum teleportation protocol
- GHZ state distribution
- W-state threshold schemes
- Network topology visualization

### Run Comprehensive Examples

```bash
python examples_demo.py
```

This runs all 7 demonstrations:
1. Basic Quantum VES
2. Entanglement-based sharing
3. Threshold secret sharing
4. Quantum network distribution
5. Security analysis
6. Performance comparison
7. Comprehensive visualization

## Project Structure

```
QVES/
├── quantum_ves.py              # Core Q-VES implementation
├── quantum_network_ves.py      # Quantum network extension
├── examples_demo.py            # Comprehensive demonstrations
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── Quantum_networks13112025.pdf  # Research paper
└── [generated outputs]
    ├── quantum_ves_results.png
    ├── quantum_network_topology.png
    └── demo*_*.png
```

## Modules

### `quantum_ves.py`

**Classes:**
- `QuantumVES`: Main class for quantum visual encryption
- `QuantumVisualSecretSharing`: Threshold-based secret sharing

**Key Methods:**
- `encode_pixel_to_quantum_state()`: Encode pixels into quantum states
- `create_quantum_shares()`: Generate quantum shares
- `create_entangled_shares()`: Create Bell state shares
- `xor_based_sharing()`: XOR-based quantum sharing
- `quantum_reconstruct()`: Reconstruct from quantum shares

### `quantum_network_ves.py`

**Classes:**
- `QuantumNode`: Represents a network node
- `QuantumNetworkVES`: Network-based VES

**Key Methods:**
- `quantum_teleportation_protocol()`: Implement quantum teleportation
- `entanglement_distribution()`: Create GHZ states
- `w_state_distribution()`: Generate W-states for threshold schemes
- `distribute_shares_via_teleportation()`: Network share distribution
- `calculate_entanglement_entropy()`: Measure entanglement

## Scientific Background

### Visual Cryptography

Visual cryptography splits a secret image into shares such that:
- Individual shares appear random
- Combining shares reveals the secret
- Perfect secrecy: single shares leak no information

### Quantum Enhancement

Quantum mechanics provides:
1. **Superposition**: Shares exist in multiple states simultaneously
2. **Entanglement**: Non-local correlations between shares
3. **No-Cloning**: Quantum states cannot be copied
4. **Measurement Disturbance**: Eavesdropping is detectable

### Security Model

- **Information-Theoretic Security**: Based on quantum physics, not computational hardness
- **Unconditional Security**: Secure against adversaries with unlimited computational power
- **Eavesdropping Detection**: Quantum measurements disturb the state

## IBM Quantum Integration

### Running on IBM Quantum Hardware

```python
from qiskit_ibm_runtime import QiskitRuntimeService

# Save your IBM Quantum account
QiskitRuntimeService.save_account(token='YOUR_IBM_QUANTUM_TOKEN')

# Load service
service = QiskitRuntimeService()

# Get backend
backend = service.backend('ibm_brisbane')  # or another available backend

# Execute circuit
from qiskit import transpile
transpiled = transpile(circuit, backend=backend)
job = backend.run(transpiled, shots=1024)
result = job.result()
```

### Accessing IBM Quantum

1. Create account at: https://quantum.cloud.ibm.com/
2. Get your API token from account settings
3. Use token in your code as shown above

## Performance Metrics

### Circuit Complexity

For an image of size (h, w):
- **Qubits required**: 2 × h × w (for two shares)
- **Circuit depth**: O(h × w)
- **Gate count**: O(h × w)

### Simulation Limits

Classical simulator limits:
- ~20-25 qubits: Real-time simulation
- ~30 qubits: Requires significant RAM (~8GB)
- ~40+ qubits: Use IBM Quantum hardware

For 4×4 images:
- 32 qubits total (16 per share)
- Feasible on classical simulators

## Security Analysis

### Entropy Analysis

```python
# Shannon entropy of shares should be maximal
import numpy as np

def shannon_entropy(data):
    unique, counts = np.unique(data, return_counts=True)
    probs = counts / counts.sum()
    return -np.sum(probs * np.log2(probs + 1e-10))

# For secure shares: H(Share) ≈ H(Random) = 1.0 bit per pixel
```

### Quantum Security Features

| Property | Classical VES | Quantum VES |
|----------|--------------|-------------|
| Share copying | Possible | Prevented (No-Cloning) |
| Eavesdropping detection | No | Yes (Bell violations) |
| Secure distribution | Requires secure channel | Quantum teleportation |
| Multi-party entanglement | No | Yes (GHZ, W-states) |

## Applications

1. **Secure Image Transmission**: Banking, medical imaging
2. **Authentication**: Visual passwords, biometrics
3. **Watermarking**: Copyright protection
4. **Multi-Party Computation**: Collaborative image analysis
5. **Blockchain Integration**: Quantum-secure NFTs

## Limitations

1. **Image Size**: Limited by available qubits
2. **Noise**: Quantum decoherence affects reconstruction quality
3. **Hardware Access**: Real quantum computers have limited availability
4. **Binary Images**: Current implementation supports binary (black/white) images

## Future Work

- [ ] Grayscale and color image support
- [ ] Error correction codes for noisy channels
- [ ] Integration with QKD protocols
- [ ] Optimized circuits for current hardware
- [ ] Quantum advantage demonstrations
- [ ] Threshold schemes with arbitrary k and n
- [ ] Integration with quantum blockchain

## References

1. Naor, M., & Shamir, A. (1995). Visual cryptography. *Advances in Cryptology—EUROCRYPT'94*.
2. Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*.
3. IBM Quantum Documentation: https://docs.quantum.ibm.com/
4. Qiskit Textbook: https://qiskit.org/learn/

## Contributing

This is a research project. For questions or collaboration:

- Email: [Your Email]
- Institution: Ben-Gurion University (BGU)
- Research Group: Quantum Computing and Cryptography

## License

This project is part of PhD research at Ben-Gurion University.

## Citation

If you use this code in your research, please cite:

```bibtex
@misc{quantum_ves_2025,
  title={Quantum Visual Encryption Scheme: Implementation and Analysis},
  author={[Your Name]},
  year={2025},
  institution={Ben-Gurion University},
  note={Quantum Networks for Visual Cryptography}
}
```

## Acknowledgments

- IBM Quantum for quantum computing access
- Qiskit development team
- Ben-Gurion University, Department of Computer Science
- NVIDIA Corporation (for institutional support)

---

**Last Updated**: November 13, 2025  
**Version**: 1.0.0  
**Status**: Active Development


