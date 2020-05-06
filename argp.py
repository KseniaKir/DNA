#!/usr/bin/env python
# coding: utf-8

# In[27]:


import argparse
import sys
import solid
import argparse
import os

from solid import *
from solid.objects import sphere

parser=argparse.ArgumentParser(prog='DNA molecule',
                                 description='''Creating your own DNA molecule''')
parser.add_argument('-r', '---size', type=int, help='Radius of carbon atoms in molecule')
parser.add_argument('-s', '---seq', type=str, help='Sequence')
args=parser.parse_args("")

def ostov53(z, angle, nuc):
    element=(union()(
        color("Gainsboro")(translate([radius,0,0])(sphere(8))),
        color("Gainsboro")(translate([radius, 15, 0])(sphere (8))),
        color("Gainsboro")(translate([radius, 20, 15])(sphere (8))),
        color("Gainsboro")(translate([radius, -5, 15])(sphere (8))),
        color("Gainsboro")(translate([radius, 7.5, 25])(sphere (10))),
        color("Gainsboro")(translate([radius, -15, 25])(sphere (8))),
        color("Yellow")(translate([radius, -20, 42.5])(sphere (10))),
        color("Yellow")(translate([radius, -20, 60])(sphere (13))),
        color("Yellow")(translate([radius, -20, 80])(sphere (10))),
        color("Yellow")(translate([radius, -40, 60])(sphere (10))),
        color("Yellow")(translate([radius, 0, 60])(sphere (10)))))
        
    element1=translate([0,0,z])(rotate(angle)(element))
    element2=translate([0, 0, z])(rotate(angle)((translate([0,0,80])(rotate(a=[0, 180, 0])(element)))))
    
    if nuc=="A":
#        nuc2="T"
        nucleus1=rotate(angle)(translate([radius/2,0,z+20])((translate([0,30,0])(rotate(150)(union()(
            color("Green")(translate([0,0,0])(sphere(9))),
            color("Blue")(translate([-10,7.5,0])(sphere(8))),
            color("Green")(translate([-20,8,0])(sphere(9))),
            color("Blue")(translate([-30,15,0])(sphere(8))),
            color("Green")(translate([-20,26,0])(sphere(9))),
            color("Blue")(translate([-10,22.5,0])(sphere(8))),
            color("Blue")(translate([0,30,0])(sphere(8))),
            color("Green")(translate([10,22.5,0])(sphere(9))),
            color("Blue")(translate([10,7.5,0])(sphere(8))),
            color("Green")(translate([0,44,0])(sphere(9))),
            color("Gray")(translate([0,54,0])(sphere(4))),
            color("Gray")(translate([10,44,0])(sphere(4))),
        ))))))
        nucleus2=rotate(angle+180)(translate([radius/1.7,0,z+20])(translate([0,10,0])(rotate(25)((union()(     
            color("Blue")(translate([0,0,0])(sphere(8))),
            color("Green")(translate([-10,7.5,0])(sphere(9))),
            color("Blue")(translate([-10,22.5,0])(sphere(8))),
            color("Blue")(translate([0,30,0])(sphere(8))),
            color("Blue")(translate([10,22.5,0])(sphere(8))),
            color("Green")(translate([10,7.5,0])(sphere(9))),
            color("Red")(translate([0,-14,0])(sphere(10))),
            color("Red")(translate([-24,25,0])(sphere(10))),
            color("Gray")(translate([-20,7.5,0])(sphere(4))),
        ))))))  
        
    elif nuc=="G":
#        nuc2="C"
        nucleus1=rotate(angle)(translate([radius/2.5,0,z+20])(translate([0,20,0])(rotate(170)((union()(     
            color("Green")(translate([0,0,0])(sphere(9))),
            color("Blue")(translate([-10,7.5,0])(sphere(8))),
            color("Green")(translate([-20,4,0])(sphere(9))),
            color("Blue")(translate([-30,15,0])(sphere(8))),
            color("Green")(translate([-20,26,0])(sphere(9))),
            color("Blue")(translate([-10,22.5,0])(sphere(8))),
            color("Blue")(translate([0,30,0])(sphere(8))),
            color("Green")(translate([10,22.5,0])(sphere(9))),
            color("Blue")(translate([10,7.5,0])(sphere(8))),
            color("Green")(translate([20,0,0])(sphere(9))),
            color("Gray")(translate([20,-10,0])(sphere(4))),
            color("Gray")(translate([30,0,0])(sphere(4))),
            color("Red")(translate([0,46,0])(sphere(10))),            
            color("Gray")(translate([20,22.5,0])(sphere(4))),            
        ))))))     
        nucleus2=rotate(angle+180)(translate([radius/2,0,z+20])(translate([0,10,0])(rotate(0)((union()(  
            color("Blue")(translate([0,0,0])(sphere(8))),
            color("Green")(translate([-10,7.5,0])(sphere(9))),
            color("Blue")(translate([-10,22.5,0])(sphere(8))),
            color("Blue")(translate([0,30,0])(sphere(8))),
            color("Blue")(translate([10,22.5,0])(sphere(8))),
            color("Green")(translate([10,7.5,0])(sphere(9))),
            color("Red")(translate([0,-14,0])(sphere(10))),
            color("Green")(translate([-24,25,0])(sphere(9))),
            color("Gray")(translate([-24,35,0])(sphere(4))),
            color("Gray")(translate([-34,25,0])(sphere(4))),
        ))))))        
            
    elif nuc=="C":
#        nuc2="G"
        nucleus1=rotate(angle)(translate([radius/2,0,z+20])(translate([0,5,0])(rotate(5)((union()(     
            color("Blue")(translate([0,0,0])(sphere(8))),
            color("Green")(translate([-10,7.5,0])(sphere(9))),
            color("Blue")(translate([-10,22.5,0])(sphere(8))),
            color("Blue")(translate([0,30,0])(sphere(8))),
            color("Blue")(translate([10,22.5,0])(sphere(8))),
            color("Green")(translate([10,7.5,0])(sphere(9))),
            color("Red")(translate([0,-14,0])(sphere(10))),
            color("Green")(translate([-24,25,0])(sphere(9))),
            color("Gray")(translate([-24,35,0])(sphere(4))),
            color("Gray")(translate([-34,25,0])(sphere(4))),
        ))))))                
        nucleus2=rotate(angle+180)(translate([radius/2,0,z+20])(translate([0,20,0])(rotate(160)((union()( 
            color("Green")(translate([0,0,0])(sphere(9))),
            color("Blue")(translate([-10,7.5,0])(sphere(8))),
            color("Green")(translate([-20,4,0])(sphere(9))),
            color("Blue")(translate([-30,15,0])(sphere(8))),
            color("Green")(translate([-20,26,0])(sphere(9))),
            color("Blue")(translate([-10,22.5,0])(sphere(8))),
            color("Blue")(translate([0,30,0])(sphere(8))),
            color("Green")(translate([10,22.5,0])(sphere(9))),
            color("Blue")(translate([10,7.5,0])(sphere(8))),
            color("Green")(translate([20,0,0])(sphere(9))),
            color("Gray")(translate([20,-10,0])(sphere(4))),
            color("Gray")(translate([30,0,0])(sphere(4))),
            color("Red")(translate([0,46,0])(sphere(10))),            
            color("Gray")(translate([20,22.5,0])(sphere(4))),         
        ))))))
                 
    elif nuc=="T":
#        nuc2="A"
        nucleus1=rotate(angle)(translate([radius/1.6,0,z+20])(translate([0,0,0])(rotate(30)((union()(   
            color("Blue")(translate([0,0,0])(sphere(8))),
            color("Green")(translate([-10,7.5,0])(sphere(9))),
            color("Blue")(translate([-10,22.5,0])(sphere(8))),
            color("Blue")(translate([0,30,0])(sphere(8))),
            color("Blue")(translate([10,22.5,0])(sphere(8))),
            color("Green")(translate([10,7.5,0])(sphere(9))),
            color("Red")(translate([0,-14,0])(sphere(10))),
            color("Red")(translate([-24,25,0])(sphere(10))),
            color("Gray")(translate([-20,7.5,0])(sphere(4))),
        ))))))
        nucleus2=rotate(angle+180)(translate([radius/1.7,0,z+20])((translate([0,30,0])(rotate(137)(union()(
            color("Green")(translate([0,0,0])(sphere(9))),
            color("Blue")(translate([-10,7.5,0])(sphere(8))),
            color("Green")(translate([-20,8,0])(sphere(9))),
            color("Blue")(translate([-30,15,0])(sphere(8))),
            color("Green")(translate([-20,26,0])(sphere(9))),
            color("Blue")(translate([-10,22.5,0])(sphere(8))),
            color("Blue")(translate([0,30,0])(sphere(8))),
            color("Green")(translate([10,22.5,0])(sphere(9))),
            color("Blue")(translate([10,7.5,0])(sphere(8))),
            color("Green")(translate([0,44,0])(sphere(9))),
            color("Gray")(translate([0,54,0])(sphere(4))),
            color("Gray")(translate([10,44,0])(sphere(4))),
        ))))))     
            
    return element1+element2+nucleus1+nucleus2

a=0
g=0
i=0
radius=75
number=10



if __name__ == '__main__':
        for nuc in args.seq:
            nuc=nuc.capitalize()
            if (nuc!="A" and nuc!="T" and nuc!="C" and nuc!="G"):
                print ("Wrong sequence!")
                break
            a += ostov53(g, i*360/number, nuc)
            g+=50
            i+=1
        
        a=scale([args.size,args.size,args.size])(a)
        out_dir = sys.argv[1] if len(sys.argv) > 1 else None  
        file_out = scad_render_to_file(a, out_dir=out_dir, include_orig_code=True)

#print ("You're going to create your own DNA sequence!")
#def main():
#    while True:
#        try:
#            s = int(input("Enter the size of the nucleotide (integer number): "))
#            break
#        except ValueError:
#            print ("You should enter an integer number, try again")
#    return(s)


#size=main()
#seq=input(str("Enter DNA sequence (ACGT...) "))




# In[26]:


import argparse
parser = argparse.ArgumentParser("")
parser.add_argument("echo")
args = parser.parse_args("")
print(args.echo)


# In[ ]:




