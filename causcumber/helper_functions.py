import covasim as cv


def msim_to_csv(simulation: cv.MultiSim, output_file_name: str):
    """ Takes a MultiSim simulation, converts to a CSV file, and saves to ./results/ with the
        given file name. """
    simulation_df = simulation.base_sim.to_df()
    simulation_df.to_csv("./results/{}.csv".format(str.lower(output_file_name)), index=False)
