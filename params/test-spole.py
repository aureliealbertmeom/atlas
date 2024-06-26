#! /usr/bin/env python

"""
This is an example plots definition
=====================================
This is where the user defines what he/she wants to plot and where
A beginner user may look at the params.py file to see what can be done and where
An advanced user modifies params.py file to match their needs
Be careful not to put a . in the name of this file
Written in 2024-02-07 by Aurelie Albert aurelie.albert@univ-grenoble-alpes.fr
"""

# Machine where the plots are performed and hopefully the raw data are stored
# It can be only one above adastra, jean-zay, irene
machine='adastra'

# Name of the configuration
# It must be one of the configuration outputs stored on the above machine
configuration='eORCA36.L121'

# Simulation, experiment or run
# It must be one of the simulations for the above configuration stored on the above machine
#simulations=['EXP22a-10','EXP22b-10','EXP22c-10','EXP22d-10','EXP22e-10','EXP22f-10','EXP22g-10','EXP22h-10']
simulations=['EXP22a-10']

# Variables considered for plots
# It must be in the list of acceptable variables
#variables=['SSH','SSU','SSV','SSS','SST','MLD','MOD','VORT','SICONC','SITHIC']
variables=['SICONC']

# Type of plots 
# It must be either a map, a section or a time-serie
plot_type='map'

# Parameters of the plot
# This specifies the depth for maps, the coordinates for sections or time-series
plot_locs=['surf']

# Region of the plot
# This specifies the region for maps
#plot_regions=['global']
plot_regions=['spole']
#plot_regions=['global','natl','satl','windian','eindian','npac','spac','med']
#plot_regions=['natl','satl','windian','eindian','npac','spac','med']

# Frequency of the plots
# It must be compatible for the simulation and variable
frequency='1h'

# Period of the extraction
# Must be in the format yyyy-mm-dd
date_init='2012-01-01 11:00'
date_end='2012-01-01 11:00'

make_movies=True

plots_to_be_sent=['6694615800']
