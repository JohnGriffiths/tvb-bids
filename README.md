# tvb-bids  


[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/JohnGriffiths/tvb-bids/master)  


First pass at a minimal TVB BIDS App  

---  

The structure is as follows:  

- Dockerfile - specifies the docker image  
- Makefile   - has instructions on how to run (see also below)  
- demo1.py   - minimal tvb simulation demo  


## Usage  

*1. Build the docker image*  

docker build -t tvb-bids .  


*2. Run the app*  

This is the line in the makefile (specific to my machine)  

docker run -i --rm -v /c/Ubuntu_WSL/Code/libraries_of_mine/github/tvb-bids_data:/bids-dataset tvb-bids  


To run locally:  

docker run -i --rm -v M:/D tvb-bids  

where  

- M is the absolute system path to a folder containing the input data, and will also server as the top-level output destination. You should change this to match your system.   
- D is the path within the container that this system path will be mounted to. No need to change this.   



## More info  

### The TVB Part  

The tvb simulation part is in demo1.py (renamed to 'run.py' when the docker container is built)  

This implements an extremely minimal tvb simulation based closely on the [tutorial 1](https://github.com/the-virtual-brain/tvb-documentation/blob/master/tutorials/tutorial_s1_region_simulation.ipynb). See that file for documentation on wht exactly is going on here.   

The key thing from the point of view of BIDS is the standardization of the naming nomenclature for the inputs and outputs.   

These should follow the various BIDS derivatives specs identified in the [Neural Mass Models BIDS extension proposal](https://docs.google.com/document/d/1oaBWmkrUqH28oQb1PTO-rG_kuwNX9KqAoE9i5iDh1xw/edit?ts=5ca502fe). Specifically:   


*Inputs:*  

Connectivity matrix (mandatory)  
  data_folder/sub-01/connectivity/sub-01_desc-weight_conndata-network_connectivity.tsv  

Tract lengths matrix (mandatory)  
  data_folder/sub-01/connectivity/sub-01_desc-distance_conndata-network_connectivity.tsv  

json sidecar with additional info (mandatory)  
  data_folder/sub-01/connectivity/sub-01_conndata-network_connectivity.tsv  


*Outputs*  

Simulated regional time series (mandatory)  
data_folder/sub-01/neuralstates/  
	sub-01_desc-neuralstates.tsv  


The python script itself is called from the command line as follows:  

python demo1.py inputfolder outputfolder subnum  

e.g. (from this folder):  

python demo1.py bids_data bids_data 01  



*Run on binder*

1. Launch with the binder badge

2. Open terminal

3. cd /home/jovyan

4. python /opt/run.py bd bd 01




## To do  


Other potential inputs for different models:  

data_folder/sub-01/anat/  
sub-01_desc-parcstats_morph.tsv  
sub-01_hemi-L_space-fsnative_dseg.label.gii  
sub-01_hemi-L_space-fsnative_face.surf.gii  
sub-01_hemi-L_space-fsnative_innerskull.surf.gii  
sub-01_hemi-L_space-fsnative_outerskull.surf.gii  
sub-01_hemi-L_space-fsnative_normal.vector.gii  
sub-01_hemi-L_space-fsnative_pial.surf.gii  
sub-01_hemi-L_space-fsnative_scalp.surf.gii  
sub-01_hemi-R_space-fsnative_dseg.label.gii  
sub-01_hemi-R_space-fsnative_face.surf.gii  
sub-01_hemi-R_space-fsnative_innerskull.surf.gii  
sub-01_hemi-R_space-fsnative_normal.vector.gii  
sub-01_hemi-R_space-fsnative_outerskull.surf.gii  
sub-01_hemi-R_space-fsnative_pial.surf.gii  
sub-01_hemi-R_space-fsnative_scalp.surf.gii  

data_folder/sub-01/eeg/  
	sub-01_desc-eeg_proj.tsv  
	sub-01_task-simulation_electrodes.tsv  

data_folder/sub-01/func/
	sub-01_task-rest_atlas-aparcaseg_timeseries.tsv

data_folder/sub-01/meg/
	sub-01_desc-meg_proj.tsv
	sub-01_task-simulation_space-anat_sensors.tsv



