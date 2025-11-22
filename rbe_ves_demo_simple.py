"""
Simplified RBE-VES Demonstration (No Qiskit Required)
Shows the algorithm logic from the paper without quantum simulation
"""

import numpy as np


class RBEVESSimple:
    """
    Simplified demonstration of RBE-based Quantum VES protocol
    """
    
    def __init__(self):
        self.secret_image = None
        self.rbe_keys = {}
        self.encrypted_qubits = {}
    
    def setup_secret_image(self, image: np.ndarray):
        """
        Phase 1: Participant A encrypts the secret image
        
        For each pixel T[i]:
          1. Generate random key (θ, φ)
          2. Encrypt: QT[i] = K_{θ,φ} |T[i]⟩
          3. Send QT[i] to storage, (θ, φ) to Participant B
        """
        self.secret_image = image.flatten()
        
        print("\n" + "="*60)
        print("PHASE 1: ENCRYPTION BY PARTICIPANT A")
        print("="*60)
        
        for i, pixel_value in enumerate(self.secret_image):
            # Generate random RBE key
            theta = np.random.uniform(0, 2 * np.pi)
            phi = np.random.choice([-np.pi/2, np.pi/2])
            
            self.rbe_keys[i] = (theta, phi)
            
            # Simulate quantum encryption (in reality this creates a qubit)
            # We store the original value for simulation purposes
            self.encrypted_qubits[i] = pixel_value
            
            print(f"  Pixel {i}: T[{i}]={pixel_value} → "
                  f"RBE.Enc with key (θ={theta:.3f}, φ={phi:.3f})")
        
        print(f"\n✓ Encrypted {len(self.secret_image)} pixels")
        print(f"✓ Sent {len(self.rbe_keys)} RBE keys to Participant B")
    
    def perform_matching(self, candidate_image: np.ndarray):
        """
        Phase 2: Secure Image Matching
        
        For each pixel i:
          1. A sends QT[i] to C
          2. C observes C[i] and applies:
             - If C[i] = 0: no operation
             - If C[i] = 1: apply CNOT (flips bit)
          3. C sends QT'[i] to B
          4. B applies RBE.Dec and measures
          5. Match if result = |0⟩
        """
        candidate = candidate_image.flatten()
        
        print("\n" + "="*60)
        print("PHASE 2: SECURE IMAGE MATCHING")
        print("="*60)
        
        print(f"\nParticipant C observes candidate image")
        
        matches = []
        
        for i in range(len(self.secret_image)):
            T_i = self.secret_image[i]
            C_i = candidate[i]
            
            print(f"\n--- Pixel {i} ---")
            print(f"  Secret T[{i}] = {T_i} (encrypted)")
            print(f"  Candidate C[{i}] = {C_i}")
            
            # Simulate the protocol
            # A sends QT[i] to C
            qt_i = self.encrypted_qubits[i]  # Encrypted qubit
            print(f"  A → C: QT[{i}] (encrypted state)")
            
            # C applies conditional CNOT
            if C_i == 1:
                qt_i_transformed = 1 - qt_i  # CNOT flips the bit
                print(f"  C applies CNOT (C[{i}]=1): QT[{i}] → QT'[{i}]")
            else:
                qt_i_transformed = qt_i
                print(f"  C skips CNOT (C[{i}]=0): QT'[{i}] = QT[{i}]")
            
            print(f"  C → B: QT'[{i}]")
            
            # B decrypts using RBE key
            theta, phi = self.rbe_keys[i]
            decrypted_bit = qt_i_transformed  # After RBE.Dec
            
            print(f"  B applies RBE.Dec with key (θ={theta:.3f}, φ={phi:.3f})")
            print(f"  B measures: {decrypted_bit}")
            
            # Determine match
            is_match = (decrypted_bit == 0)
            matches.append(is_match)
            
            # Explanation
            print(f"  Result: {'✓ MATCH' if is_match else '✗ MISMATCH'}")
            
            # Show the logic
            xor_result = T_i ^ C_i
            print(f"  Logic: T[{i}] ⊕ C[{i}] = {T_i} ⊕ {C_i} = {xor_result}")
            print(f"         (Match when XOR = 0)")
        
        match_percentage = (sum(matches) / len(matches)) * 100
        
        print("\n" + "="*60)
        print(f"MATCHING RESULT: {match_percentage:.1f}% match")
        print(f"  Matched pixels: {sum(matches)}/{len(matches)}")
        print("="*60)
        
        return matches, match_percentage


def demonstrate_protocol():
    """Main demonstration"""
    
    print("\n" + "="*60)
    print("RBE-BASED QUANTUM VISUAL ENCRYPTION SCHEME")
    print("Implementation from paper:")
    print("'Quantum Perfect Output VES in Spite of Swarm Byzantine Participants'")
    print("="*60)
    
    # Create secret image
    secret_image = np.array([[1, 0, 1],
                             [0, 1, 0],
                             [1, 0, 1]], dtype=int)
    
    print("\nSecret Image (3x3):")
    print(secret_image)
    
    # Initialize system
    qves = RBEVESSimple()
    
    # Phase 1: Encryption
    qves.setup_secret_image(secret_image)
    
    # Test 1: Perfect match
    print("\n\n" + "#"*60)
    print("# TEST 1: IDENTICAL CANDIDATE")
    print("#"*60)
    
    candidate_same = secret_image.copy()
    print("\nCandidate Image:")
    print(candidate_same)
    
    matches, percentage = qves.perform_matching(candidate_same)
    
    # Test 2: Partial match
    print("\n\n" + "#"*60)
    print("# TEST 2: PARTIALLY DIFFERENT CANDIDATE")
    print("#"*60)
    
    qves2 = RBEVESSimple()
    qves2.setup_secret_image(secret_image)
    
    candidate_partial = np.array([[1, 0, 1],
                                  [1, 1, 1],  # Different row
                                  [1, 0, 1]], dtype=int)
    print("\nCandidate Image:")
    print(candidate_partial)
    
    matches, percentage = qves2.perform_matching(candidate_partial)
    
    # Test 3: No match
    print("\n\n" + "#"*60)
    print("# TEST 3: COMPLETELY DIFFERENT CANDIDATE")
    print("#"*60)
    
    qves3 = RBEVESSimple()
    qves3.setup_secret_image(secret_image)
    
    candidate_diff = 1 - secret_image  # Flip all bits
    print("\nCandidate Image:")
    print(candidate_diff)
    
    matches, percentage = qves3.perform_matching(candidate_diff)
    
    # Summary
    print("\n\n" + "="*60)
    print("KEY PROPERTIES OF THE SCHEME")
    print("="*60)
    print("""
1. PARTICIPANT ROLES:
   - A: Encrypts pixels using RBE, stores encrypted qubits
   - B: Holds decryption keys (θ, φ)
   - C: Observes candidate and applies conditional CNOT

2. MATCHING PROTOCOL:
   - A sends QT[i] to C
   - C applies CNOT if C[i] = 1
   - C sends transformed QT'[i] to B
   - B decrypts and measures
   - Match if result = |0⟩

3. SECURITY FEATURES:
   ✓ Information-theoretic security
   ✓ No single participant knows both secret and keys
   ✓ Homomorphic CNOT operation (C doesn't learn T[i])
   ✓ No-cloning theorem prevents copying
   ✓ Byzantine resilience via majority voting

4. MATCHING LOGIC (from Lemma in paper):
   RBE.Dec(QT'[i]) = T[i] ⊕ C[i]
   Match when: T[i] ⊕ C[i] = 0
   Therefore: T[i] = C[i]
""")
    
    print("="*60)
    print("DEMONSTRATION COMPLETE!")
    print("="*60)
    print("\nTo run with actual quantum simulation:")
    print("1. Install Qiskit: pip install -r requirements.txt")
    print("2. Run: python3 rbe_quantum_ves.py")
    print()


if __name__ == "__main__":
    demonstrate_protocol()


