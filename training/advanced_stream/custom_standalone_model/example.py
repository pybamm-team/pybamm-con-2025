from model import ThermalDFN
import pybamm
from parameter_values import get_parameter_values

model = ThermalDFN()
# parameter_values = pybamm.ParameterValues("Chen2020")
# parameter_values.update({"R_c": 2, "C_c": 60}, check_already_exists=False)
parameter_values = pybamm.ParameterValues(get_parameter_values())
sim = pybamm.Simulation(model, parameter_values=parameter_values)
sim.solve([0, 3600])
sim.plot(["Temperature [°C]"])
