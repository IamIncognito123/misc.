#parse the sample species and genus abundance tables and prepare species list abundance tables
#keystone list, pathogen list, pathway list, phylum ratios
#use: python3 parse_tax_abd_lists.py folder sample_ID; for example: pbg0530.230511.zymo 1235364	
import os, sys

folder = sys.argv[1]
sample = sys.argv[2]
species_abd = {}
inp = open(f"/{folder}/midog.a.Bac16Sv13/taxa_plots/sorted_otu_L7.txt", 'r')
line = inp.readline()
line = inp.readline()
ll = line.strip('\n').split('\t')
pos = ll.index(sample)
line = inp.readline()
while line:
  ll = line.strip('\n').split('\t')
  species_name = ' '.join(ll[0].split(';')[-2:len(ll)]).replace('g__', '').replace('s__', '')
  species_abd[species_name] = ll[pos]
  line = inp.readline()
inp.close()

genus_abd = {}
inp = open(f"/{folder}/midog.a.Bac16Sv13/taxa_plots/sorted_otu_L6.txt", 'r')
line = inp.readline()
line = inp.readline()
line = inp.readline()
while line:
  ll = line.strip('\n').split('\t')
  genus_name = ll[0].split(';')[-1].replace('g__', '')
  genus_abd[genus_name] = ll[pos]
  line = inp.readline()
inp.close()





