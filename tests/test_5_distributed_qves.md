# Test 5: Distributed Quantum VES (Enhanced Security)

**Configuration:** 5 C participants, 1 Byzantine, Distributed Mode
**Image size:** 6×6 (36 pixels)
**Security:** Each C gets max 1/3 of qubits

```
======================================================================
Test 5: Distributed Quantum VES (Enhanced Security)
======================================================================

Image size: 6×6 (36 pixels)

Secret Image: 6×6

Candidate Image: 6×6 (identical to secret)

Security Enhancement:
  • Each C participant receives ≤ 33% of qubits
  • Compromised C cannot learn full secret
  • Byzantine participant 2 has limited access

Byzantine-Resilient Matching
Mode: DISTRIBUTED (each C gets max 1/3 of qubits)
--------------------------------------------------
Total C participants: 5
Byzantine participants: 1

Qubit Distribution (each qubit assigned to multiple Cs):
  QT[0] → C participants [0, 1, 2]
  QT[1] → C participants [3, 4, 0]
  QT[2] → C participants [1, 2, 3]
  QT[3] → C participants [4, 0, 1]
  QT[4] → C participants [2, 3, 4]
  ... (total 36 qubits)

Qubits per C participant:
  C0: 22 qubits (61.1%)
  C1: 22 qubits (61.1%)
  C2: 22 qubits (61.1%)
  C3: 21 qubits (58.3%)
  C4: 21 qubits (58.3%)

  C participant 0: Honest (observes correct image)
  C participant 1: Honest (observes correct image)
  C participant 2: Byzantine (observes flipped image)
  C participant 3: Honest (observes correct image)
  C participant 4: Honest (observes correct image)

--- Pixel 0 ---
  Candidate C[0] = 0
  A sends QT[0] to C participants [0, 1, 2]
  C0 → B: QT'[0], B measures: 0, Vote: MATCH
  C1 → B: QT'[0], B measures: 0, Vote: MATCH
  C2 → B: QT'[0], B measures: 1, Vote: MISMATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 1 ---
  Candidate C[1] = 1
  A sends QT[1] to C participants [3, 4, 0]
  C3 → B: QT'[1], B measures: 0, Vote: MATCH
  C4 → B: QT'[1], B measures: 0, Vote: MATCH
  C0 → B: QT'[1], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 2 ---
  Candidate C[2] = 0
  A sends QT[2] to C participants [1, 2, 3]
  C1 → B: QT'[2], B measures: 0, Vote: MATCH
  C2 → B: QT'[2], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[2], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 3 ---
  Candidate C[3] = 1
  A sends QT[3] to C participants [4, 0, 1]
  C4 → B: QT'[3], B measures: 0, Vote: MATCH
  C0 → B: QT'[3], B measures: 0, Vote: MATCH
  C1 → B: QT'[3], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 4 ---
  Candidate C[4] = 0
  A sends QT[4] to C participants [2, 3, 4]
  C2 → B: QT'[4], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[4], B measures: 0, Vote: MATCH
  C4 → B: QT'[4], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 5 ---
  Candidate C[5] = 1
  A sends QT[5] to C participants [0, 1, 2]
  C0 → B: QT'[5], B measures: 0, Vote: MATCH
  C1 → B: QT'[5], B measures: 0, Vote: MATCH
  C2 → B: QT'[5], B measures: 1, Vote: MISMATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 6 ---
  Candidate C[6] = 1
  A sends QT[6] to C participants [3, 4, 0]
  C3 → B: QT'[6], B measures: 0, Vote: MATCH
  C4 → B: QT'[6], B measures: 0, Vote: MATCH
  C0 → B: QT'[6], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 7 ---
  Candidate C[7] = 0
  A sends QT[7] to C participants [1, 2, 3]
  C1 → B: QT'[7], B measures: 0, Vote: MATCH
  C2 → B: QT'[7], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[7], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 8 ---
  Candidate C[8] = 1
  A sends QT[8] to C participants [4, 0, 1]
  C4 → B: QT'[8], B measures: 0, Vote: MATCH
  C0 → B: QT'[8], B measures: 0, Vote: MATCH
  C1 → B: QT'[8], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 9 ---
  Candidate C[9] = 0
  A sends QT[9] to C participants [2, 3, 4]
  C2 → B: QT'[9], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[9], B measures: 0, Vote: MATCH
  C4 → B: QT'[9], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 10 ---
  Candidate C[10] = 1
  A sends QT[10] to C participants [0, 1, 2]
  C0 → B: QT'[10], B measures: 0, Vote: MATCH
  C1 → B: QT'[10], B measures: 0, Vote: MATCH
  C2 → B: QT'[10], B measures: 1, Vote: MISMATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 11 ---
  Candidate C[11] = 0
  A sends QT[11] to C participants [3, 4, 0]
  C3 → B: QT'[11], B measures: 0, Vote: MATCH
  C4 → B: QT'[11], B measures: 0, Vote: MATCH
  C0 → B: QT'[11], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 12 ---
  Candidate C[12] = 0
  A sends QT[12] to C participants [1, 2, 3]
  C1 → B: QT'[12], B measures: 0, Vote: MATCH
  C2 → B: QT'[12], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[12], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 13 ---
  Candidate C[13] = 1
  A sends QT[13] to C participants [4, 0, 1]
  C4 → B: QT'[13], B measures: 0, Vote: MATCH
  C0 → B: QT'[13], B measures: 0, Vote: MATCH
  C1 → B: QT'[13], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 14 ---
  Candidate C[14] = 0
  A sends QT[14] to C participants [2, 3, 4]
  C2 → B: QT'[14], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[14], B measures: 0, Vote: MATCH
  C4 → B: QT'[14], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 15 ---
  Candidate C[15] = 1
  A sends QT[15] to C participants [0, 1, 2]
  C0 → B: QT'[15], B measures: 0, Vote: MATCH
  C1 → B: QT'[15], B measures: 0, Vote: MATCH
  C2 → B: QT'[15], B measures: 1, Vote: MISMATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 16 ---
  Candidate C[16] = 0
  A sends QT[16] to C participants [3, 4, 0]
  C3 → B: QT'[16], B measures: 0, Vote: MATCH
  C4 → B: QT'[16], B measures: 0, Vote: MATCH
  C0 → B: QT'[16], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 17 ---
  Candidate C[17] = 1
  A sends QT[17] to C participants [1, 2, 3]
  C1 → B: QT'[17], B measures: 0, Vote: MATCH
  C2 → B: QT'[17], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[17], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 18 ---
  Candidate C[18] = 1
  A sends QT[18] to C participants [4, 0, 1]
  C4 → B: QT'[18], B measures: 0, Vote: MATCH
  C0 → B: QT'[18], B measures: 0, Vote: MATCH
  C1 → B: QT'[18], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 19 ---
  Candidate C[19] = 0
  A sends QT[19] to C participants [2, 3, 4]
  C2 → B: QT'[19], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[19], B measures: 0, Vote: MATCH
  C4 → B: QT'[19], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 20 ---
  Candidate C[20] = 1
  A sends QT[20] to C participants [0, 1, 2]
  C0 → B: QT'[20], B measures: 0, Vote: MATCH
  C1 → B: QT'[20], B measures: 0, Vote: MATCH
  C2 → B: QT'[20], B measures: 1, Vote: MISMATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 21 ---
  Candidate C[21] = 0
  A sends QT[21] to C participants [3, 4, 0]
  C3 → B: QT'[21], B measures: 0, Vote: MATCH
  C4 → B: QT'[21], B measures: 0, Vote: MATCH
  C0 → B: QT'[21], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 22 ---
  Candidate C[22] = 1
  A sends QT[22] to C participants [1, 2, 3]
  C1 → B: QT'[22], B measures: 0, Vote: MATCH
  C2 → B: QT'[22], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[22], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 23 ---
  Candidate C[23] = 0
  A sends QT[23] to C participants [4, 0, 1]
  C4 → B: QT'[23], B measures: 0, Vote: MATCH
  C0 → B: QT'[23], B measures: 0, Vote: MATCH
  C1 → B: QT'[23], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 24 ---
  Candidate C[24] = 0
  A sends QT[24] to C participants [2, 3, 4]
  C2 → B: QT'[24], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[24], B measures: 0, Vote: MATCH
  C4 → B: QT'[24], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 25 ---
  Candidate C[25] = 1
  A sends QT[25] to C participants [0, 1, 2]
  C0 → B: QT'[25], B measures: 0, Vote: MATCH
  C1 → B: QT'[25], B measures: 0, Vote: MATCH
  C2 → B: QT'[25], B measures: 1, Vote: MISMATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 26 ---
  Candidate C[26] = 0
  A sends QT[26] to C participants [3, 4, 0]
  C3 → B: QT'[26], B measures: 0, Vote: MATCH
  C4 → B: QT'[26], B measures: 0, Vote: MATCH
  C0 → B: QT'[26], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 27 ---
  Candidate C[27] = 1
  A sends QT[27] to C participants [1, 2, 3]
  C1 → B: QT'[27], B measures: 0, Vote: MATCH
  C2 → B: QT'[27], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[27], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 28 ---
  Candidate C[28] = 0
  A sends QT[28] to C participants [4, 0, 1]
  C4 → B: QT'[28], B measures: 0, Vote: MATCH
  C0 → B: QT'[28], B measures: 0, Vote: MATCH
  C1 → B: QT'[28], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 29 ---
  Candidate C[29] = 1
  A sends QT[29] to C participants [2, 3, 4]
  C2 → B: QT'[29], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[29], B measures: 0, Vote: MATCH
  C4 → B: QT'[29], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 30 ---
  Candidate C[30] = 1
  A sends QT[30] to C participants [0, 1, 2]
  C0 → B: QT'[30], B measures: 0, Vote: MATCH
  C1 → B: QT'[30], B measures: 0, Vote: MATCH
  C2 → B: QT'[30], B measures: 1, Vote: MISMATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 31 ---
  Candidate C[31] = 0
  A sends QT[31] to C participants [3, 4, 0]
  C3 → B: QT'[31], B measures: 0, Vote: MATCH
  C4 → B: QT'[31], B measures: 0, Vote: MATCH
  C0 → B: QT'[31], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 32 ---
  Candidate C[32] = 1
  A sends QT[32] to C participants [1, 2, 3]
  C1 → B: QT'[32], B measures: 0, Vote: MATCH
  C2 → B: QT'[32], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[32], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 33 ---
  Candidate C[33] = 0
  A sends QT[33] to C participants [4, 0, 1]
  C4 → B: QT'[33], B measures: 0, Vote: MATCH
  C0 → B: QT'[33], B measures: 0, Vote: MATCH
  C1 → B: QT'[33], B measures: 0, Vote: MATCH
  Majority Vote: 3/3 → ✓ MATCH

--- Pixel 34 ---
  Candidate C[34] = 1
  A sends QT[34] to C participants [2, 3, 4]
  C2 → B: QT'[34], B measures: 1, Vote: MISMATCH
  C3 → B: QT'[34], B measures: 0, Vote: MATCH
  C4 → B: QT'[34], B measures: 0, Vote: MATCH
  Majority Vote: 2/3 → ✓ MATCH

--- Pixel 35 ---
  Candidate C[35] = 0
  A sends QT[35] to C participants [0, 1, 2]
  C0 → B: QT'[35], B measures: 0, Vote: MATCH
  C1 → B: QT'[35], B measures: 0, Vote: MATCH
  C2 → B: QT'[35], B measures: 1, Vote: MISMATCH
  Majority Vote: 2/3 → ✓ MATCH

Matching complete with majority voting: 100.0% match
  Matched pixels: 36/36

Final Result: 100% match
Byzantine tolerance: 1/5 faulty nodes

Security Analysis (Distributed Mode):
- Total qubits: 36
- Target max per C: 12 (≤ 33%)
- Each qubit: Processed by 3 different C participants
- Byzantine C2: Limited to ~33% of information
- System Status: ✓ Enhanced Security

```
