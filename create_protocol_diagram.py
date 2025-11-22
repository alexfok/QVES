"""
Create a visual diagram of the RBE-VES protocol flow
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(16, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')

# Define colors
color_a = '#E8F4F8'  # Light blue
color_b = '#FFF4E6'  # Light orange
color_c = '#F0F8E8'  # Light green
arrow_color = '#2C5F8D'
text_color = '#1A1A1A'

# Title
ax.text(8, 9.5, 'RBE-Based Quantum Visual Encryption Scheme Protocol Flow', 
        fontsize=20, fontweight='bold', ha='center', color=text_color)

# ============================================================================
# LEFT: Secret Image Input
# ============================================================================
secret_box = FancyBboxPatch((0.5, 7), 1.5, 1.5, boxstyle="round,pad=0.1", 
                            edgecolor='black', facecolor='#E0E0E0', linewidth=2)
ax.add_patch(secret_box)
ax.text(1.25, 7.75, 'Secret\nImage\nT[i]', fontsize=10, ha='center', 
        va='center', fontweight='bold')

# ============================================================================
# PARTICIPANT A - Encryption
# ============================================================================
a_box = FancyBboxPatch((3, 6.5), 2.5, 2.5, boxstyle="round,pad=0.15", 
                       edgecolor='#2C5F8D', facecolor=color_a, linewidth=3)
ax.add_patch(a_box)
ax.text(4.25, 8.5, 'Participant A', fontsize=12, ha='center', 
        fontweight='bold', color=text_color)
ax.text(4.25, 8.1, 'RBE Encryption', fontsize=10, ha='center', style='italic')
ax.text(4.25, 7.6, 'QT[i] = K(θ,φ)|T[i]⟩', fontsize=9, ha='center', 
        family='monospace', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.text(4.25, 7.1, '• Generates random keys', fontsize=8, ha='center')
ax.text(4.25, 6.8, '• Encrypts each pixel', fontsize=8, ha='center')

# Arrow from Secret to A
arrow1 = FancyArrowPatch((2, 7.75), (3, 7.75), 
                        arrowstyle='->', mutation_scale=30, 
                        linewidth=2.5, color=arrow_color)
ax.add_patch(arrow1)

# ============================================================================
# PARTICIPANT B - Key Holder
# ============================================================================
b_box = FancyBboxPatch((11, 6.5), 2.5, 2.5, boxstyle="round,pad=0.15", 
                       edgecolor='#D97706', facecolor=color_b, linewidth=3)
ax.add_patch(b_box)
ax.text(12.25, 8.5, 'Participant B', fontsize=12, ha='center', 
        fontweight='bold', color=text_color)
ax.text(12.25, 8.1, 'Key Holder', fontsize=10, ha='center', style='italic')
ax.text(12.25, 7.6, 'Receives: (θ, φ) keys', fontsize=9, ha='center',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.text(12.25, 7.1, '• Waits for QT\'[i]', fontsize=8, ha='center')
ax.text(12.25, 6.8, '• Applies RBE.Dec', fontsize=8, ha='center')

# Arrow from A to B (Keys only)
arrow2 = FancyArrowPatch((5.5, 8.3), (11, 8.3), 
                        arrowstyle='->', mutation_scale=30, 
                        linewidth=2.5, color='#D97706', linestyle='--')
ax.add_patch(arrow2)
ax.text(8.25, 8.6, 'Keys (θ, φ) ONLY', fontsize=9, ha='center', 
        bbox=dict(boxstyle='round', facecolor='#FFF4E6', edgecolor='#D97706', linewidth=2),
        fontweight='bold')

# ============================================================================
# PARTICIPANT C - Quantum State Processor
# ============================================================================
c_box = FancyBboxPatch((6.75, 2), 2.5, 3.5, boxstyle="round,pad=0.15", 
                       edgecolor='#16A34A', facecolor=color_c, linewidth=3)
ax.add_patch(c_box)
ax.text(8, 5.1, 'Participant C', fontsize=12, ha='center', 
        fontweight='bold', color=text_color)
ax.text(8, 4.7, 'Quantum Processor', fontsize=10, ha='center', style='italic')
ax.text(8, 4.3, 'Receives: QT[i]', fontsize=9, ha='center',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.text(8, 3.8, '1. Observes C[i]', fontsize=8, ha='center')
ax.text(8, 3.5, '2. If C[i]=1:', fontsize=8, ha='center')
ax.text(8, 3.2, '   QT\'[i] = CNOT·QT[i]', fontsize=8, ha='center', 
        family='monospace')
ax.text(8, 2.9, '3. Else: QT\'[i] = QT[i]', fontsize=8, ha='center',
        family='monospace')
ax.text(8, 2.5, '4. Sends QT\'[i] to B', fontsize=8, ha='center')

# Arrow from A to C (Quantum States)
arrow3 = FancyArrowPatch((5.5, 6.8), (7, 5.5), 
                        arrowstyle='->', mutation_scale=30, 
                        linewidth=2.5, color='#16A34A')
ax.add_patch(arrow3)
ax.text(5.5, 6, 'QT[i]', fontsize=9, ha='center', 
        bbox=dict(boxstyle='round', facecolor=color_c, edgecolor='#16A34A', linewidth=2),
        fontweight='bold', rotation=-30)
ax.text(5.5, 5.6, 'Quantum', fontsize=8, ha='center', rotation=-30)
ax.text(5.5, 5.3, 'States', fontsize=8, ha='center', rotation=-30)

# Candidate Image input to C
candidate_box = FancyBboxPatch((6.75, 0.3), 2.5, 1.2, boxstyle="round,pad=0.1", 
                               edgecolor='black', facecolor='#E0E0E0', linewidth=2)
ax.add_patch(candidate_box)
ax.text(8, 0.9, 'Candidate Image C[i]', fontsize=10, ha='center', 
        fontweight='bold')

# Arrow from Candidate to C
arrow4 = FancyArrowPatch((8, 1.5), (8, 2), 
                        arrowstyle='->', mutation_scale=30, 
                        linewidth=2.5, color=arrow_color)
ax.add_patch(arrow4)

# ============================================================================
# Arrow from C to B (Transformed States)
# ============================================================================
arrow5 = FancyArrowPatch((9.25, 4), (11, 7), 
                        arrowstyle='->', mutation_scale=30, 
                        linewidth=3, color='#7C3AED')
ax.add_patch(arrow5)
ax.text(10.5, 5.8, 'QT\'[i]', fontsize=10, ha='center', 
        bbox=dict(boxstyle='round', facecolor='#EDE9FE', edgecolor='#7C3AED', linewidth=2),
        fontweight='bold', rotation=35)
ax.text(10.5, 5.3, 'Transformed', fontsize=8, ha='center', rotation=35)
ax.text(10.5, 5, 'States', fontsize=8, ha='center', rotation=35)

# ============================================================================
# FINAL OUTPUT - Decryption & Matching Result
# ============================================================================
result_box = FancyBboxPatch((14, 7), 1.5, 1.5, boxstyle="round,pad=0.1", 
                            edgecolor='black', facecolor='#DBEAFE', linewidth=2)
ax.add_patch(result_box)
ax.text(14.75, 7.9, 'B Decrypts', fontsize=9, ha='center', fontweight='bold')
ax.text(14.75, 7.5, 'Measures', fontsize=8, ha='center')
ax.text(14.75, 7.2, 'Match if', fontsize=8, ha='center')
ax.text(14.75, 6.9, 'result=|0⟩', fontsize=8, ha='center', family='monospace')

# Arrow from B to Result
arrow6 = FancyArrowPatch((13.5, 7.75), (14, 7.75), 
                        arrowstyle='->', mutation_scale=30, 
                        linewidth=2.5, color=arrow_color)
ax.add_patch(arrow6)

# ============================================================================
# Key Properties Box
# ============================================================================
props_y = 0.3
ax.text(12.25, props_y + 1.2, 'Key Properties:', fontsize=10, ha='center', 
        fontweight='bold', color=text_color)

properties = [
    '✓ Information-theoretic security',
    '✓ B has keys, C has quantum states',
    '✓ Homomorphic CNOT evaluation',
    '✓ No-cloning protection',
    '✓ Byzantine resilience (majority vote)'
]

for i, prop in enumerate(properties):
    ax.text(12.25, props_y + 0.9 - i*0.18, prop, fontsize=7, ha='center', 
            color=text_color)

# ============================================================================
# Flow indicators
# ============================================================================
# Add step numbers
steps = [
    (1.25, 8.8, '1'),
    (4.25, 9.2, '2'),
    (8.25, 9, '3'),
    (8, 1.7, '4'),
    (10, 5.5, '5'),
    (12.25, 9.2, '6'),
    (14.75, 8.5, '7')
]

for x, y, num in steps:
    circle = Circle((x, y), 0.25, color='#DC2626', zorder=10)
    ax.add_patch(circle)
    ax.text(x, y, num, fontsize=10, ha='center', va='center', 
            color='white', fontweight='bold', zorder=11)

# Add step descriptions at bottom
ax.text(8, -0.5, 
        '1→Secret  2→A:Encrypt  3→A sends keys to B  4→C observes candidate  5→C applies CNOT  6→C sends QT\' to B  7→B decrypts & measures',
        fontsize=8, ha='center', style='italic', color='#666666')

# Add legend for different types of data
legend_y = 5.5
ax.text(0.8, legend_y + 0.3, 'Data Flow:', fontsize=9, fontweight='bold')
ax.plot([0.5, 1.3], [legend_y, legend_y], '--', color='#D97706', linewidth=2)
ax.text(1.6, legend_y, 'Classical Keys', fontsize=8)
ax.plot([0.5, 1.3], [legend_y-0.3, legend_y-0.3], '-', color='#16A34A', linewidth=2)
ax.text(1.6, legend_y-0.3, 'Quantum States', fontsize=8)

# Save the figure
plt.tight_layout()
plt.savefig('rbe_ves_protocol_flow.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✓ Protocol diagram saved as 'rbe_ves_protocol_flow.png'")
plt.close()

print("\nDiagram Details:")
print("- Resolution: 300 DPI (high quality)")
print("- Format: PNG")
print("- Size: 16x10 inches")
print("- Flow: Left to Right")
print("- Shows: Complete RBE-VES protocol with all participants")

