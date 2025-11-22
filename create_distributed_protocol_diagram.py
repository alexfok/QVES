"""
Create a visual diagram of the DISTRIBUTED RBE-VES protocol flow
where QTs are distributed among C participants (max 1/3 each)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(18, 11))
ax.set_xlim(0, 18)
ax.set_ylim(0, 11)
ax.axis('off')

# Define colors
color_a = '#E8F4F8'  # Light blue
color_b = '#FFF4E6'  # Light orange
color_c = '#F0F8E8'  # Light green
arrow_color = '#2C5F8D'
text_color = '#1A1A1A'

# Title
ax.text(9, 10.5, 'Distributed RBE-VES Protocol: Enhanced Security Architecture', 
        fontsize=20, fontweight='bold', ha='center', color=text_color)
ax.text(9, 10.1, 'Each C participant receives ≤ 1/3 of quantum states', 
        fontsize=12, ha='center', style='italic', color='#666666')

# ============================================================================
# LEFT: Secret Image Input
# ============================================================================
secret_box = FancyBboxPatch((0.5, 7.5), 1.5, 1.5, boxstyle="round,pad=0.1", 
                            edgecolor='black', facecolor='#E0E0E0', linewidth=2)
ax.add_patch(secret_box)
ax.text(1.25, 8.25, 'Secret\nImage\nT[i]', fontsize=10, ha='center', 
        va='center', fontweight='bold')

# ============================================================================
# PARTICIPANT A - Encryption & Distribution
# ============================================================================
a_box = FancyBboxPatch((3, 7), 2.8, 2.5, boxstyle="round,pad=0.15", 
                       edgecolor='#2C5F8D', facecolor=color_a, linewidth=3)
ax.add_patch(a_box)
ax.text(4.4, 9.1, 'Participant A', fontsize=13, ha='center', 
        fontweight='bold', color=text_color)
ax.text(4.4, 8.7, 'RBE Encryption', fontsize=10, ha='center', style='italic')
ax.text(4.4, 8.2, 'QT[i] = K(θ,φ)|T[i]⟩', fontsize=9, ha='center', 
        family='monospace', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.text(4.4, 7.7, '• Generates random keys', fontsize=8, ha='center')
ax.text(4.4, 7.4, '• Distributes QTs to Cs', fontsize=8, ha='center', 
        color='#DC2626', fontweight='bold')

# Arrow from Secret to A
arrow1 = FancyArrowPatch((2, 8.25), (3, 8.25), 
                        arrowstyle='->', mutation_scale=30, 
                        linewidth=2.5, color=arrow_color)
ax.add_patch(arrow1)

# ============================================================================
# PARTICIPANT B - Key Holder
# ============================================================================
b_box = FancyBboxPatch((14.5, 7), 2.8, 2.5, boxstyle="round,pad=0.15", 
                       edgecolor='#D97706', facecolor=color_b, linewidth=3)
ax.add_patch(b_box)
ax.text(15.9, 9.1, 'Participant B', fontsize=13, ha='center', 
        fontweight='bold', color=text_color)
ax.text(15.9, 8.7, 'Key Holder', fontsize=10, ha='center', style='italic')
ax.text(15.9, 8.2, 'Receives: (θ, φ) keys', fontsize=9, ha='center',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.text(15.9, 7.7, '• Waits for QT\'[i]', fontsize=8, ha='center')
ax.text(15.9, 7.4, '• Applies RBE.Dec', fontsize=8, ha='center')

# Arrow from A to B (Keys only)
arrow2 = FancyArrowPatch((5.8, 8.9), (14.5, 8.9), 
                        arrowstyle='->', mutation_scale=30, 
                        linewidth=2.5, color='#D97706', linestyle='--')
ax.add_patch(arrow2)
ax.text(10.15, 9.3, 'Keys (θ, φ) ONLY', fontsize=10, ha='center', 
        bbox=dict(boxstyle='round', facecolor='#FFF4E6', edgecolor='#D97706', linewidth=2),
        fontweight='bold')

# ============================================================================
# MULTIPLE C PARTICIPANTS - Distributed Processing
# ============================================================================
c_spacing = 2.3
c_start_x = 7.5
c_y_positions = [5.5, 3.8, 2.1]
c_colors = ['#E8F8F0', '#F0F8E8', '#E8F8E8']

for i, (y_pos, c_color) in enumerate(zip(c_y_positions, c_colors)):
    c_box = FancyBboxPatch((c_start_x, y_pos), 2, 1.4, boxstyle="round,pad=0.1", 
                          edgecolor='#16A34A', facecolor=c_color, linewidth=2.5)
    ax.add_patch(c_box)
    ax.text(c_start_x + 1, y_pos + 1.15, f'C Participant {i}', fontsize=10, 
            ha='center', fontweight='bold', color=text_color)
    
    # Show qubit assignments
    if i == 0:
        qubits = 'QT[0,1,5]'
        ax.text(c_start_x + 1, y_pos + 0.8, f'{qubits}', fontsize=8, ha='center',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.9),
                family='monospace', fontweight='bold')
    elif i == 1:
        qubits = 'QT[2,4,7]'
        ax.text(c_start_x + 1, y_pos + 0.8, f'{qubits}', fontsize=8, ha='center',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.9),
                family='monospace', fontweight='bold')
    else:
        qubits = 'QT[3,6,8]'
        ax.text(c_start_x + 1, y_pos + 0.8, f'{qubits}', fontsize=8, ha='center',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.9),
                family='monospace', fontweight='bold')
    
    ax.text(c_start_x + 1, y_pos + 0.45, '≤ 33% of qubits', fontsize=7, ha='center',
            style='italic', color='#DC2626')
    ax.text(c_start_x + 1, y_pos + 0.15, 'Apply CNOT if C[i]=1', fontsize=7, ha='center')

# Add "..." to indicate more participants possible
ax.text(c_start_x + 1, 1.2, '... more C participants ...', fontsize=8, 
        ha='center', style='italic', color='#666666')

# Distribution arrows from A to Cs
for i, y_pos in enumerate(c_y_positions):
    arrow = FancyArrowPatch((5.8, 7.8 - i*0.3), (c_start_x, y_pos + 0.7), 
                           arrowstyle='->', mutation_scale=25, 
                           linewidth=2, color='#16A34A', alpha=0.7)
    ax.add_patch(arrow)

# Add distribution label
ax.text(6.5, 6.5, 'Distributed\nQT[i]', fontsize=9, ha='center', 
        bbox=dict(boxstyle='round', facecolor=color_c, edgecolor='#16A34A', linewidth=2),
        fontweight='bold')

# Candidate Image input
candidate_box = FancyBboxPatch((7.5, 0.2), 2, 0.8, boxstyle="round,pad=0.08", 
                               edgecolor='black', facecolor='#E0E0E0', linewidth=2)
ax.add_patch(candidate_box)
ax.text(8.5, 0.6, 'Candidate C[i]', fontsize=9, ha='center', fontweight='bold')

# Arrow from Candidate to Cs
arrow_cand = FancyArrowPatch((8.5, 1.0), (8.5, 2.1), 
                            arrowstyle='->', mutation_scale=25, 
                            linewidth=2, color=arrow_color)
ax.add_patch(arrow_cand)

# ============================================================================
# Arrows from Cs to B (Transformed States)
# ============================================================================
for i, y_pos in enumerate(c_y_positions):
    arrow = FancyArrowPatch((c_start_x + 2, y_pos + 0.7), (14.5, 8), 
                           arrowstyle='->', mutation_scale=25, 
                           linewidth=2, color='#7C3AED', alpha=0.6)
    ax.add_patch(arrow)

ax.text(12, 6, 'QT\'[i]', fontsize=10, ha='center', 
        bbox=dict(boxstyle='round', facecolor='#EDE9FE', edgecolor='#7C3AED', linewidth=2),
        fontweight='bold')
ax.text(12, 5.5, 'Transformed', fontsize=8, ha='center')

# ============================================================================
# Security Enhancement Box
# ============================================================================
sec_box = FancyBboxPatch((0.3, 3.5), 2.9, 3.2, boxstyle="round,pad=0.15", 
                         edgecolor='#DC2626', facecolor='#FEE2E2', linewidth=2.5)
ax.add_patch(sec_box)
ax.text(1.75, 6.4, '🔒 Security Enhancement', fontsize=11, ha='center', 
        fontweight='bold', color='#DC2626')

security_features = [
    '✓ Each C gets ≤ 1/3 qubits',
    '✓ Compromised C learns',
    '  only partial info',
    '✓ Each qubit processed',
    '  by 3 different Cs',
    '✓ Majority voting per',
    '  qubit group',
    '✓ Byzantine resilient',
    '✓ No-cloning protection'
]

for i, feature in enumerate(security_features):
    ax.text(1.75, 6.0 - i*0.28, feature, fontsize=7.5, ha='center',
            color=text_color)

# ============================================================================
# Key Properties Box
# ============================================================================
props_box = FancyBboxPatch((11, 3.5), 3.5, 3.2, boxstyle="round,pad=0.15", 
                          edgecolor='#2C5F8D', facecolor='#EBF5FF', linewidth=2)
ax.add_patch(props_box)
ax.text(12.75, 6.4, 'Protocol Properties', fontsize=11, ha='center', 
        fontweight='bold', color='#2C5F8D')

properties = [
    'Information-theoretic security',
    'Distributed quantum states',
    'Limited exposure per C',
    'Homomorphic CNOT evaluation',
    'Byzantine fault tolerance',
    'Scalable to N participants',
    'Quantum advantage'
]

for i, prop in enumerate(properties):
    ax.text(12.75, 6.0 - i*0.35, f'• {prop}', fontsize=8, ha='center',
            color=text_color)

# ============================================================================
# Distribution Statistics
# ============================================================================
stats_y = 0.2
ax.text(12.75, stats_y + 2.5, 'Distribution Example (9 qubits, 5 Cs):', 
        fontsize=9, ha='center', fontweight='bold', color='#666666')

stats = [
    'QT[0,3,5] → C₀, C₁, C₂  (3 Cs)',
    'QT[1,4,6] → C₁, C₂, C₃  (3 Cs)',
    'QT[2,7,8] → C₃, C₄, C₀  (3 Cs)',
]

for i, stat in enumerate(stats):
    ax.text(12.75, stats_y + 2.0 - i*0.3, stat, fontsize=7, ha='center',
            family='monospace', color='#444444')

ax.text(12.75, stats_y + 0.8, 'Each C: max 6 qubits (66.7%)', 
        fontsize=7, ha='center', style='italic', color='#DC2626', fontweight='bold')
ax.text(12.75, stats_y + 0.5, 'Target: ≤ 1/3 (33%) for large images', 
        fontsize=7, ha='center', style='italic', color='#666666')

# ============================================================================
# Flow Steps
# ============================================================================
steps = [
    (1.25, 9.3, '1'),
    (4.4, 9.7, '2'),
    (10.15, 9.6, '3'),
    (8.5, 1.2, '4'),
    (8.5, 4, '5'),
    (12, 6.4, '6'),
    (15.9, 9.7, '7')
]

for x, y, num in steps:
    circle = Circle((x, y), 0.28, color='#DC2626', zorder=10)
    ax.add_patch(circle)
    ax.text(x, y, num, fontsize=11, ha='center', va='center', 
            color='white', fontweight='bold', zorder=11)

# Add step descriptions at bottom
ax.text(9, -0.4, 
        '1→Secret  2→A:Encrypt  3→A distributes keys to B  4→Cs observe candidate  5→Cs apply CNOT  6→Cs send QT\' to B  7→B decrypts & votes',
        fontsize=8, ha='center', style='italic', color='#666666')

# ============================================================================
# Comparison with standard approach
# ============================================================================
ax.text(4, 0.7, 'vs Standard: All Cs get ALL qubits', fontsize=8, ha='center',
        bbox=dict(boxstyle='round', facecolor='#FEE2E2', alpha=0.8),
        style='italic', color='#666666')

# Save the figure
plt.tight_layout()
plt.savefig('rbe_ves_distributed_protocol.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✓ Distributed protocol diagram saved as 'rbe_ves_distributed_protocol.png'")
plt.close()

print("\nDiagram Details:")
print("- Resolution: 300 DPI (high quality)")
print("- Format: PNG")
print("- Architecture: DISTRIBUTED quantum states")
print("- Security: Each C participant gets ≤ 1/3 of qubits")
print("- Shows: Enhanced security through distribution")

