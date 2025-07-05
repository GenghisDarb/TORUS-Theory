# Contributing to TORUS-Theory

## Purpose
This repository is structured to support scientific reproducibility and collaboration. Contributions should align with the project's phases, naming conventions, and branch strategy.

### Project Phases
- **Phase A**: Initial theory development.
- **Phase B**: Validation and refinement.
- **Phase C**: Experimental integration.
- **Phase D**: Broader applications and extensions.

### Naming Conventions
- **Files**: Use `snake_case`.
- **Folders**: Use `dashes`.

### Branch Strategy
- Use `feature/<topic>` for new features.
- Use `bugfix/<issue>` for bug fixes.

## Workflow
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request (PR) with a linked issue.
4. Run pre-commit hooks before pushing.

## Adding New Validation
- Place notebooks under `notebooks/validation/<domain>/`.
- Supply a 50-word README.
- If raw data exceeds 10 MB, provide a fetch-script.

## Coding Standards
- Use **Black** for code formatting.
- Use **Ruff** for linting.
- Write docstrings in NumPy style.
- Add tests in `tests/` using **pytest**.

## Pre-Commit Hooks
Ensure all pre-commit hooks pass before pushing changes. Run:
```bash
pre-commit run --all-files
```
