# Causcumber
Can we use cucumber specifications to systematicaly produce causal graphs that can be used to answer causal questions about a particular scenario in the Covasim model?

## Structure
The scenarios directory contains different example scenarios implemented in the Covasim model. For each scenario in the directory, a separate sub-directory should be created that contains the simulation and a cucumber specification.

## Steps to create a virtual environment:
1. In `./covasim/causcumber`, run `python3 -m venv causcumber`
2. To activate the virtual environment, run `source causcumber/bin/activate`
3. To install the necessary requirements, in the root directory (`./covasim`), run `pip install -r requirements.txt`
4. To install the necessary testing requirements, in the tests directory (`./covasim/tests`), run `pip install -r requirements_test.txt`
