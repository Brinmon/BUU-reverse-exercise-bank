from angr import *
 
p = Project('re.exe',auto_load_libs = False)
state = p.factory.blank_state(addr=0x004164F8)
simfd = state.posix.get_fd(0)
data,real_size = simfd.read_data(22)
state.memory.store(0x0042612C,data)
state.memory.store(0x00426020,data)
sm = p.factory.simulation_manager(state)
sm.one_active.options.add(options.LAZY_SOLVES)
sm.explore(find = 0x00416609,avoid = 0x004165EA)
text = sm.one_found.solver.eval(sm.one_found.memory.load(0x0042612C,22),cast_to = bytes)
print (text)