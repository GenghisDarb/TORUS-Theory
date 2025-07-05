#!/usr/bin/env bash
set -euo pipefail

############################################
# 0. Ensure folder tree
############################################
mkdir -p docs/book/frontmatter docs/book/chapters docs/book/appendices \
         docs/papers docs/validation docs/experiments

############################################
# 1. Bulk moves ames
############################################
while read -r src dest; do
  [[ -e "$src" ]] && git mv -f "$src" "$dest" || echo "WARN: $src not found, skipped"
done <<'MAP'
# ----- front-matter -----
Preface.docx                                                   docs/book/frontmatter/00_Preface.docx
Table of Contents.docx                                         docs/book/frontmatter/Table_of_Contents.docx

# ----- chapters (01-15) -----
Chapter 1 - Introduction to TORUS.docx                         docs/book/chapters/01_Introduction_to_TORUS.docx
Chapter 2 - Principles of Structured Recursion.docx            docs/book/chapters/02_Principles_of_Structured_Recursion.docx
Chapter 3 - Dimensional Structure and Harmonic Closure.docx    docs/book/chapters/03_Dimensional_Structure_and_Harmonic_Closure.docx
Chapter 4 - Recursive Field Equations.docx                     docs/book/chapters/04_Recursive_Field_Equations.docx
Chapter 5 - Quantum Gravity from Recursion.docx                docs/book/chapters/05_Quantum_Gravity_from_Recursion.docx
Chapter 6 - Unification of Fundamental Forces.docx             docs/book/chapters/06_Unification_of_Fundamental_Forces.docx
Chapter 7 - Observer-State and Reality Anchoring.docx          docs/book/chapters/07_Observer-State_and_Reality_Anchoring.docx
Chapter 8 - Recursive Cosmology and Large-Scale Structure.docx docs/book/chapters/08_Recursive_Cosmology_and_Large-Scale_Structure.docx
Chapter 9 - Higher-Dimensional Recursion and Emergent Phenomena.docx docs/book/chapters/09_Higher-Dimensional_Recursion_and_Emergent_Phenomena.docx
Chapter 10 - Gravitational Wave Tests of TORUS.docx            docs/book/chapters/10_Gravitational_Wave_Tests_of_TORUS.docx
Chapter 11 - Quantum Experimental Tests of TORUS.docx          docs/book/chapters/11_Quantum_Experimental_Tests_of_TORUS.docx
Chapter 12 - Cosmological Observational Tests.docx             docs/book/chapters/12_Cosmological_Observational_Tests.docx
Chapter 13 - Technological and Societal Implications of TORUS.docx docs/book/chapters/13_Technological_and_Societal_Implications_of_TORUS.docx
Chapter 14 - Recursive Intelligence and Future Observer Frameworks.docx docs/book/chapters/14_Recursive_Intelligence_and_Future_Observer_Frameworks.docx
Chapter 15 - Future Directions and Open Questions.docx         docs/book/chapters/15_Future_Directions_and_Open_Questions.docx

# ----- appendices A-E -----
Appendix A - Mathematical Derivations and Proofs.docx          docs/book/appendices/A_Mathematical_Derivations_and_Proofs.docx
Appendix B - TORUS 14-Dimensional Hierarchy and Fundamental Constants.docx docs/book/appendices/B_14D_Hierarchy_and_Fundamental_Constants.docx
Appendix C - Glossary of Recursive Physics Terminology.docx    docs/book/appendices/C_Glossary_of_Recursive_Physics_Terminology.docx
Appendix D - Experimental Protocols and Recommended Tests.docx docs/book/appendices/D_Experimental_Protocols_and_Tests.docx
Controller Dimension Supplement to TORUS Theory Recursive Closure and Observer–State Synchronization.docx docs/book/appendices/E_Controller_Dimension_Supplement.docx

# ----- papers -----
Dimensional Constants Interrelation in TORUS Theory (0D–13D) – Formal Derivation and Closure.docx docs/papers/Dimensional_Constants_Interrelation_0D-13D.docx
Hyper-Recursive Algebra in TORUS Theory.docx                   docs/papers/Hyper-Recursive_Algebra_in_TORUS.docx
Topology of the Torus-of-Tori, chi-beta-Function, and the Projection-Angle Theorem.docx docs/papers/Topology_of_the_Torus-of-Tori_Chi_Beta_Function_and_Projection-Angle_Theorem.docx
Resolving the Black Hole Entropy and Information Paradox via TORUS Structured Recursion.docx docs/papers/Black_Hole_Entropy_and_Info_Paradox_TORUS.docx
Stationary-Action Ladder & Secondary Harmonics.docx            docs/papers/Stationary_Action_Ladder_and_Secondary_Harmonics.docx

# ----- validation -----
Universal Recursion - A 12 Sigma Cross-Domain Validation (Phase A).tex docs/validation/Universal_Recursion_Validation_PhaseA_12Sigma.tex
Universal Recursion - A 14 Sigma Cross-Domain Validation (Phase B).tex docs/validation/Universal_Recursion_Validation_PhaseB_14Sigma.tex
Gravitational-Wave-Detector Validation – Executive Summary (v1.0).docx docs/validation/GW_Detector_Validation_Exec_Summary_v1.0.docx

# ----- experiments -----
OSQN Drift in a Quartz-Oscillator Loop Lab Worksheet.docx      docs/experiments/OSQN_Drift_Quartz_Osc_Lab_Worksheet.docx
MAP

############################################
# 2. Commit & push
############################################
git add .
git commit -m "Fix: move misplaced files, slug-rename, restore TORUS folder structure"
git push origin main

############################################
# 3. Quick verification (optional)
############################################
echo "Chapters:   $(git ls-files docs/book/chapters | wc -l)  (expect 15)"
echo "Appendices: $(git ls-files docs/book/appendices | wc -l) (expect 5)"
