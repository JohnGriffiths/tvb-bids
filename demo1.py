

import sys
#sys.path.append('/github/github/tvb-library')
#sys.path.append('/github/github/tvb-data')
from tvb.simulator.lab import *

import numpy
from matplotlib.pyplot import figure,plot,title,show
from matplotlib import pyplot as plt


def run_demo(conn_file):

    oscillator = models.Generic2dOscillator()
    white_matter = connectivity.Connectivity(load_default=True)
    white_matter.speed = numpy.array([4.0])
    white_matter_coupling = coupling.Linear(a=0.0154)
    heunint = integrators.HeunDeterministic(dt=2**-6)

    mon_raw = monitors.Raw()
    mon_tavg = monitors.TemporalAverage(period=2**-2)

    what_to_watch = (mon_raw, mon_tavg)


    sim = simulator.Simulator(model = oscillator, connectivity = white_matter,
                              coupling = white_matter_coupling, 
                              integrator = heunint, monitors = what_to_watch)
    
    sim.configure()
     
    
    
    raw_data = []
    raw_time = []
    tavg_data = []
    tavg_time = []
    
    for raw, tavg in sim(simulation_length=2**10):
      if not raw is None:
         raw_time.append(raw[0])
         raw_data.append(raw[1])
    
      if not tavg is None:
         tavg_time.append(tavg[0])
         tavg_data.append(tavg[1])

    RAW = numpy.array(raw_data)
    TAVG = numpy.array(tavg_data)

    #Plot raw time series
    figure(1)
    plot(raw_time, RAW[:, 0, :, 0])
    title("Raw -- State variable 0")
    plt.savefig('figure1.png')
    plt.close()

    #Plot temporally averaged time series
    figure(2)
    plot(tavg_time, TAVG[:, 0, :, 0])
    title("Temporal average")
    plt.savefig('figure2.png')
    plt.close()
    #Show them
    #show()

    numpy.save('roi_data.npy', tavg_data)


if __name__ == '__main__':

    conn_file = sys.argv[1]

    run_demo(conn_file)


