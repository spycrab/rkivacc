import sys

import rkivacc

if __name__ == "__main__":
    report = None
    if len(sys.argv) == 2:
        report = rkivacc.RKIReport(sys.argv[1])
    else:
        report = rkivacc.RKIReport.obtain()

    if not report.has_per_capita():
        print("Calculating data")
        report.calculate_per_capita()

    print("Report from {}".format(report.modified()))
    print("Available states: {}".format(report.states()))
    print("Berlin: {}".format(report.state("Berlin")))
    
    for state in report.all_states():
            print(state)
        
    print("Total: {}".format(report.total())) # Same data as state() and all_states() but for all of Germany
