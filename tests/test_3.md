# Test 3: Matching with Completely Different Candidate

**Image size:** 6×6 (36 pixels)

```
======================================================================
Test 3: Matching with completely different candidate
======================================================================

Images: 6×6 (all pixels flipped)

Phase 1: Encryption by Participant A
--------------------------------------------------
Encrypted 36 pixels using RBE
Transferred 36 RBE keys to Participant B

Phase 2: Secure Image Matching
--------------------------------------------------
Participant C observes candidate image

--- Pixel 0 ---
  Secret T[0] = (encrypted)
  Candidate C[0] = 1
  A → C: QT[0] (encrypted quantum state)
  C applies CNOT (C[0]=1): QT[0] → QT'[0]
  C → B: QT'[0]
  B applies RBE.Dec with key (θ=1.841, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 1 ---
  Secret T[1] = (encrypted)
  Candidate C[1] = 0
  A → C: QT[1] (encrypted quantum state)
  C skips CNOT (C[1]=0): QT'[1] = QT[1]
  C → B: QT'[1]
  B applies RBE.Dec with key (θ=4.748, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 2 ---
  Secret T[2] = (encrypted)
  Candidate C[2] = 1
  A → C: QT[2] (encrypted quantum state)
  C applies CNOT (C[2]=1): QT[2] → QT'[2]
  C → B: QT'[2]
  B applies RBE.Dec with key (θ=0.201, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 3 ---
  Secret T[3] = (encrypted)
  Candidate C[3] = 0
  A → C: QT[3] (encrypted quantum state)
  C skips CNOT (C[3]=0): QT'[3] = QT[3]
  C → B: QT'[3]
  B applies RBE.Dec with key (θ=3.030, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 4 ---
  Secret T[4] = (encrypted)
  Candidate C[4] = 1
  A → C: QT[4] (encrypted quantum state)
  C applies CNOT (C[4]=1): QT[4] → QT'[4]
  C → B: QT'[4]
  B applies RBE.Dec with key (θ=0.626, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 5 ---
  Secret T[5] = (encrypted)
  Candidate C[5] = 0
  A → C: QT[5] (encrypted quantum state)
  C skips CNOT (C[5]=0): QT'[5] = QT[5]
  C → B: QT'[5]
  B applies RBE.Dec with key (θ=3.797, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 6 ---
  Secret T[6] = (encrypted)
  Candidate C[6] = 0
  A → C: QT[6] (encrypted quantum state)
  C skips CNOT (C[6]=0): QT'[6] = QT[6]
  C → B: QT'[6]
  B applies RBE.Dec with key (θ=3.222, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 7 ---
  Secret T[7] = (encrypted)
  Candidate C[7] = 1
  A → C: QT[7] (encrypted quantum state)
  C applies CNOT (C[7]=1): QT[7] → QT'[7]
  C → B: QT'[7]
  B applies RBE.Dec with key (θ=0.120, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 8 ---
  Secret T[8] = (encrypted)
  Candidate C[8] = 0
  A → C: QT[8] (encrypted quantum state)
  C skips CNOT (C[8]=0): QT'[8] = QT[8]
  C → B: QT'[8]
  B applies RBE.Dec with key (θ=4.283, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 9 ---
  Secret T[9] = (encrypted)
  Candidate C[9] = 1
  A → C: QT[9] (encrypted quantum state)
  C applies CNOT (C[9]=1): QT[9] → QT'[9]
  C → B: QT'[9]
  B applies RBE.Dec with key (θ=1.283, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 10 ---
  Secret T[10] = (encrypted)
  Candidate C[10] = 0
  A → C: QT[10] (encrypted quantum state)
  C skips CNOT (C[10]=0): QT'[10] = QT[10]
  C → B: QT'[10]
  B applies RBE.Dec with key (θ=2.895, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 11 ---
  Secret T[11] = (encrypted)
  Candidate C[11] = 1
  A → C: QT[11] (encrypted quantum state)
  C applies CNOT (C[11]=1): QT[11] → QT'[11]
  C → B: QT'[11]
  B applies RBE.Dec with key (θ=0.512, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 12 ---
  Secret T[12] = (encrypted)
  Candidate C[12] = 1
  A → C: QT[12] (encrypted quantum state)
  C applies CNOT (C[12]=1): QT[12] → QT'[12]
  C → B: QT'[12]
  B applies RBE.Dec with key (θ=5.585, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 13 ---
  Secret T[13] = (encrypted)
  Candidate C[13] = 0
  A → C: QT[13] (encrypted quantum state)
  C skips CNOT (C[13]=0): QT'[13] = QT[13]
  C → B: QT'[13]
  B applies RBE.Dec with key (θ=3.831, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 14 ---
  Secret T[14] = (encrypted)
  Candidate C[14] = 1
  A → C: QT[14] (encrypted quantum state)
  C applies CNOT (C[14]=1): QT[14] → QT'[14]
  C → B: QT'[14]
  B applies RBE.Dec with key (θ=5.269, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 15 ---
  Secret T[15] = (encrypted)
  Candidate C[15] = 0
  A → C: QT[15] (encrypted quantum state)
  C skips CNOT (C[15]=0): QT'[15] = QT[15]
  C → B: QT'[15]
  B applies RBE.Dec with key (θ=2.670, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 16 ---
  Secret T[16] = (encrypted)
  Candidate C[16] = 1
  A → C: QT[16] (encrypted quantum state)
  C applies CNOT (C[16]=1): QT[16] → QT'[16]
  C → B: QT'[16]
  B applies RBE.Dec with key (θ=2.566, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 17 ---
  Secret T[17] = (encrypted)
  Candidate C[17] = 0
  A → C: QT[17] (encrypted quantum state)
  C skips CNOT (C[17]=0): QT'[17] = QT[17]
  C → B: QT'[17]
  B applies RBE.Dec with key (θ=3.055, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 18 ---
  Secret T[18] = (encrypted)
  Candidate C[18] = 0
  A → C: QT[18] (encrypted quantum state)
  C skips CNOT (C[18]=0): QT'[18] = QT[18]
  C → B: QT'[18]
  B applies RBE.Dec with key (θ=1.644, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 19 ---
  Secret T[19] = (encrypted)
  Candidate C[19] = 1
  A → C: QT[19] (encrypted quantum state)
  C applies CNOT (C[19]=1): QT[19] → QT'[19]
  C → B: QT'[19]
  B applies RBE.Dec with key (θ=2.029, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 20 ---
  Secret T[20] = (encrypted)
  Candidate C[20] = 0
  A → C: QT[20] (encrypted quantum state)
  C skips CNOT (C[20]=0): QT'[20] = QT[20]
  C → B: QT'[20]
  B applies RBE.Dec with key (θ=6.222, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 21 ---
  Secret T[21] = (encrypted)
  Candidate C[21] = 1
  A → C: QT[21] (encrypted quantum state)
  C applies CNOT (C[21]=1): QT[21] → QT'[21]
  C → B: QT'[21]
  B applies RBE.Dec with key (θ=2.390, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 22 ---
  Secret T[22] = (encrypted)
  Candidate C[22] = 0
  A → C: QT[22] (encrypted quantum state)
  C skips CNOT (C[22]=0): QT'[22] = QT[22]
  C → B: QT'[22]
  B applies RBE.Dec with key (θ=4.461, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 23 ---
  Secret T[23] = (encrypted)
  Candidate C[23] = 1
  A → C: QT[23] (encrypted quantum state)
  C applies CNOT (C[23]=1): QT[23] → QT'[23]
  C → B: QT'[23]
  B applies RBE.Dec with key (θ=2.287, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 24 ---
  Secret T[24] = (encrypted)
  Candidate C[24] = 1
  A → C: QT[24] (encrypted quantum state)
  C applies CNOT (C[24]=1): QT[24] → QT'[24]
  C → B: QT'[24]
  B applies RBE.Dec with key (θ=3.116, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 25 ---
  Secret T[25] = (encrypted)
  Candidate C[25] = 0
  A → C: QT[25] (encrypted quantum state)
  C skips CNOT (C[25]=0): QT'[25] = QT[25]
  C → B: QT'[25]
  B applies RBE.Dec with key (θ=5.118, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 26 ---
  Secret T[26] = (encrypted)
  Candidate C[26] = 1
  A → C: QT[26] (encrypted quantum state)
  C applies CNOT (C[26]=1): QT[26] → QT'[26]
  C → B: QT'[26]
  B applies RBE.Dec with key (θ=6.076, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 27 ---
  Secret T[27] = (encrypted)
  Candidate C[27] = 0
  A → C: QT[27] (encrypted quantum state)
  C skips CNOT (C[27]=0): QT'[27] = QT[27]
  C → B: QT'[27]
  B applies RBE.Dec with key (θ=4.342, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 28 ---
  Secret T[28] = (encrypted)
  Candidate C[28] = 1
  A → C: QT[28] (encrypted quantum state)
  C applies CNOT (C[28]=1): QT[28] → QT'[28]
  C → B: QT'[28]
  B applies RBE.Dec with key (θ=5.166, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 29 ---
  Secret T[29] = (encrypted)
  Candidate C[29] = 0
  A → C: QT[29] (encrypted quantum state)
  C skips CNOT (C[29]=0): QT'[29] = QT[29]
  C → B: QT'[29]
  B applies RBE.Dec with key (θ=2.011, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 30 ---
  Secret T[30] = (encrypted)
  Candidate C[30] = 0
  A → C: QT[30] (encrypted quantum state)
  C skips CNOT (C[30]=0): QT'[30] = QT[30]
  C → B: QT'[30]
  B applies RBE.Dec with key (θ=4.713, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 31 ---
  Secret T[31] = (encrypted)
  Candidate C[31] = 1
  A → C: QT[31] (encrypted quantum state)
  C applies CNOT (C[31]=1): QT[31] → QT'[31]
  C → B: QT'[31]
  B applies RBE.Dec with key (θ=2.625, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 32 ---
  Secret T[32] = (encrypted)
  Candidate C[32] = 0
  A → C: QT[32] (encrypted quantum state)
  C skips CNOT (C[32]=0): QT'[32] = QT[32]
  C → B: QT'[32]
  B applies RBE.Dec with key (θ=1.732, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 33 ---
  Secret T[33] = (encrypted)
  Candidate C[33] = 1
  A → C: QT[33] (encrypted quantum state)
  C applies CNOT (C[33]=1): QT[33] → QT'[33]
  C → B: QT'[33]
  B applies RBE.Dec with key (θ=1.367, φ=-1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 34 ---
  Secret T[34] = (encrypted)
  Candidate C[34] = 0
  A → C: QT[34] (encrypted quantum state)
  C skips CNOT (C[34]=0): QT'[34] = QT[34]
  C → B: QT'[34]
  B applies RBE.Dec with key (θ=2.143, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

--- Pixel 35 ---
  Secret T[35] = (encrypted)
  Candidate C[35] = 1
  A → C: QT[35] (encrypted quantum state)
  C applies CNOT (C[35]=1): QT[35] → QT'[35]
  C → B: QT'[35]
  B applies RBE.Dec with key (θ=0.659, φ=1.571)
  B measures: 1
  Result: ✗ MISMATCH
  Logic: Match when measurement = 0 (got 1)

Matching complete: 0.0% match
  Matched pixels: 0/36

Result: 0% match (Expected: 0%)

```
