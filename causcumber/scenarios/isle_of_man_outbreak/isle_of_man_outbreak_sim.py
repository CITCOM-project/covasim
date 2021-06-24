import covasim as cv


def msim_to_csv(simulation: cv.MultiSim, output_file_name: str):
    """ Takes a MultiSim simulation, converts to a CSV file, and saves to ./results/ with the
        given file name. """
    simulation_df = simulation.base_sim.to_df()
    simulation_df.to_csv("./results/{}.csv".format(str.lower(output_file_name)), index=False)


""" Which intervention is more effective at reducing the cumulative number of infections? """
isle_of_man_outbreak_pars = dict(
    location="UK",  # No Isle of Man, UK is closest
    start_day="2021-02-01",
    end_day="2021-04-30",
    pop_type="hybrid",
    pop_size=84584
)

# Define interventions
testing_intervention = cv.test_prob(symp_prob=0.2, asymp_prob=0.001, symp_quar_prob=1.0, asymp_quar_prob=1.0)
contact_tracing_intervention = cv.contact_tracing(trace_probs=dict(h=1.0, s=0.5, w=0.5, c=0.3), start_day="2020-05-28")

# Create simulations
baseline_sim = cv.Sim(pars=isle_of_man_outbreak_pars, label="Baseline")
testing_sim = cv.Sim(pars=isle_of_man_outbreak_pars, interventions=testing_intervention, label="Testing")
contact_tracing_sim = cv.Sim(pars=isle_of_man_outbreak_pars, interventions=[testing_intervention, contact_tracing_intervention],
                             label="Contact Tracing")

# Create multi-simulations
baseline_sims = cv.MultiSim(baseline_sim)
testing_sims = cv.MultiSim(testing_sim)
contact_tracing_sims = cv.MultiSim(contact_tracing_sim)
intervention_sims = [baseline_sims, testing_sims, contact_tracing_sims]

# Combine multi-simulations into a single multi-simulation and run
interventions_msims = []
for intervention_sim in intervention_sims:
    intervention_sim.run(n_runs=10)
    intervention_sim.mean()
    interventions_msims.append(intervention_sim)
    msim_to_csv(intervention_sim, str.lower(intervention_sim.label))

# View plots
merged_intervention_msims = cv.MultiSim.merge(interventions_msims, base=True)
plt = merged_intervention_msims.plot(color_by_sim=True, to_plot=["new_infections", "cum_infections",
                                                            "new_deaths", "cum_deaths"])
plt.savefig("data/predicted_isle_of_man_pandemic.png", dpi=300, format="png")