#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""Kernel installer"""

import os
import shutil
from jupyter_client.kernelspec import KernelSpecManager

json ="""{"argv":["python","-m","janschatgptkernel", "-f", "{connection_file}"],
 "display_name":"ChatGPT"
}"""

svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   viewBox="0 0 300 300"
   version="1.1"
   id="svg152"
   width="300"
   height="300"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <defs
     id="defs156" />
  <g
     id="g435"
     transform="matrix(0.12396007,0,0,0.12396007,0.87603993,0.87603993)">
    <path
       d="M 1,578.4 C 1,259.5 259.5,1 578.4,1 h 1249.1 c 319,0 577.5,258.5 577.5,577.4 V 2406 H 578.4 C 259.5,2406 1,2147.5 1,1828.6 Z"
       fill="#74aa9c"
       id="path148" />
    <path
       d="m 1107.3,299.1 c -198,0 -373.9,127.3 -435.2,315.3 -127.3,26.2 -237.2,105.8 -301.6,218.6 -99.3,171.4 -76.6,386.9 56.4,533.8 -41.1,123.1 -27,257.7 38.6,369.2 98.7,172 297.3,260.2 491.6,219.2 86.1,97 209.8,152.3 339.6,151.8 198,0 373.9,-127.3 435.3,-315.3 127.5,-26.3 237.2,-105.9 301,-218.5 99.9,-171.4 77.2,-386.9 -55.8,-533.9 v -0.6 c 41.1,-123.1 27,-257.8 -38.6,-369.8 C 1839.9,497.5 1641.3,409.3 1447.6,450.3 1361,353.5 1237.1,298.5 1107.3,299.1 Z m 0,117.5 -0.6,0.6 c 79.7,0 156.3,27.5 217.6,78.4 -2.5,1.2 -7.4,4.3 -11,6.1 L 952.8,709.3 c -18.4,10.4 -29.4,30 -29.4,51.4 V 1248 L 768.3,1158.6 V 755.8 c -0.1,-187.1 151.6,-338.9 339,-339.2 z m 434.2,141.9 c 121.6,-0.2 234,64.5 294.7,169.8 39.2,68.6 53.9,148.8 40.4,226.5 -2.5,-1.8 -7.3,-4.3 -10.4,-6.1 L 1505.8,740.5 c -18.4,-10.4 -41,-10.4 -59.4,0 L 1024,984.2 V 805.4 L 1372.7,604 c 51.3,-29.7 109.5,-45.4 168.8,-45.5 z M 650,743.5 v 427.9 c 0,21.4 11,40.4 29.4,51.4 l 421.7,243 -155.7,90 L 597.2,1355 C 435.2,1261.2 379.8,1054.1 473.4,892.2 513.1,823.6 575.5,771 650,743.5 Z m 807.9,106 348.8,200.8 c 162.5,93.7 217.6,300.6 123.8,462.8 l 0.6,0.6 c -39.8,68.6 -102.4,121.2 -176.5,148.2 v -428 c 0,-21.4 -11,-41 -29.4,-51.4 L 1302.9,938.8 Z m -256.2,147.5 177.8,102.8 v 205.1 l -177.8,102.8 -177.8,-102.8 v -205.1 z m 279.5,161.6 155.1,89.4 v 402.2 c 0,187.3 -152,339.2 -339,339.2 v -0.6 c -79.1,0 -156.3,-27.6 -217,-78.4 2.5,-1.2 8,-4.3 11,-6.1 l 360.4,-207.5 c 18.4,-10.4 30,-30 29.4,-51.4 z M 1380,1421.9 v 178.8 l -348.8,200.8 c -162.5,93.1 -369.6,38 -463.4,-123.7 h 0.6 c -39.8,-68 -54,-148.8 -40.5,-226.5 2.5,1.8 7.4,4.3 10.4,6.1 l 360.4,208.2 c 18.4,10.4 41,10.4 59.4,0 z"
       fill="#ffffff"
       id="path150" />
  </g>
</svg>
"""

def install_kernelspec():
    kerneldir = "/tmp/janschatgptkernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w") as f:
        f.write(json)

    with open(kerneldir + "logo-svg.svg", "w") as f:
        f.write(svg)
        
    print(' Done!')
    print('Installing Jupyter kernel...', end="")
    
    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'janschatgptkernel', user=os.getenv('USER'))
    
    print(' Done!')
    print('Cleaning up tmp files...', end="")
    
    shutil.rmtree(kerneldir)
    
    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall janschatgptkernel')