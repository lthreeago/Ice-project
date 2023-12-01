#!/usr/bin/python
import sys
import numpy as np
from scipy import integrate
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import locale
from matplotlib.ticker import StrMethodFormatter
from matplotlib.ticker import FormatStrFormatter
from matplotlib.font_manager import FontProperties
import os
from ctypes import *

def show_help():
    print ('''
ipi2obs is a code to calculate the average of some observables from i-Pi simulations and provides a Matplotlib graph

Usage: ipi2obs [OPTIONS]

INSTALATION:
    For install this code, type: 'ipi2obs.py -i'

OPTIONS:
    
    -f or --file (input file)
        sets the input file to calculate the observables. Without this option, the code not run

    -d or --density
        calculate the average density of your system

    -e or --energy
        calculate the average energy of your system

    -v or --volume
        calculate the average volume of your system

    -a or --alldata
        calculate the average in all data. If this option is not used, the average is calculated after 100 ps

    -p or --plot (output file .png)
        sets the output file to save the final graph

    -l or --label (label name) (default: Data)
        sets the label name of data.

    -h or --help
        displays this help menu

AUTHOR
   Lucas Thiago Siqueira de Miranda
''')

def param_select():
    par={}
    for i,v in enumerate(sys.argv):
        if v[0] == '-':
            try:
                next_arg=sys.argv[i+1]
            except:
                next_arg=sys.argv[i]
            if v in ('-f','--file'):
                par['input_file'] = next_arg
            
            elif v in ('-e','--energy'):
                par['observable'] = 5
            
            elif v in ('-v','--volume'):
                par['observable'] = 9

            elif v in ('-d','--density'):
                par['observable'] = 8

            elif v in ('-a', '--alldata'):
                par['alldata'] = True

            elif v in ('-p' or '--plot'):
                par['output_file'] = next_arg

            elif v in ('-l' or '--label'):
                par['label'] = next_arg

            elif v in ('-xc' or '--functional'):
                par['xc'] = next_arg

            elif v in ('-h','--help'):
                show_help()
                exit()

    return par

# Instalation
if ('-i' in sys.argv or '--install' in sys.argv ) and '.py' in sys.argv[0]:
    print('Installing...')
    exe=sys.argv[0].replace('.py','')
    os.system('which python > .tmp')
    program='#!'+open('.tmp','r').read()
    program+=open(sys.argv[0],'r').read()[1:]
    open(exe,'w').write(program)
    os.system('rm .tmp')
    os.system('chmod +x '+exe)
    print('Done!')
    exit()


def read_data(par):

    if "alldata" in par:
        data = np.loadtxt(par['input_file'], skiprows=10)
        return data[:,1], data[:,par['observable']]
    
    else:
        data = np.loadtxt(par['input_file'], skiprows=2010)
        return data[:,1]-100, data[:,par['observable']]


def plot(par):
    
    time, obs = read_data(par)
    cm=1/2.54

    plt.rcParams.update({'text.usetex': True})
    plt.rcParams['text.latex.preamble'] = [
       r'\usepackage{helvet}',    # set the normal font here
       r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
       r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
]

    
    fig, ax = plt.subplots(figsize=(8*cm, 8*cm))

    oavg = np.average(obs)
    ostd = np.std(obs)

    if par['observable'] == 5:
        text = str(locale.format('%.3f', oavg)) + r' $\rm{eV}$ $\pm$ ' + str(locale.format('%.3f', ostd))
        plt.ylabel(r'Energy [$\rm{eV}$]', fontsize=11)

    if par['observable'] == 8:
        text = str(locale.format('%.3f', oavg)) + r' $\rm{g/cm^3}$'
        plt.ylabel(r'Density [$\rm{g/cm^3}$]', fontsize=11)

    if par['observable'] == 9:
        text = str(locale.format('%.3f', oavg)) + r' $\rm{\AA^3}$ $\pm$ ' + str(locale.format('%.3f', ostd))
        plt.ylabel(r'Volume [$\rm{\AA^3}$]', fontsize=11)
    
    if 'label' in par:
        text1 = par['label']

    else:
        text1 = 'Data'

    #cor = {
    #        "PBE": "black",
    #        "optB88": "#2d75c2",
    #        "vdW-cx": "#eb42a1",
    #        "SCAN": "#edda32"
    #        }
    
    cor = {
            "PBE": "black",
            "optB88": "#0c31ee",
            "vdW-cx": "#f9705e",
            "SCAN": "#fcba03"
            }

    med = []
    for i in range(len(obs)):
        med.append(oavg)

    ax.plot(time, obs, '-', color=cor[par['xc']], alpha=0.8, label=text1, linewidth=1.8)
    ax.plot(time, med, '--', color='red', alpha=0.9, label=text, linewidth=2.5)

    ax.legend(loc=1, fontsize=9)
    ax.tick_params(length=6, width=1, direction='in')

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(9)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(9)

    ax.set_xlabel(r'Time [$\rm{ps}$]', fontsize=11)
    
    if 'alldata' in par:
        ax.set_xticks([0, 100, 200, 300, 400, 500, 600])
        ax.set_xticklabels([0, 100, 200, 300, 400, 500, 600])
        ax.set_xlim(0, 600)

    else:
        ax.set_xticks([0, 100, 200, 300, 400, 500])
        ax.set_xticklabels([0, 100, 200, 300, 400, 500])
        ax.set_xlim(0, 500)

    ax.set_title(par['xc'], x=0.02, y=0.14, pad=-14, fontsize=10, loc='left', color=cor[par['xc']])


# to be executed when called as a script
if __name__ == "__main__":
    
    # parse filename argument
    par=param_select()
    
    if not "input_file" in par:
        print("Missing the input file")
        show_help()
        exit()
   
    if not 'observable' in par:
        print("Missing the observable to plot")
        show_help()
        exit()

    plot(par)

    plt.tight_layout()
    plt.draw()

    if "output_file" in par:
        plt.savefig(par['output_file'])
    else:
        plt.show()


    sys.exit()
