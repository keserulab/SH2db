#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import sys
import os

# importing table to get the needed folders names
table = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_struct.csv')
print(table.head())

print("TABLE READING HAS FINISHED")

# Creating the needed folders:
    # The system:
# CATEGORY folders / GENE name folders / folders for every PDB ID (entries)

# creating the category folders:
x = 0
for cat in table["Category"].unique():
    os.system('mkdir -p /home/takacsg/Documents/sh2db/Stuctures/'+cat+'/')
    if x%1 ==  0:
        print("Already created folders {} based on category folders".format(x))
    x += 1
   

# -p : no error if existing, make parent directories as needed
print("CATEGORY FOLDER ARE READY")

# creating the GENE name folders:
x = 0
for cat in table["Category"].unique():
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        os.system('mkdir -p /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/')
        if x%1 == 0:
            print("Already created folders {} based on gene names".format(x))
        x += 1

print("GENE NAME FOLDERS INSIDE THE CATEGORY FOLDERS ARE READY")

# creating the PDB ID folders (inside the category folders:
x = 0
for cat in table["Category"].unique():
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            os.system('mkdir -p /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/')
            if x%1 == 0:
                print("Already created folders {} PDB entries".format(x))
            x += 1

print("ALREADY CREATED THE FOLDER SYSTEM.")

