# L1-L3 Pure Attrition Model

A computational model exploring the boundary conditions of L1 Chinese attrition in a pure L3 Japanese immersion environment. No L2 (English) involved. Pure L1-L3 bilingual competition.

## Research Question

In a pure L3 environment, under what conditions does L1 Chinese undergo attrition? What are the roles of L3 proficiency, L1 use frequency, and inhibition strength?

## Theoretical Framework

Based on:
- BIA+ model (Dijkstra & Van Heuven, 2002)
- Inhibitory Control model (Green, 1998)
- Activation Threshold hypothesis (De Bot, 2007)

## Model Design

- **Pure L3 Environment**: L1 use frequency is set to 0.0-0.2, simulating complete immersion in Japanese with minimal Chinese exposure.
- **L3 Proficiency**: systematically varied from 0.3 to 1.2.
- **L1 Use Frequency**: systematically varied from 0.0 to 0.8.
- **Inhibition Strength**: systematically varied from 0.3 to 0.7.
- The model tracks the day when L1 baseline activation falls below the attrition threshold (0.05).

## Key Findings

1. In a pure L3 environment, L1 attrition occurs when **L3 proficiency ≥ 0.9** (approximately JLPT N1 or above).
2. **L1 use frequency is the strongest protective factor**. Even in a pure L3 environment, if L1 use frequency ≥ 0.6 (daily use), L1 remains protected from attrition.
3. Inhibition strength accelerates attrition but is not the deciding factor.
4. Immersion in an L3 environment is **necessary but not sufficient** for L1 attrition.

## JLPT Level Correspondence

| L3 Baseline | JLPT Level | Vocabulary | Attrition Risk |
|-------------|------------|------------|----------------|
| < 0.3 | N5-N4 | 800-1,500 | Near zero |
| 0.3-0.5 | N3 | ~3,000 | Very low |
| 0.5-0.7 | N2 | ~6,000 | Low (L1 still protected) |
| 0.7-0.9 | N1 | 10,000+ | Moderate (requires low L1 use) |
| ≥ 0.9 | N1+ | 15,000+ | High (pure L3 + low L1 use) |

## Comparison with Model 6 (L1 Attrition Model)

| Dimension | Model 6 (L1 Attrition) | Model 7 (Pure L3 Attrition) |
|-----------|------------------------|-----------------------------|
| Core Question | Does L1 attrite in different environments? | When does L1 attrite in pure L3 environment? |
| Comparison | L1 environment vs. L2 environment | L3 proficiency, L1 use frequency, inhibition |
| L1 Environment | Performance interference, no attrition | L1 use ≥ 0.6 protects L1 |
| L2/L3 Environment | Competence attrition (activation → 0) | L3 ≥ N1 + low L1 use → attrition |
| Reversibility | Reversible in L1, irreversible in L2 | Reversible if L1 baseline > 0 |
| Protective Factor | Daily L1 use and top-down support | L1 use frequency is strongest |

## Integrated Conclusion

1. **L1 environment is the strongest protective shield** for L1.
2. **Pure L3 environment is necessary but not sufficient** for attrition.
3. **L3 must reach N1+ level** to pose a real threat to L1.
4. **L1 use frequency is the deciding factor** across all conditions.

## Implications for Teaching

Based on 14 years of Japanese teaching experience, this model provides mechanistic explanations for:
- **N5-N2 learners**: No risk of L1 attrition even when immersed in Japanese environment.
- **N1+ learners**: May experience "tip-of-the-tongue" or word order confusion if L1 use is minimal.
- **Language teachers**: No need to worry about foreign language learning "contaminating" the native language.

## File Structure

- `L1_L3_pure_attrition.py`: Python implementation of the model.
- `L1_L3_pure_attrition.png`: Visualization of attrition boundary conditions.

## Author

Wenjing DUAN

## License

This project is shared for academic portfolio purposes. If you use or adapt this code or ideas, please cite this repository.
