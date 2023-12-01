#!/usr/bin/python
import sys
import math as math
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

def plot(par, bond, angle):
    
    cm=1/2.54

    plt.rcParams.update({'text.usetex': True})
    plt.rcParams['text.latex.preamble'] = [
       r'\usepackage{helvet}',    # set the normal font here
       r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
       r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
]

    fig, ax = plt.subplots(2, 1, figsize=(8*cm, 12*cm))

    bavg = np.average(bond)
    aavg = np.average(angle)

    ax[0].hist(bond, align='mid', bins=500, alpha=0.6, color='#2390cf', label='Data')
    ax[1].hist(angle, align='mid', bins=500, alpha=0.6, color='#2390cf', label='Data')

    ax[0].vlines(bavg, 0, 25040, colors='red', alpha=0.6, linestyles='dashed', label='Average')
    ax[0].vlines(1.01, 0, 25040, colors='black', alpha=0.6, linestyles='dashed', label='Experimental')

    ax[1].vlines(aavg, 0, 11520, colors='red', alpha=0.6, linestyles='dashed', label='Average')
    ax[1].vlines(109.5, 0, 11520, colors='black', alpha=0.6, linestyles='dashed', label='Experimental')

    ax[0].legend(loc=2, fontsize=6)

    ax[0].set_ylabel(r'$\rm{P(d_{OO})}$', fontsize=10)
    ax[0].set_xlabel(r'$\rm{d_{OO}}$ $\rm{[\AA]}$', fontsize=10)
    ax[1].set_ylabel(r'$\rm{P(\theta_{HOH})}$', fontsize=10)
    ax[1].set_xlabel(r'$\rm{\theta}$ $\rm{[^\circ]}$', fontsize=10)

    ax[0].tick_params(length=6, width=0.5, direction='in')
    ax[1].tick_params(length=6, width=0.5, direction='in')

    ax[0].set_yticklabels([])
    ax[1].set_yticklabels([])
    ax[0].set_yticks([])
    ax[1].set_yticks([])

    ax[0].set_xticklabels([0.80, 0.90, 1.00, 1.10, 1.20])
    ax[1].set_xticklabels([80, 90, 100, 110, 120, 130])
    ax[0].set_xticks([0.80, 0.90, 1.00, 1.10, 1.20])
    ax[1].set_xticks([80, 90, 100, 110, 120, 130])

    ax[0].set_xlim(0.8, 1.2)
    ax[0].set_ylim(0, 25000)
    ax[1].set_xlim(80, 130)
    ax[1].set_ylim(0, 10000)


    for tick in ax[0].xaxis.get_major_ticks():
        tick.label.set_fontsize(10)

    for tick in ax[0].yaxis.get_major_ticks():
        tick.label.set_fontsize(10)

    for tick in ax[1].xaxis.get_major_ticks():
        tick.label.set_fontsize(10)

    for tick in ax[1].yaxis.get_major_ticks():
        tick.label.set_fontsize(10)

def measure(par):

    file = open(par['input_file'], 'r')
    anglefile = open('angle.dat', 'w')
    bondfile = open('bond.dat', 'w')

    bond = []
    angle = []

    a = file.readline()
    while a:
        a = file.readline()
        for i in range(int(par['n_mol'])):
            a = file.readline()
            b = a.split()
            x1 = float(b[5])
            y1 = float(b[6])
            z1 = float(b[7])
            a = file.readline()
            b = a.split()
            x2 = float(b[5])
            y2 = float(b[6])
            z2 = float(b[7])
            a = file.readline()
            b = a.split()
            x3 = float(b[5])
            y3 = float(b[6])
            z3 = float(b[7])
            
            xm = x1-x2
            ym = y1-y2
            zm = z1-z2

            xn = x1-x3
            yn = y1-y3
            zn = z1-z3

            d1 = math.sqrt(pow(xm,2) + pow(ym,2) + pow(zm,2))
            d2 = math.sqrt(pow(xn,2) + pow(yn,2) + pow(zn,2))

            bond.append(d1)
            bond.append(d2)

            bondfile.writelines(str(d1))
            bondfile.writelines('\n')
            bondfile.writelines(str(d2))
            bondfile.writelines('\n')

            cos = (xn*xm + yn*ym + zn*zm)/(d1*d2)

            rad = math.acos(cos)
            
            theta = 180*rad/math.pi

            angle.append(theta)

            anglefile.writelines(str(theta))
            anglefile.writelines('\n')



        a = file.readline()
        a = file.readline()

    return bond, angle


def average(bond, angle):

    bavg = np.average(bond)
    bstd = np.std(bond)

    aavg = np.average(angle)
    astd = np.std(angle)

    text = 'Average O-H bond lenght = '+ str(locale.format_string('%.3f', bavg)) + ' Ang +/- ' + str(locale.format_string('%.3f', bstd))
    name = r'Average H-O-H angle  = '+ str(locale.format_string('%.3f', aavg)) + r' degrees +/- ' + str(locale.format_string('%.3f', astd))

    print(text+'\n\n')
    print(name)




def show_help():
    print ('''
pdb2measure is a script to calculate and plot the theoretical O-H bond distance and H-O-H angle distributions for ice.

Usage: pdb2measure [OPTIONS]

INSTALATION:
    For install this code, type: 'python pdb2measure.py -i'

OPTIONS:
    
    -f or --file (pdb file)
        sets the pdb file to calculate the average O-H bond distance and H-O-H angle.

    -n or --n_mol (number of water molecules)
        defines the number of water molecules in system to calculate the averages.

    -sf or --save_file
        the angle.dat and bond.dat output files are saved if this option is marked.

    -p or --plot
        if this option is marked, a histogram is ploted for both measures

    -o or --output (.png file)
        sets the output file to save the graph.

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

            elif v in ('-n','--n_mol'):
                par['n_mol'] = next_arg

            elif v in ('-p','--plot'):
                par['plot'] = True

            elif v in ('-sf', '--save_file'):
                par['save_file'] = True

            elif v in ('-o', '--output'):
                par['output_file'] = next_arg

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


# to be executed when called as a script
if __name__ == "__main__":
    
    # parse filename argument
    par=param_select()
    
    if not 'input_file' in par:
        print("Missing the .pdb file")
        show_help()
        exit()

    if not 'n_mol' in par:
        print("Missing the number of water molecules")
        show_help()
        exit()
    
    bond, angle = measure(par)

    average(bond, angle)

    if 'plot' in par:
        plot(par, bond, angle)
        plt.tight_layout()
        plt.draw()

        if 'output_file' in par:
            plt.savefig(par['output_file'], dpi=500, bbox_inches='tight')

        else:
            plt.show()

    if 'save_file' in par:
        sys.exit()

    os.system('rm bond.dat angle.dat')
    sys.exit()
