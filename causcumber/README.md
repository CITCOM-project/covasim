# Causcumber
Can we use cucumber specifications to systematically produce causal graphs that can be used to answer causal questions about a particular scenario in the Covasim model?

## Structure
The scenarios directory contains different example scenarios implemented in the Covasim model. For each scenario in the directory, a separate sub-directory should be created that contains the simulation and a cucumber specification.

## Steps to create a virtual environment:
1. In `./covasim/causcumber`, run `python3 -m venv causcumber`
2. To activate the virtual environment, run `source causcumber/bin/activate`
3. To install the necessary requirements, in the root directory (`./covasim`), run `pip install -r requirements.txt`
4. To install the necessary testing requirements, in the tests directory (`./covasim/tests`), run `pip install -r requirements_test.txt`

## Results Format
We work with CSV files produced by the simulations. These have 164 columns, the headings of which is as follows:
- `t` (time step)
- `date`
- Cumulative (`cum_`) and new (`new_`)
  - `infections`
  - `reinfections`
  - `infectious`
  - `symptomatic`
  - `severe`
  - `critical`
  - `recoveries`
  - `deaths`
  - `tests`
  - `diagnoses`
  - `known_deaths`
  - `quarantined`
  - `vaccinations`
  - `vaccinated`
- `n_susceptible`
- `n_exposed`
- `n_infectious`
- `n_symptomatic`
- `n_severe`
- `n_critical`
- `n_recovered`
- `n_dead`
- `n_diagnosed`
- `n_known_dead`
- `n_quarantined`
- `n_vaccinated`
- `n_alive`
- `n_naive`
- `n_preinfectious`
- `n_removed`
- `prevalence`
- `incidence`
- `r_eff`
- `doubling_time`
- `test_yield`
- `rel_test_yield`
- `frac_vaccinated`
- `pop_nabs`
- `pop_protection`
- `pop_symp_protection`

Each row in the CSV represents a single time step (day) in the model. The outputs are stored in `compare_interventions/results`, which is ignored by Git during the development process. We will make our results publicly available via ORDA when it is appropriate to do so.
