def run_simulation():
    from simulation.datacenter import DataCenter
    dc = DataCenter()
    dc.simulate_write("foo", "bar", R=2, W=2, N=3)
    dc.simulate_read("foo", R=2)
