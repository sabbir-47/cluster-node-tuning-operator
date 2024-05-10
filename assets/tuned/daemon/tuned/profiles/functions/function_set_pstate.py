import os
import tuned.logs
from . import base
from tuned.utils.commands import commands

log = tuned.logs.get()

processor_name = ("sandybridge",
        "ivybridge",
        "haswell",
        "broadwell",
        "skylake", 
        "kabylake",
        "cometlake",
        "canonlake")
		
pmu_path = "/sys/devices/cpu/caps/pmu_name"
class intel_recommended_pstate(base.Function):
	"""
	Checks the processor name and set the pstate
	"""
	def __init__(self):
		# arbitrary number of arguments
		super(intel_recommended_pstate, self).__init__("set_pstate_processor", 0)

	def execute(self, args):
		pstate="disable"
		if not super(intel_recommended_pstate, self).execute(args):
			return None
		
		current_processor_name = self._cmd.read_file(pmu_path)
		if current_processor_name == "" or current_processor_name in processor_name:
			return pstate
		pstate = "active"
		return pstate

	
