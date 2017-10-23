from FireSpreadSimulator import FireSpreadEngine

def test_create_FireSpreadEngine():
    '''Checks whether a FireSpreadEngine object gets created correctly.'''
    sim_engine = FireSpreadEngine()
    sim_engine.print_current_grid()
    sim_engine.step_simulation()
    print("STEP ONCE")
    sim_engine.print_current_grid()

test_create_FireSpreadEngine()
