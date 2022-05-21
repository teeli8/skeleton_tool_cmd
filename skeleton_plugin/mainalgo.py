# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:11:46 2022

@author: Yigan
"""

#import napari
#from . import graph
#from . import drawing
#from . import display
from timer import TimeRecord
#from .pruning import ETPruningAlgo
from statemachine import StateMachine
import appstates as aps
import graphprinter as gp


class AlgoStatus:
    
    def __init__(self):
        self.run = False
        self.raw_data = []
        self.biimg = None
        self.boundary = None
        self.vor = None
        self.graph = None
        self.algo = None
        self.final = None
        self.finalEts = None
        self.joint = None
        

class AppStatus:
    
    def __init__(self):
        self.biThresh = 0
        self.etThresh = 0
        self.method = 0
        self.shape = None
        self.imgpath = ''
        self.outpath = ''
        

class SkeletonApp:
    
    __current = None
    etThresh = 10
    
    def __init__(self):
        self.algoStatus = AlgoStatus()
        self.appStatus = AppStatus()
        self.stm = StateMachine()
        self.timer = TimeRecord()
        pass
    
    def inst():
        if SkeletonApp.__current is None:
            SkeletonApp.__current = SkeletonApp()
        return SkeletonApp.__current
    
    def run(self):
        self.timer.clear()
        self.timer.stamp("Start")
        self.algoStatus.run = True
        if self.algoStatus.biimg == None:
            self.stm.change_state(aps.ReadState())
        else:
            self.stm.change_state(aps.BoundaryState())
        
        self.__runall()
        self.timer.print_records()
    
    def reset_bithresh(self, newT : float):
        self.appStatus.biThresh = newT
        if self.algoStatus.raw_data is None or len(self.algoStatus.raw_data)==0:
            self.stm.change_state(aps.ReadState())
        else:          
            self.stm.change_state(aps.ThreshState())    
        self.__runall()
    
    def reset_etthresh(self, newT : float):
        self.appStatus.etThresh = newT
        #self.stm.change_state(aps.ETPruneState())
        self.stm.change_state(aps.PruneChoosingState())
        self.__runall()
    
    def reset_method(self, met : float):
        self.appStatus.method = met
    
    def reset_algo(self):
        self.algoStatus = AlgoStatus()
    
    def save_to_file(self):
        if self.algoStatus.final != None:
            pt = gp.GraphPrinter(self.appStatus.outpath)
            pt.set_graph(self.algoStatus.final)
            pt.set_et(self.algoStatus.finalEts)
            success = pt.write()
            toas = 'Success' if success else 'Write Canceled'
            #display.Display.current().toast(toas)
            print(toas)
        else :
            print("No Skeleton Computed")
            #display.Display.current().toast("No Skeleton Computed")
        
        
    def __runall(self):
        while self.stm.valid():
            self.stm.execute()
            self.stm.to_next()
      
    