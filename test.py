import simulation
import logger
import person

def _test_simulation():
    pop_size = 10000
    vacc_percentage = .90
    virus_name = "Ebola"
    mortality_rate = .70
    basic_repro_num = .25
    initial_infected = 10
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)
    simulation.run()
