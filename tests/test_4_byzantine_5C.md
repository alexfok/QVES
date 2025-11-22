# Test 4: Byzantine-Resilient Quantum VES

**Configuration:** 5 C participants, 2 Byzantine
**Image size:** 6×6 (36 pixels)

```
======================================================================
Test 4: Byzantine-Resilient Quantum VES (5 C participants, 2 Byzantine)
======================================================================

Image size: 6×6 (36 pixels)

Secret Image: 6×6

Candidate Image: 6×6 (identical to secret)

Byzantine-Resilient Matching
Mode: REPLICATED (each C gets all qubits)
--------------------------------------------------
Total C participants: 5
Byzantine participants: 2

  C participant 0: Honest (observes correct image)
  C participant 1: Byzantine (observes flipped image)
  C participant 2: Honest (observes correct image)
  C participant 3: Byzantine (observes flipped image)
  C participant 4: Honest (observes correct image)

--- Pixel 0 ---
  Candidate C[0] = 0
  A broadcasts QT[0] to all 5 C participants
  C0 → B: QT'[0], B measures: 0, Vote: MATCH
  C1 → B: QT'[0], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[0], B measures: 0, Vote: MATCH
  C3 → B: QT'[0], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[0], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 1 ---
  Candidate C[1] = 1
  A broadcasts QT[1] to all 5 C participants
  C0 → B: QT'[1], B measures: 0, Vote: MATCH
  C1 → B: QT'[1], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[1], B measures: 0, Vote: MATCH
  C3 → B: QT'[1], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[1], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 2 ---
  Candidate C[2] = 0
  A broadcasts QT[2] to all 5 C participants
  C0 → B: QT'[2], B measures: 0, Vote: MATCH
  C1 → B: QT'[2], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[2], B measures: 0, Vote: MATCH
  C3 → B: QT'[2], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[2], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 3 ---
  Candidate C[3] = 1
  A broadcasts QT[3] to all 5 C participants
  C0 → B: QT'[3], B measures: 0, Vote: MATCH
  C1 → B: QT'[3], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[3], B measures: 0, Vote: MATCH
  C3 → B: QT'[3], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[3], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 4 ---
  Candidate C[4] = 0
  A broadcasts QT[4] to all 5 C participants
  C0 → B: QT'[4], B measures: 0, Vote: MATCH
  C1 → B: QT'[4], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[4], B measures: 0, Vote: MATCH
  C3 → B: QT'[4], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[4], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 5 ---
  Candidate C[5] = 1
  A broadcasts QT[5] to all 5 C participants
  C0 → B: QT'[5], B measures: 0, Vote: MATCH
  C1 → B: QT'[5], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[5], B measures: 0, Vote: MATCH
  C3 → B: QT'[5], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[5], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 6 ---
  Candidate C[6] = 1
  A broadcasts QT[6] to all 5 C participants
  C0 → B: QT'[6], B measures: 0, Vote: MATCH
  C1 → B: QT'[6], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[6], B measures: 0, Vote: MATCH
  C3 → B: QT'[6], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[6], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 7 ---
  Candidate C[7] = 0
  A broadcasts QT[7] to all 5 C participants
  C0 → B: QT'[7], B measures: 0, Vote: MATCH
  C1 → B: QT'[7], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[7], B measures: 0, Vote: MATCH
  C3 → B: QT'[7], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[7], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 8 ---
  Candidate C[8] = 1
  A broadcasts QT[8] to all 5 C participants
  C0 → B: QT'[8], B measures: 0, Vote: MATCH
  C1 → B: QT'[8], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[8], B measures: 0, Vote: MATCH
  C3 → B: QT'[8], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[8], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 9 ---
  Candidate C[9] = 0
  A broadcasts QT[9] to all 5 C participants
  C0 → B: QT'[9], B measures: 0, Vote: MATCH
  C1 → B: QT'[9], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[9], B measures: 0, Vote: MATCH
  C3 → B: QT'[9], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[9], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 10 ---
  Candidate C[10] = 1
  A broadcasts QT[10] to all 5 C participants
  C0 → B: QT'[10], B measures: 0, Vote: MATCH
  C1 → B: QT'[10], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[10], B measures: 0, Vote: MATCH
  C3 → B: QT'[10], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[10], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 11 ---
  Candidate C[11] = 0
  A broadcasts QT[11] to all 5 C participants
  C0 → B: QT'[11], B measures: 0, Vote: MATCH
  C1 → B: QT'[11], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[11], B measures: 0, Vote: MATCH
  C3 → B: QT'[11], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[11], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 12 ---
  Candidate C[12] = 0
  A broadcasts QT[12] to all 5 C participants
  C0 → B: QT'[12], B measures: 0, Vote: MATCH
  C1 → B: QT'[12], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[12], B measures: 0, Vote: MATCH
  C3 → B: QT'[12], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[12], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 13 ---
  Candidate C[13] = 1
  A broadcasts QT[13] to all 5 C participants
  C0 → B: QT'[13], B measures: 0, Vote: MATCH
  C1 → B: QT'[13], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[13], B measures: 0, Vote: MATCH
  C3 → B: QT'[13], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[13], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 14 ---
  Candidate C[14] = 0
  A broadcasts QT[14] to all 5 C participants
  C0 → B: QT'[14], B measures: 0, Vote: MATCH
  C1 → B: QT'[14], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[14], B measures: 0, Vote: MATCH
  C3 → B: QT'[14], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[14], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 15 ---
  Candidate C[15] = 1
  A broadcasts QT[15] to all 5 C participants
  C0 → B: QT'[15], B measures: 0, Vote: MATCH
  C1 → B: QT'[15], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[15], B measures: 0, Vote: MATCH
  C3 → B: QT'[15], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[15], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 16 ---
  Candidate C[16] = 0
  A broadcasts QT[16] to all 5 C participants
  C0 → B: QT'[16], B measures: 0, Vote: MATCH
  C1 → B: QT'[16], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[16], B measures: 0, Vote: MATCH
  C3 → B: QT'[16], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[16], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 17 ---
  Candidate C[17] = 1
  A broadcasts QT[17] to all 5 C participants
  C0 → B: QT'[17], B measures: 0, Vote: MATCH
  C1 → B: QT'[17], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[17], B measures: 0, Vote: MATCH
  C3 → B: QT'[17], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[17], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 18 ---
  Candidate C[18] = 1
  A broadcasts QT[18] to all 5 C participants
  C0 → B: QT'[18], B measures: 0, Vote: MATCH
  C1 → B: QT'[18], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[18], B measures: 0, Vote: MATCH
  C3 → B: QT'[18], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[18], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 19 ---
  Candidate C[19] = 0
  A broadcasts QT[19] to all 5 C participants
  C0 → B: QT'[19], B measures: 0, Vote: MATCH
  C1 → B: QT'[19], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[19], B measures: 0, Vote: MATCH
  C3 → B: QT'[19], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[19], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 20 ---
  Candidate C[20] = 1
  A broadcasts QT[20] to all 5 C participants
  C0 → B: QT'[20], B measures: 0, Vote: MATCH
  C1 → B: QT'[20], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[20], B measures: 0, Vote: MATCH
  C3 → B: QT'[20], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[20], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 21 ---
  Candidate C[21] = 0
  A broadcasts QT[21] to all 5 C participants
  C0 → B: QT'[21], B measures: 0, Vote: MATCH
  C1 → B: QT'[21], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[21], B measures: 0, Vote: MATCH
  C3 → B: QT'[21], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[21], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 22 ---
  Candidate C[22] = 1
  A broadcasts QT[22] to all 5 C participants
  C0 → B: QT'[22], B measures: 0, Vote: MATCH
  C1 → B: QT'[22], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[22], B measures: 0, Vote: MATCH
  C3 → B: QT'[22], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[22], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 23 ---
  Candidate C[23] = 0
  A broadcasts QT[23] to all 5 C participants
  C0 → B: QT'[23], B measures: 0, Vote: MATCH
  C1 → B: QT'[23], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[23], B measures: 0, Vote: MATCH
  C3 → B: QT'[23], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[23], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 24 ---
  Candidate C[24] = 0
  A broadcasts QT[24] to all 5 C participants
  C0 → B: QT'[24], B measures: 0, Vote: MATCH
  C1 → B: QT'[24], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[24], B measures: 0, Vote: MATCH
  C3 → B: QT'[24], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[24], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 25 ---
  Candidate C[25] = 1
  A broadcasts QT[25] to all 5 C participants
  C0 → B: QT'[25], B measures: 0, Vote: MATCH
  C1 → B: QT'[25], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[25], B measures: 0, Vote: MATCH
  C3 → B: QT'[25], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[25], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 26 ---
  Candidate C[26] = 0
  A broadcasts QT[26] to all 5 C participants
  C0 → B: QT'[26], B measures: 0, Vote: MATCH
  C1 → B: QT'[26], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[26], B measures: 0, Vote: MATCH
  C3 → B: QT'[26], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[26], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 27 ---
  Candidate C[27] = 1
  A broadcasts QT[27] to all 5 C participants
  C0 → B: QT'[27], B measures: 0, Vote: MATCH
  C1 → B: QT'[27], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[27], B measures: 0, Vote: MATCH
  C3 → B: QT'[27], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[27], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 28 ---
  Candidate C[28] = 0
  A broadcasts QT[28] to all 5 C participants
  C0 → B: QT'[28], B measures: 0, Vote: MATCH
  C1 → B: QT'[28], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[28], B measures: 0, Vote: MATCH
  C3 → B: QT'[28], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[28], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 29 ---
  Candidate C[29] = 1
  A broadcasts QT[29] to all 5 C participants
  C0 → B: QT'[29], B measures: 0, Vote: MATCH
  C1 → B: QT'[29], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[29], B measures: 0, Vote: MATCH
  C3 → B: QT'[29], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[29], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 30 ---
  Candidate C[30] = 1
  A broadcasts QT[30] to all 5 C participants
  C0 → B: QT'[30], B measures: 0, Vote: MATCH
  C1 → B: QT'[30], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[30], B measures: 0, Vote: MATCH
  C3 → B: QT'[30], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[30], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 31 ---
  Candidate C[31] = 0
  A broadcasts QT[31] to all 5 C participants
  C0 → B: QT'[31], B measures: 0, Vote: MATCH
  C1 → B: QT'[31], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[31], B measures: 0, Vote: MATCH
  C3 → B: QT'[31], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[31], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 32 ---
  Candidate C[32] = 1
  A broadcasts QT[32] to all 5 C participants
  C0 → B: QT'[32], B measures: 0, Vote: MATCH
  C1 → B: QT'[32], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[32], B measures: 0, Vote: MATCH
  C3 → B: QT'[32], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[32], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 33 ---
  Candidate C[33] = 0
  A broadcasts QT[33] to all 5 C participants
  C0 → B: QT'[33], B measures: 0, Vote: MATCH
  C1 → B: QT'[33], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[33], B measures: 0, Vote: MATCH
  C3 → B: QT'[33], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[33], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 34 ---
  Candidate C[34] = 1
  A broadcasts QT[34] to all 5 C participants
  C0 → B: QT'[34], B measures: 0, Vote: MATCH
  C1 → B: QT'[34], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[34], B measures: 0, Vote: MATCH
  C3 → B: QT'[34], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[34], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

--- Pixel 35 ---
  Candidate C[35] = 0
  A broadcasts QT[35] to all 5 C participants
  C0 → B: QT'[35], B measures: 0, Vote: MATCH
  C1 → B: QT'[35], B measures: 1, Vote: MISMATCH
  C2 → B: QT'[35], B measures: 0, Vote: MATCH
  C3 → B: QT'[35], B measures: 1, Vote: MISMATCH
  C4 → B: QT'[35], B measures: 0, Vote: MATCH
  Majority Vote: 3/5 → ✓ MATCH

Matching complete with majority voting: 100.0% match
  Matched pixels: 36/36

Final Result: 100% match
Byzantine tolerance: 2/5 faulty nodes

Byzantine Tolerance Analysis:
- Total C participants: 5
- Tolerated Byzantine: ⌊(5-1)/2⌋ = 2
- Current Byzantine: 2
- System Status: ✓ Resilient

```
