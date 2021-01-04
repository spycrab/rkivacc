import rkivacc

if __name__ == "__main__":
    report = rkivacc.RKIReport.obtain()
    
    print("Available states: {}".format(report.states()))
    print("Berlin: {}".format(report.state("Berlin")))
    
    for state in report.all_states():
            print(state)
        
    print("Total: {}".format(report.total())) # Same data as state() and all_states() but for all of Germany