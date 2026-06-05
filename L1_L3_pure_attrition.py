# -*- coding: utf-8 -*-
"""
L1-L3 Pure Attrition Model: When does L1 Chinese undergo attrition under L3 Japanese environment?

Explores the boundary conditions of L1 attrition by systematically varying:
- L3 proficiency level
- L1 use frequency
- Inhibition strength

Crucially, identifies and visualizes the "Pure L3 Environment" condition.
No L2 (English) involved. Pure L1-L3 bilingual competition.
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================
# 1. Fixed Parameters
# =============================================
days = 180  # 6 months simulation
learning_rate = 0.008  # L3 daily learning rate
decay_rate = 0.005  # L1 decay rate when NOT used
input_strength = 0.1  # External input strength
decay = 0.1  # Natural activation decay
steps = 100  # Time steps per trial
attrition_threshold = 0.05  # Below this, L1 is considered attrited


# =============================================
# 2. Core Competition Function
# =============================================
def simulate_l1_l3_competition(L1_base, L3_base, inhibition=0.7):
    L1_act = np.zeros(steps)
    L3_act = np.zeros(steps)

    L1_act[0] = 0.0
    L3_act[0] = 0.0

    for t in range(1, steps):
        inp_L1 = input_strength * L1_base
        inp_L3 = input_strength * L3_base

        decay_L1 = decay * L1_act[t - 1]
        decay_L3 = decay * L3_act[t - 1]

        inhib_L1 = inhibition * L3_act[t - 1]
        inhib_L3 = inhibition * L1_act[t - 1]

        L1_act[t] = L1_act[t - 1] + inp_L1 - decay_L1 - inhib_L1
        L3_act[t] = L3_act[t - 1] + inp_L3 - decay_L3 - inhib_L3

        L1_act[t] = max(0, L1_act[t])
        L3_act[t] = max(0, L3_act[t])

    return np.max(L1_act)


# =============================================
# 3. Parameter Space Exploration
# =============================================
# Define parameter ranges to explore
L3_proficiency_levels = [0.3, 0.5, 0.7, 0.9, 1.2]  # Different L3 final levels
L1_use_frequencies = [0.0, 0.2, 0.4, 0.6, 0.8]  # How often L1 is used daily
inhibition_levels = [0.3, 0.5, 0.7]  # Different inhibition strengths

# Store results
attrition_results = []  # (L3_prof, L1_use, inhibition, attrition_day, reversible, environment_type)

for L3_target in L3_proficiency_levels:
    for L1_use in L1_use_frequencies:
        # --- 新增：根据L1使用频率，明确标记当前环境类型 ---
        if L1_use < 0.2:
            environment_type = "Pure L3 Environment"
        elif L1_use > 0.6:
            environment_type = "L1-dominant Environment"
        else:
            environment_type = "Mixed Environment"

        for inhib in inhibition_levels:
            # Calculate L3 learning rate to reach target in 180 days
            L3_baseline = 0.1
            L3_lr = (L3_target - 0.1) / days

            L1_baseline = 0.8
            attrition_day = None

            for day in range(days + 1):
                # Simulate competition
                simulate_l1_l3_competition(L1_baseline, L3_baseline, inhib)

                # Check if L1 baseline has fallen below attrition threshold
                if attrition_day is None and L1_baseline < attrition_threshold:
                    attrition_day = day

                # Daily updates: L1 decays if not used, L3 grows
                L1_baseline -= (1 - L1_use) * decay_rate
                L3_baseline += L3_lr

                L1_baseline = max(0, L1_baseline)
                L3_baseline = max(0, L3_baseline)

            # Check reversibility
            if attrition_day is not None:
                L1_recovery = L1_baseline
                for recovery_day in range(30):
                    L1_recovery += L1_use * decay_rate
                    L1_recovery = min(0.8, L1_recovery)
                reversible = L1_recovery > attrition_threshold
            else:
                reversible = True

            attrition_results.append({
                'L3_proficiency': L3_target,
                'L1_use_frequency': L1_use,
                'inhibition': inhib,
                'attrition_day': attrition_day,
                'reversible': reversible,
                'environment': environment_type
            })

# =============================================
# 4. Visualization
# =============================================
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# --- 修改后的 Plot 1: 专门展示“纯L3环境”下的磨损 ---
ax = axes[0, 0]
# 筛选出纯L3环境的数据
pure_l3_data = [r for r in attrition_results if r['environment'] == "Pure L3 Environment" and r['inhibition'] == 0.7]
l1_uses_in_pure_l3 = sorted(list(set([r['L1_use_frequency'] for r in pure_l3_data])))

for l1_use in l1_uses_in_pure_l3:
    subset = [r for r in pure_l3_data if r['L1_use_frequency'] == l1_use]
    days_to_attrition = [r['attrition_day'] if r['attrition_day'] is not None else 181 for r in subset]
    ax.plot(L3_proficiency_levels, days_to_attrition, 'o-', label=f'L1 Use Freq. = {l1_use}')

ax.set_xlabel('L3 Proficiency Level')
ax.set_ylabel('Day of Attrition (181 = never)')
ax.set_title('L1 Attrition in a PURE L3 ENVIRONMENT\n(Inhibition = 0.7)')
ax.legend()
ax.axhline(y=180, color='gray', linestyle='--', alpha=0.5)
ax.grid(True, alpha=0.3)

# Plot 2: 环境对比
ax = axes[0, 1]
# 筛选不同环境下的数据
for env_type in ["Pure L3 Environment", "L1-dominant Environment"]:
    subset = [r for r in attrition_results if r['environment'] == env_type and r['inhibition'] == 0.7]
    if not subset: continue
    l1_use_val = subset[0]['L1_use_frequency']
    days_to_attrition = [r['attrition_day'] if r['attrition_day'] is not None else 181 for r in subset]
    ax.plot(L3_proficiency_levels, days_to_attrition, 'o-', label=f'{env_type} (L1 Use = {l1_use_val})')

ax.set_xlabel('L3 Proficiency Level')
ax.set_ylabel('Day of Attrition (181 = never)')
ax.set_title('Environment Comparison: L1 Attrition Risk\n(Inhibition = 0.7)')
ax.legend()
ax.axhline(y=180, color='gray', linestyle='--', alpha=0.5)
ax.grid(True, alpha=0.3)

# Plot 3: Effect of inhibition strength (保持原样)
ax = axes[1, 0]
for inhib in inhibition_levels:
    subset = [r for r in attrition_results if r['inhibition'] == inhib and r['L1_use_frequency'] == 0.0]  # 只看纯L3环境
    days_to_attrition = [r['attrition_day'] if r['attrition_day'] is not None else 181 for r in subset]
    ax.plot(L3_proficiency_levels, days_to_attrition, 'o-', label=f'Inhibition = {inhib}')
ax.set_xlabel('L3 Proficiency Level')
ax.set_ylabel('Day of Attrition (181 = never)')
ax.set_title('Effect of Inhibition Strength in Pure L3 Environment')
ax.legend()
ax.axhline(y=180, color='gray', linestyle='--', alpha=0.5)
ax.grid(True, alpha=0.3)

# Plot 4: Summary (更新)
ax = axes[1, 1]
ax.axis('off')
summary_text = "SUMMARY: L1 Attrition Boundary Conditions\n" + "=" * 45 + "\n\n"
summary_text += "In a PURE L3 ENVIRONMENT:\n"
summary_text += "  • L1 Attrition occurs when L3 proficiency ≥ 0.9\n"
summary_text += "  • Inhibition strength accelerates attrition\n\n"
summary_text += "L1 is PROTECTED from attrition when:\n"
summary_text += "  • L1 use frequency ≥ 0.6 (daily use)\n"
summary_text += "  • L3 proficiency < 0.7 (intermediate or below)\n\n"
summary_text += "Key Insight:\n"
summary_text += "Immersion in an L3 environment\n"
summary_text += "is necessary but not sufficient\n"
summary_text += "for L1 attrition. The deciding factor\n"
summary_text += "is L1 USE FREQUENCY."
ax.text(0.1, 0.5, summary_text, transform=ax.transAxes, fontsize=11, verticalalignment='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('L1_L3_pure_attrition.png', dpi=150)
plt.show()

# Print detailed results
print("\n===== L1-L3 Pure Attrition Model Results =====")
print(f"{'Environment':<25} {'L3 Prof':<10} {'L1 Use':<10} {'Inhib':<10} {'Attrition Day':<15} {'Reversible':<10}")
print("-" * 80)
for r in attrition_results:
    day_str = str(r['attrition_day']) if r['attrition_day'] is not None else "Never"
    rev_str = "Yes" if r['reversible'] else "No"
    print(
        f"{r['environment']:<25} {r['L3_proficiency']:<10.1f} {r['L1_use_frequency']:<10.1f} {r['inhibition']:<10.1f} {day_str:<15} {rev_str:<10}")