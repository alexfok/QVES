# Test 2: Matching with Partially Different Candidate

**Image size:** 6×6 (36 pixels)

```
======================================================================
Test 2: Matching with partially different candidate
======================================================================

Images: 6×6, 6/36 pixels different

Phase 1: Encryption by Participant A
--------------------------------------------------
Encrypted 36 pixels using RBE
Transferred 36 RBE keys to Participant B

Phase 2: Secure Image Matching
--------------------------------------------------
Participant C observes candidate image

--- Pixel 0 ---
  Secret T[0] = (encrypted)
  Candidate C[0] = 0
  A → C: QT[0] (encrypted quantum state)
  C skips CNOT (C[0]=0): QT'[0] = QT[0]
  C → B: QT'[0]
  B applies RBE.Dec with key (θ=1.504, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 1 ---
  Secret T[1] = (encrypted)
  Candidate C[1] = 1
  A → C: QT[1] (encrypted quantum state)
  C applies CNOT (C[1]=1): QT[1] → QT'[1]
  C → B: QT'[1]
  B applies RBE.Dec with key (θ=3.948, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 2 ---
  Secret T[2] = (encrypted)
  Candidate C[2] = 0
  A → C: QT[2] (encrypted quantum state)
  C skips CNOT (C[2]=0): QT'[2] = QT[2]
  C → B: QT'[2]
  B applies RBE.Dec with key (θ=4.722, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 3 ---
  Secret T[3] = (encrypted)
  Candidate C[3] = 1
  A → C: QT[3] (encrypted quantum state)
  C applies CNOT (C[3]=1): QT[3] → QT'[3]
  C → B: QT'[3]
  B applies RBE.Dec with key (θ=0.707, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 4 ---
  Secret T[4] = (encrypted)
  Candidate C[4] = 0
  A → C: QT[4] (encrypted quantum state)
  C skips CNOT (C[4]=0): QT'[4] = QT[4]
  C → B: QT'[4]
  B applies RBE.Dec with key (θ=2.573, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 5 ---
  Secret T[5] = (encrypted)
  Candidate C[5] = 1
  A → C: QT[5] (encrypted quantum state)
  C applies CNOT (C[5]=1): QT[5] → QT'[5]
  C → B: QT'[5]
  B applies RBE.Dec with key (θ=6.110, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 6 ---
  Secret T[6] = (encrypted)
  Candidate C[6] = 1
  A → C: QT[6] (encrypted quantum state)
  C applies CNOT (C[6]=1): QT[6] → QT'[6]
  C → B: QT'[6]
  B applies RBE.Dec with key (θ=0.444, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 7 ---
  Secret T[7] = (encrypted)
  Candidate C[7] = 0
  A → C: QT[7] (encrypted quantum state)
  C skips CNOT (C[7]=0): QT'[7] = QT[7]
  C → B: QT'[7]
  B applies RBE.Dec with key (θ=1.877, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 8 ---
  Secret T[8] = (encrypted)
  Candidate C[8] = 1
  A → C: QT[8] (encrypted quantum state)
  C applies CNOT (C[8]=1): QT[8] → QT'[8]
  C → B: QT'[8]
  B applies RBE.Dec with key (θ=6.082, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 9 ---
  Secret T[9] = (encrypted)
  Candidate C[9] = 0
  A → C: QT[9] (encrypted quantum state)
  C skips CNOT (C[9]=0): QT'[9] = QT[9]
  C → B: QT'[9]
  B applies RBE.Dec with key (θ=4.697, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 10 ---
  Secret T[10] = (encrypted)
  Candidate C[10] = 1
  A → C: QT[10] (encrypted quantum state)
  C applies CNOT (C[10]=1): QT[10] → QT'[10]
  C → B: QT'[10]
  B applies RBE.Dec with key (θ=4.565, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 11 ---
  Secret T[11] = (encrypted)
  Candidate C[11] = 0
  A → C: QT[11] (encrypted quantum state)
  C skips CNOT (C[11]=0): QT'[11] = QT[11]
  C → B: QT'[11]
  B applies RBE.Dec with key (θ=5.271, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 12 ---
  Secret T[12] = (encrypted)
  Candidate C[12] = 0
  A → C: QT[12] (encrypted quantum state)
  C skips CNOT (C[12]=0): QT'[12] = QT[12]
  C → B: QT'[12]
  B applies RBE.Dec with key (θ=5.668, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 13 ---
  Secret T[13] = (encrypted)
  Candidate C[13] = 1
  A → C: QT[13] (encrypted quantum state)
  C applies CNOT (C[13]=1): QT[13] → QT'[13]
  C → B: QT'[13]
  B applies RBE.Dec with key (θ=4.630, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 14 ---
  Secret T[14] = (encrypted)
  Candidate C[14] = 0
  A → C: QT[14] (encrypted quantum state)
  C skips CNOT (C[14]=0): QT'[14] = QT[14]
  C → B: QT'[14]
  B applies RBE.Dec with key (θ=5.820, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 15 ---
  Secret T[15] = (encrypted)
  Candidate C[15] = 1
  A → C: QT[15] (encrypted quantum state)
  C applies CNOT (C[15]=1): QT[15] → QT'[15]
  C → B: QT'[15]
  B applies RBE.Dec with key (θ=2.037, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 16 ---
  Secret T[16] = (encrypted)
  Candidate C[16] = 0
  A → C: QT[16] (encrypted quantum state)
  C skips CNOT (C[16]=0): QT'[16] = QT[16]
  C → B: QT'[16]
  B applies RBE.Dec with key (θ=1.364, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 17 ---
  Secret T[17] = (encrypted)
  Candidate C[17] = 1
  A → C: QT[17] (encrypted quantum state)
  C applies CNOT (C[17]=1): QT[17] → QT'[17]
  C → B: QT'[17]
  B applies RBE.Dec with key (θ=4.822, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 18 ---
  Secret T[18] = (encrypted)
  Candidate C[18] = 0
  A → C: QT[18] (encrypted quantum state)
  C skips CNOT (C[18]=0): QT'[18] = QT[18]
  C → B: QT'[18]
  B applies RBE.Dec with key (θ=1.436, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 19 ---
  Secret T[19] = (encrypted)
  Candidate C[19] = 1
  A → C: QT[19] (encrypted quantum state)
  C applies CNOT (C[19]=1): QT[19] → QT'[19]
  C → B: QT'[19]
  B applies RBE.Dec with key (θ=0.590, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 20 ---
  Secret T[20] = (encrypted)
  Candidate C[20] = 0
  A → C: QT[20] (encrypted quantum state)
  C skips CNOT (C[20]=0): QT'[20] = QT[20]
  C → B: QT'[20]
  B applies RBE.Dec with key (θ=4.995, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 21 ---
  Secret T[21] = (encrypted)
  Candidate C[21] = 1
  A → C: QT[21] (encrypted quantum state)
  C applies CNOT (C[21]=1): QT[21] → QT'[21]
  C → B: QT'[21]
  B applies RBE.Dec with key (θ=0.222, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 22 ---
  Secret T[22] = (encrypted)
  Candidate C[22] = 0
  A → C: QT[22] (encrypted quantum state)
  C skips CNOT (C[22]=0): QT'[22] = QT[22]
  C → B: QT'[22]
  B applies RBE.Dec with key (θ=4.156, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 23 ---
  Secret T[23] = (encrypted)
  Candidate C[23] = 1
  A → C: QT[23] (encrypted quantum state)
  C applies CNOT (C[23]=1): QT[23] → QT'[23]
  C → B: QT'[23]
  B applies RBE.Dec with key (θ=2.933, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 24 ---
  Secret T[24] = (encrypted)
  Candidate C[24] = 0
  A → C: QT[24] (encrypted quantum state)
  C skips CNOT (C[24]=0): QT'[24] = QT[24]
  C → B: QT'[24]
  B applies RBE.Dec with key (θ=5.054, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 25 ---
  Secret T[25] = (encrypted)
  Candidate C[25] = 1
  A → C: QT[25] (encrypted quantum state)
  C applies CNOT (C[25]=1): QT[25] → QT'[25]
  C → B: QT'[25]
  B applies RBE.Dec with key (θ=3.555, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 26 ---
  Secret T[26] = (encrypted)
  Candidate C[26] = 0
  A → C: QT[26] (encrypted quantum state)
  C skips CNOT (C[26]=0): QT'[26] = QT[26]
  C → B: QT'[26]
  B applies RBE.Dec with key (θ=4.799, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 27 ---
  Secret T[27] = (encrypted)
  Candidate C[27] = 1
  A → C: QT[27] (encrypted quantum state)
  C applies CNOT (C[27]=1): QT[27] → QT'[27]
  C → B: QT'[27]
  B applies RBE.Dec with key (θ=3.620, φ=1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 28 ---
  Secret T[28] = (encrypted)
  Candidate C[28] = 0
  A → C: QT[28] (encrypted quantum state)
  C skips CNOT (C[28]=0): QT'[28] = QT[28]
  C → B: QT'[28]
  B applies RBE.Dec with key (θ=3.915, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 29 ---
  Secret T[29] = (encrypted)
  Candidate C[29] = 1
  A → C: QT[29] (encrypted quantum state)
  C applies CNOT (C[29]=1): QT[29] → QT'[29]
  C → B: QT'[29]
  B applies RBE.Dec with key (θ=1.015, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 30 ---
  Secret T[30] = (encrypted)
  Candidate C[30] = 1
  A → C: QT[30] (encrypted quantum state)
  C applies CNOT (C[30]=1): QT[30] → QT'[30]
  C → B: QT'[30]
  B applies RBE.Dec with key (θ=1.867, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 31 ---
  Secret T[31] = (encrypted)
  Candidate C[31] = 0
  A → C: QT[31] (encrypted quantum state)
  C skips CNOT (C[31]=0): QT'[31] = QT[31]
  C → B: QT'[31]
  B applies RBE.Dec with key (θ=1.683, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 32 ---
  Secret T[32] = (encrypted)
  Candidate C[32] = 1
  A → C: QT[32] (encrypted quantum state)
  C applies CNOT (C[32]=1): QT[32] → QT'[32]
  C → B: QT'[32]
  B applies RBE.Dec with key (θ=5.285, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 33 ---
  Secret T[33] = (encrypted)
  Candidate C[33] = 0
  A → C: QT[33] (encrypted quantum state)
  C skips CNOT (C[33]=0): QT'[33] = QT[33]
  C → B: QT'[33]
  B applies RBE.Dec with key (θ=2.622, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 34 ---
  Secret T[34] = (encrypted)
  Candidate C[34] = 1
  A → C: QT[34] (encrypted quantum state)
  C applies CNOT (C[34]=1): QT[34] → QT'[34]
  C → B: QT'[34]
  B applies RBE.Dec with key (θ=5.828, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

--- Pixel 35 ---
  Secret T[35] = (encrypted)
  Candidate C[35] = 0
  A → C: QT[35] (encrypted quantum state)
  C skips CNOT (C[35]=0): QT'[35] = QT[35]
  C → B: QT'[35]
  B applies RBE.Dec with key (θ=1.270, φ=-1.571)
  B measures: 0
  Result: ✓ MATCH
  Logic: Match when measurement = 0 (got 0)

Matching complete: 83.3% match
  Matched pixels: 30/36

Result: 83% match (Expected: ~83%)

```
