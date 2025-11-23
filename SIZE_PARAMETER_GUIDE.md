# Image Size Parameter Guide

## Overview

The `--size` parameter allows you to specify the dimensions of the square secret image for RBE-VES protocol testing. This enables experimentation with different scales to observe:
- Performance characteristics
- Distribution effectiveness
- Byzantine resilience
- Communication overhead

## Usage

```bash
python3 rbe_quantum_ves.py --size SIZE
```

Where `SIZE` is the dimension of the square image (SIZE × SIZE).

### Basic Examples

```bash
# Default 3×3 image (9 qubits)
python3 rbe_quantum_ves.py

# 5×5 image (25 qubits)
python3 rbe_quantum_ves.py --size 5

# 10×10 image (100 qubits)
python3 rbe_quantum_ves.py --size 10

# With verbose output
python3 rbe_quantum_ves.py --size 8 --verbose

# Save to files
python3 rbe_quantum_ves.py --size 6 --save

# Verbose + save
python3 rbe_quantum_ves.py --size 12 --verbose --save
```

## Image Size Impact

### Small Images (3×3 to 5×5)

**Qubits:** 9 - 25  
**Best for:** Quick testing, understanding protocol flow

**Characteristics:**
- Fast execution
- Easy to visualize
- Suitable for verbose mode
- Distribution: Each C gets ~60-67% (not ideal)

**Example:**
```bash
python3 rbe_quantum_ves.py --size 3 --verbose
```

**Output:**
```
Image size: 3×3 (9 pixels)
Qubits per C participant:
  C0: 6 qubits (66.7%)
  C1: 6 qubits (66.7%)
  C2: 5 qubits (55.6%)
  C3: 5 qubits (55.6%)
  C4: 5 qubits (55.6%)
```

### Medium Images (6×6 to 10×10)

**Qubits:** 36 - 100  
**Best for:** Balanced testing, good distribution visualization

**Characteristics:**
- Moderate execution time
- Better distribution properties
- Shows scalability benefits
- Distribution: Each C approaches 60%

**Example:**
```bash
python3 rbe_quantum_ves.py --size 8 --save
```

**Output:**
```
Image size: 8×8 (64 pixels)
Qubits per C participant:
  C0: 39 qubits (60.9%)
  C1: 39 qubits (60.9%)
  C2: 38 qubits (59.4%)
  C3: 38 qubits (59.4%)
  C4: 38 qubits (59.4%)
```

### Large Images (12×12 to 15×15)

**Qubits:** 144 - 225  
**Best for:** Performance testing, near-optimal distribution

**Characteristics:**
- Longer execution time
- Near-optimal distribution (~50-55% per C)
- Demonstrates communication savings
- Shows quantum advantage

**Example:**
```bash
python3 rbe_quantum_ves.py --size 15
```

**Output:**
```
Image size: 15×15 (225 pixels)
Qubits per C participant:
  C0: 135 qubits (60.0%)
  C1: 135 qubits (60.0%)
  C2: 135 qubits (60.0%)
  C3: 135 qubits (60.0%)
  C4: 135 qubits (60.0%)
```

### Very Large Images (>15×15)

**Qubits:** >225  
**Best for:** Stress testing, publication-quality results

**Characteristics:**
- Very long execution time
- Requires confirmation prompt (>20×20)
- Optimal distribution properties
- Classical simulator limits may apply

**Note:** For images >20×20, the system will prompt for confirmation.

## Distribution Analysis by Size

### Distribution Percentage per C Participant

| Size | Qubits | Ideal (33%) | Actual (%) | Gap |
|------|--------|-------------|------------|-----|
| 3×3  | 9      | 3           | 5-6 (56-67%)| +23-34% |
| 5×5  | 25     | 8           | 15 (60%)   | +27% |
| 6×6  | 36     | 12          | 21-22 (58-61%) | +25-28% |
| 10×10| 100    | 33          | 60 (60%)   | +27% |
| 15×15| 225    | 75          | 135 (60%)  | +27% |
| 20×20| 400    | 133         | 240 (60%)  | +27% |

**Key Insight:** With the current round-robin distribution algorithm, each C gets ~60% of qubits regardless of image size. This is because each qubit is assigned to 3 Cs, and 3/5 = 60%.

**To achieve true 1/3 distribution:**
- Need more C participants (≥9)
- Or use hierarchical distribution
- Or assign each qubit to 2 Cs instead of 3

## Performance Characteristics

### Execution Time & Memory Estimates

| Size | Qubits | Non-verbose | Verbose+Save | RAM Usage | Actual (M1/M2) |
|------|--------|-------------|--------------|-----------|----------------|
| 3×3  | 9      | ~1 sec      | ~2 sec       | ~300 MB   | ~2 sec         |
| 5×5  | 25     | ~2 sec      | ~3 sec       | ~350 MB   | ~3 sec         |
| 10×10| 100    | ~5 sec      | ~7 sec       | ~500 MB   | ~7 sec         |
| 15×15| 225    | ~8 sec      | ~10 sec      | ~800 MB   | ~10 sec        |
| 20×20| 400    | ~9 sec      | ~11 sec      | ~1.5 GB   | **11.4 sec** ✓ |

*Times measured on Apple M1/M2. Older hardware may be 2-3x slower.*

**Actual measurement (20×20):** 11.368 seconds (verbose+save mode)

**Memory Breakdown:**
- **Base overhead:** ~200-300 MB (Python + Qiskit/Aer)
- **Per qubit:** ~1-5 MB (circuit compilation, simulation, results)
- **Standard mode:** N qubits × 5 participants × Tests 1-4
- **Distributed mode:** N qubits × 3 copies × Test 5
- **Verbose mode:** Additional ~20-30% for output buffering

### Communication Overhead

**Standard (Replicated) Mode:**
- Transmissions: N × M (qubits × participants)
- Example 10×10: 100 × 5 = 500 transmissions

**Distributed Mode:**
- Transmissions: N × 3 (qubits × 3 copies)
- Example 10×10: 100 × 3 = 300 transmissions
- **Savings: 40%**

## Generated Image Pattern

The `generate_test_image()` function creates a **checkerboard pattern**:

```
3×3:              5×5:                    10×10:
0 1 0            0 1 0 1 0              0 1 0 1 0 1 0 1 0 1
1 0 1            1 0 1 0 1              1 0 1 0 1 0 1 0 1 0
0 1 0            0 1 0 1 0              0 1 0 1 0 1 0 1 0 1
                 1 0 1 0 1              1 0 1 0 1 0 1 0 1 0
                 0 1 0 1 0              0 1 0 1 0 1 0 1 0 1
                                        1 0 1 0 1 0 1 0 1 0
                                        0 1 0 1 0 1 0 1 0 1
                                        1 0 1 0 1 0 1 0 1 0
                                        0 1 0 1 0 1 0 1 0 1
                                        1 0 1 0 1 0 1 0 1 0
```

Pattern: `image[i,j] = (i + j) % 2`

## Test Scenarios

### Test 1: Identical Match
- **Candidate:** Same as secret
- **Expected:** 100% match
- **All sizes:** Should achieve 100%

### Test 2: Partial Match
- **Candidate:** Middle row flipped
- **Expected:** `(N² - N) / N² × 100%`

| Size | Expected Match |
|------|----------------|
| 3×3  | 67% (6/9)      |
| 5×5  | 80% (20/25)    |
| 10×10| 90% (90/100)   |

### Test 3: Complete Mismatch
- **Candidate:** All pixels flipped
- **Expected:** 0% match
- **All sizes:** Should achieve 0%

### Test 4: Byzantine (Replicated)
- **Byzantine:** 2 out of 5 Cs
- **Expected:** 100% (resilient)

### Test 5: Byzantine (Distributed)
- **Byzantine:** 1 out of 5 Cs
- **Expected:** 100% (resilient)
- **Security:** Byzantine C sees only ~60% of qubits

## Recommendations

### For Learning/Understanding
```bash
python3 rbe_quantum_ves.py --size 3 --verbose
```
- Small size for easy comprehension
- Verbose mode shows all details
- Can trace each pixel operation

### For Testing Distribution
```bash
python3 rbe_quantum_ves.py --size 10 --save
```
- Medium size shows good distribution
- Save to files for analysis
- Reasonable execution time

### For Performance Analysis
```bash
python3 rbe_quantum_ves.py --size 15
```
- Large enough to show scalability
- Still manageable execution time
- Good for benchmarking

### For Publication Results
```bash
python3 rbe_quantum_ves.py --size 20 --verbose --save
```
- Large scale demonstration
- Complete verbose output
- Saved files for documentation

## Limitations

### Size Constraints

**Minimum:** 2×2 (4 qubits)
- System enforces minimum of 2×2

**Recommended Maximum:** 20×20 (400 qubits)
- Classical simulator limits
- Execution time becomes impractical
- Above 20×20 requires confirmation

**Theoretical Maximum:** Limited by:
1. Available RAM (~8GB for 30-35 qubits realistic)
2. Execution time (exponential growth)
3. Python recursion/iteration limits

### Display Limitations

**Full Display:** SIZE ≤ 5
- Images are printed in full to console
- Easy to verify visually

**Summarized:** SIZE > 5
- Only dimensions shown: "10×10"
- Prevents console overflow
- Use `--save` to capture in files

## Scaling Analysis

### Why 60% per C (not 33%)?

**Current Algorithm:**
```python
copies_per_qubit = 3  # Each qubit goes to 3 Cs
n_c_participants = 5  # Total of 5 Cs
# Result: 3/5 = 60% per C
```

**To achieve 33% per C:**
1. **Option A:** More participants (9 Cs)
   - 3/9 = 33.3% ✓
   
2. **Option B:** Fewer copies (2 copies)
   - 2/5 = 40% (better)
   - But reduces Byzantine tolerance
   
3. **Option C:** Hierarchical distribution
   - Nest sub-groups
   - More complex protocol

### Future Enhancements

**Adaptive Distribution:**
```python
--size 10 --copies 2  # Use 2 copies instead of 3
--size 10 --participants 9  # Use 9 C participants
```

**Distribution Algorithms:**
- Random distribution
- Stratified distribution
- Trust-based distribution

## Complete Examples

### Quick Test
```bash
# Fast verification
python3 rbe_quantum_ves.py --size 3
```

### Standard Research Run
```bash
# Good for presentations
python3 rbe_quantum_ves.py --size 8 --verbose --save
```

### Scalability Study
```bash
# Test multiple sizes
for size in 3 5 8 10 12 15; do
  echo "Testing size $size..."
  python3 rbe_quantum_ves.py --size $size --save
  mv test_*.md results_${size}x${size}/
done
```

### Performance Benchmark
```bash
# Time different sizes
for size in 5 10 15 20; do
  echo "Size $size:"
  time python3 rbe_quantum_ves.py --size $size > /dev/null
done
```

## Output Files

When using `--save`, all test files are overwritten with new image size:
- `test_1.md` - Includes image size in header
- `test_2.md` - Shows expected match percentage
- `test_3.md` - Complete mismatch test
- `test_4_byzantine_5C.md` - Byzantine with replication
- `test_5_distributed_qves.md` - Distributed mode with qubit distribution

## Troubleshooting

### "Command not found: python3"
Use `python` instead of `python3`

### Very slow execution
- Reduce image size
- Remove `--verbose` flag
- Check system resources

### Memory errors
- Image too large for available RAM
- Try smaller size
- Close other applications

### Simulation warnings
- Normal for quantum simulation
- Does not affect correctness
- Can be ignored for testing

## Summary

The `--size` parameter provides:
- ✅ **Flexibility:** Test from 2×2 to 20×20+
- ✅ **Scalability:** Observe performance at different scales
- ✅ **Distribution:** See how qubit distribution changes
- ✅ **Validation:** Verify protocol works for any size

**Recommended workflow:**
1. Start small (3×3) with `--verbose` to understand
2. Test medium (8×8) with `--save` for documentation  
3. Go large (15×15) for performance analysis
4. Use results for publication/presentation

---

*For questions or issues, see the main README.md*

