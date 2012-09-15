#what
import statgrab
print("Machine Resource Agent deploying...")

#data are displayed in bytes I think
#RAM and CPU stats
print(statgrab.sg_get_cpu_stats())

#HD Space
print(statgrab.sg_get_mem_stats())

#still need to work on parsing

