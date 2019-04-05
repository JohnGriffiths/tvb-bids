

import sys
#sys.path.append('/github/github/tvb-library')
#sys.path.append('/github/github/tvb-data')
from tvb.simulator.lab import *

import numpy
from matplotlib.pyplot import figure,plot,title,show
from matplotlib import pyplot as plt


#!/usr/bin/env python3
"""
example of BIDS app for BIDS compmodels

"""

import argparse
import os
import subprocess
import nibabel
import numpy
from glob import glob
import pandas
import json
from bids import BIDSLayout, BIDSValidator

import numpy as np
import pandas as pd

__version__ = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                    'version')).read()

def run_demo(input_dir,output_dir,subnum):

    weights,lengths = read_inputs(input_dir,subnum)
    raw_data,tavg_data = run_tvb_sim(weights,lengths)
    write_outputs(output_dir,subnum,raw_data,tavg_data)


def read_inputs(input_dir,subnum):

    weights_file = '%s/sub-%s/connectivity/sub-%s_desc-weights_conndata-network_connectivity.tsv' %(input_dir,subnum,subnum)

    lengths_file = '%s/sub-%s/connectivity/sub-%s_desc-distance_conndata-network_connectivity.tsv' %(input_dir,subnum,subnum)

    weights = pd.read_csv(weights_file, sep='\t',header=None).values
    lengths = pd.read_csv(lengths_file, sep='\t',header=None).values

    return weights,lengths

def write_outputs(output_dir,subnum,raw_data,tavg_data):
       
    #raw_data,tavg_data = neuralstates
    raw_file = '%s/sub-%s/sub-%s_desc-neuralstates_raw.npy' %(output_dir,subnum,subnum)
    tavg_file = '%s/sub-%s/sub-%s_desc-neuralstates_tavg.npy' %(output_dir,subnum,subnum)
    #np.writetxt(neuralstates_file,neuralstates)
    #np.writetxt(neuralstates_file,neuralstates)
    #pd.DataFrame(np.squeeze(neuralstates)).to_csv(neuralstates_file, sep='\t')
    np.save(raw_file,raw_data)
    np.save(tavg_file,tavg_data)

def run_tvb_sim(weights,lengths):

    oscillator = models.Generic2dOscillator()
    white_matter = connectivity.Connectivity()#load_default=True)
    white_matter.weights = weights
    white_matter.tract_lengths = lengths
    white_matter.speed = numpy.array([4.0])
    white_matter_coupling = coupling.Linear(a=0.0154)
    white_matter.configure()

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
    #figure(1)
    #plot(raw_time, RAW[:, 0, :, 0])
    #title("Raw -- State variable 0")
    #plt.savefig('figure1.png')
    #plt.close()

    #Plot temporally averaged time series
    #figure(2)
    #plot(tavg_time, TAVG[:, 0, :, 0])
    #title("Temporal average")
    #plt.savefig('figure2.png')
    #plt.close()
    #Show them
    #show()

    return RAW,TAVG
    # numpy.save(output_dir + '/sub-01_desc-neuralstats.npy', tavg_data)



if __name__ == '__main__':

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    subnum = sys.argv[3]

    run_demo(input_dir,output_dir,subnum)
    #try:
    #    run_demo(input_dir,output_dir,subnum)
    #except: 
    #    #import pdb
    #    #pdb.set_trace()
    
    
