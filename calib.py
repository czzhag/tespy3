'''
calib file using for analysis of data taken through MCE. changed from matlab version calib.m
09/19/2023
'''
import numpy as np

class calib_ba:
    """BA calibration parameters. Same for all BA receivers. SI units. R - Ohms, V - Volts"""
    def __init__(self):
        self.R_SH = 0.0030 
        self.muxver = 'Mux11'
        self.M_FB = 24.99    #Mux07-15, Mux09-8, Mux11-25
        self.R_WIRE = 46.00
        self.R_BIAS = 400.00
        self.V_B_MAX = 5.00
        self.R_FB = 2000.00
        self.V_FB_MAX = 1.00
        self.BITS_BIAS = 15
        self.BITS_FB = 14
        
    def BIAS_CAL(self,clib):
        return (clib.V_B_MAX/(2**clib.BITS_BIAS))/(clib.R_BIAS + clib.R_WIRE)

    def FB_CAL(self,clib):
        return (clib.V_FB_MAX/(2**clib.BITS_FB))/(clib.R_FB+clib.R_WIRE)/clib.M_FB
