# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:27:20 2022

@author: Yigan
"""
import sys
import argparse
import mainalgo as ma

def run(iptImg : str, optFile : str, pthr:float, sthr:float):
    
    ma.SkeletonApp.inst().appStatus.biThresh = sthr
    
    ma.SkeletonApp.inst().appStatus.etThresh = pthr
    ma.SkeletonApp.inst().appStatus.imgpath = iptImg
    ma.SkeletonApp.inst().appStatus.outpath = optFile
    ma.SkeletonApp.inst().run()


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('input',type = str, help='input image')
    parser.add_argument('thresh', type = float, help='segmentation threshold in percentage')
    parser.add_argument('prune',type = float, help='pruning threshold in percentage')
    parser.add_argument('out',type = str, help='output file path and name')
    #parser.print_help()
    
    arg = sys.argv[1:]
    args = parser.parse_args(arg)
    run(args.input,args.out,args.prune,args.thresh)
    #outpath = args.o if args.o is not None else script_dir = Path( __file__ ).parent.absolute()
        
   