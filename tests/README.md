# Test Results Directory

This directory contains test output files from the RBE-VES Quantum Protocol demonstrations.

## Test Files

### test_1.md - Identical Candidate Matching
- **Scenario:** Candidate image identical to secret image
- **Expected Result:** 100% match
- **Purpose:** Verify perfect matching capability

### test_2.md - Partial Match
- **Scenario:** Candidate image with modified middle row
- **Expected Result:** Partial match (varies with image size)
- **Purpose:** Demonstrate pixel-level matching precision

### test_3.md - Complete Mismatch
- **Scenario:** Candidate image with all pixels flipped
- **Expected Result:** 0% match
- **Purpose:** Verify mismatch detection

### test_4_byzantine_5C.md - Byzantine Resilient (Replicated)
- **Scenario:** 5 C participants, 2 Byzantine (malicious)
- **Mode:** Replicated (all Cs get all qubits)
- **Expected Result:** 100% match despite Byzantine participants
- **Purpose:** Demonstrate Byzantine fault tolerance via majority voting

### test_5_distributed_qves.md - Distributed Quantum States
- **Scenario:** 5 C participants, 1 Byzantine, distributed mode
- **Mode:** Distributed (each C gets ≤33% of qubits)
- **Expected Result:** 100% match with enhanced security
- **Purpose:** Demonstrate enhanced security through qubit distribution

## File Structure

Each test file contains:
- **Configuration:** Image size, participants, Byzantine count
- **Protocol Flow:** Detailed execution steps (in verbose mode)
- **Pixel-by-Pixel Processing:** Individual qubit operations (in verbose mode)
- **Results:** Match percentage and analysis
- **Security Analysis:** For Byzantine tests

## Generating New Test Files

```bash
# Basic test generation (default 3×3)
python3 rbe_quantum_ves.py --save

# Custom size test generation
python3 rbe_quantum_ves.py --size 10 --save

# Verbose output with save
python3 rbe_quantum_ves.py --size 8 --verbose --save
```

## Test Output Modes

### Non-Verbose Mode
- Concise summary
- Execution times
- Match percentages
- Minimal details

### Verbose Mode
- Complete pixel-by-pixel processing
- Quantum state transformations
- Individual participant votes
- Key values (θ, φ)
- Majority voting details

## Image Size Impact

Different image sizes demonstrate different aspects:

| Size | Qubits | Best For |
|------|--------|----------|
| 3×3  | 9      | Understanding, debugging |
| 6×6  | 36     | Good distribution demo |
| 10×10| 100    | Performance analysis |
| 15×15| 225    | Scalability testing |

## Security Properties Demonstrated

1. **Information-Theoretic Security**
   - B has keys only, C has quantum states only
   - Neither can decrypt alone

2. **Byzantine Resilience** (Test 4)
   - Majority voting tolerates ⌊(M-1)/2⌋ faulty participants
   - System remains correct with 2/5 Byzantine nodes

3. **Enhanced Security** (Test 5)
   - Each C sees only ≤33% of qubits
   - Compromised participant has limited information
   - Reduces attack surface significantly

4. **Homomorphic CNOT Evaluation**
   - C can transform without learning secret
   - Quantum advantage preserved

## Interpreting Results

### Match Percentage
- **100%:** All pixels matched correctly
- **0%:** Complete mismatch (all pixels different)
- **Partial:** Percentage indicates similarity level

### Byzantine Voting
- Each pixel voted on by multiple Cs
- Majority determines final result
- Honest majority ensures correctness

### Distribution Statistics
```
Qubits per C participant:
  C0: X qubits (Y%)
  ...
```
Shows how qubits are distributed in Test 5.

## File Format

All test files use Markdown format with code blocks for easy viewing:
- Headers indicate test type and configuration
- Code blocks contain protocol output
- Tables show distribution and results

## Version Information

Test files include metadata:
- Image size
- Number of participants
- Byzantine configuration
- Mode (replicated/distributed)

This helps track different experimental configurations.

## Notes

- Files are regenerated on each run with `--save` flag
- Previous results are overwritten
- For long-term storage, copy files to dated directories
- Large image sizes (>10×10) produce large verbose output files

## Related Documentation

- `../README.md` - Main project documentation
- `../SIZE_PARAMETER_GUIDE.md` - Image size parameter guide
- `../DISTRIBUTED_ARCHITECTURE.md` - Distributed mode details
- `../PERFORMANCE_METRICS.md` - Performance analysis

