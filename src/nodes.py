#!/usr/bin/env python

# Notes
## Run as python3
## gc.collect() vs %reset -f

import pandas as pd
from io import StringIO

import time 
from datetime import datetime

import csv

# Create time stamp
timeStringNow = datetime.now().strftime("+%Y-%m-%dT00:00:00Z") 
start_time = time.time()

activesite = pd.read_json('files/ndjson/activesite.ndjson', lines=True) 
anatomy = pd.read_json('files/ndjson/anatomy.ndjson', lines=True) 
bindingsite = pd.read_json('files/ndjson/bindingsite.ndjson', lines=True) 
biologicalpathway = pd.read_json('files/ndjson/biologicalpathway.ndjson', lines=True) 
biologicalprocess = pd.read_json('files/ndjson/biologicalprocess.ndjson', lines=True) 
cellularcomponent = pd.read_json('files/ndjson/cellularcomponent.ndjson', lines=True) 
chemicalhazard = pd.read_json('files/ndjson/chemicalhazard.ndjson', lines=True) 
disease = pd.read_json('files/ndjson/disease.ndjson', lines=True) 
medicalspecialty = pd.read_json('files/ndjson/medicalspecialty.ndjson', lines=True) 
molecularfunction = pd.read_json('files/ndjson/molecularfunction.ndjson', lines=True) 
proteindomain = pd.read_json('files/ndjson/proteindomain.ndjson', lines=True) 
proteinfamily = pd.read_json('files/ndjson/proteinfamily.ndjson', lines=True) 
sequencevariant = pd.read_json('files/ndjson/sequencevariant.ndjson', lines=True) 
structuralmotif = pd.read_json('files/ndjson/structuralmotif.ndjson', lines=True) 
symptom = pd.read_json('files/ndjson/symptom.ndjson', lines=True) 

end_time = time.time() # 30 sec remote, 3 min local
print((end_time - start_time)/60, "to read in these .ndjson files") 

timeStringNow = datetime.now().strftime("+%Y-%m-%dT00:00:00Z") 
start_time = time.time()

with open('files/csv/activesite.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index,row in activesite.iterrows():
        print(row['id']+"\tActive Site\t"+row['labels']['en']['value'], file = file)
activesitefinal = pd.read_csv('files/csv/activesite.csv', sep="\t")

with open('files/csv/anatomy.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index,row in anatomy.iterrows():
        print(row['id']+"\tAnatomical Structure\t"+row['labels']['en']['value'], file = file)
anatomyfinal = pd.read_csv('files/csv/anatomy.csv', sep="\t")

with open('files/csv/bindingsite.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index,row in bindingsite.iterrows():
        print(row['id']+"\tBinding Site\t"+row['labels']['en']['value'], file = file)
bindingsitefinal = pd.read_csv('files/csv/bindingsite.csv', sep="\t")

with open('files/csv/biologicalpathway.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index,row in biologicalpathway.iterrows():
        print(row['id']+"\tBiological Pathway\t"+row['labels']['en']['value'], file = file)
biologicalpathwayfinal = pd.read_csv('files/csv/biologicalpathway.csv', sep="\t")

with open('files/csv/biologicalprocess.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index, row in biologicalprocess.iterrows():
        if "en" in row["labels"].keys():
            print(row['id']+"\tBiological Process\t"+row['labels']['en']['value'], file = file)
        else:
            print(row["id"]+"\tBiological Process\t", file = file)
biologicalprocessfinal = pd.read_csv('files/csv/biologicalprocess.csv', sep="\t")

with open('files/csv/cellularcomponent.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index, row in cellularcomponent.iterrows():
        if "en" in row["labels"].keys():
            print(row['id']+"\tCellular Component\t"+row['labels']['en']['value'], file = file)
        else:
            print(row["id"]+"\tCellular Component\t", file = file)
cellularcomponentfinal = pd.read_csv('files/csv/cellularcomponent.csv', sep="\t")

with open('files/csv/chemicalhazard.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index, row in chemicalhazard.iterrows():
        if "en" in row["labels"].keys():
            print(row['id']+"\tChemical Hazard\t"+row['labels']['en']['value'], file = file)
        else:
            print(row["id"]+"\tChemical Hazard\t", file = file)
chemicalhazardfinal = pd.read_csv('files/csv/chemicalhazard.csv', sep="\t")

with open('files/csv/disease.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index, row in disease.iterrows():
        if "en" in row["labels"].keys():
            print(row['id']+"\tDisease\t"+row['labels']['en']['value'], file = file)
        else:
            print(row["id"]+"\tDisease\t", file = file)
diseasefinal = pd.read_csv('files/csv/disease.csv', sep="\t")

with open('files/csv/medicalspecialty.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index, row in medicalspecialty.iterrows():
        if "en" in row["labels"].keys():
            print(row['id']+"\tMedical Specialty\t"+row['labels']['en']['value'], file = file)
        else:
            print(row["id"]+"\tMedical Specialty\t", file = file)
medicalspecialtyfinal = pd.read_csv('files/csv/medicalspecialty.csv', sep="\t")

with open('files/csv/molecularfunction.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index,row in molecularfunction.iterrows():
        print(row['id']+"\tMolecular Function\t"+row['labels']['en']['value'], file = file)
molecularfunctionfinal = pd.read_csv('files/csv/molecularfunction.csv', sep="\t")

with open('files/csv/proteindomain.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index, row in proteindomain.iterrows():
        if "en" in row["labels"].keys():
            print(row['id']+"\tProtein Domain\t"+row['labels']['en']['value'], file = file)
        else:
            print(row["id"]+"\tProtein Domain\t", file = file)
proteindomainfinal = pd.read_csv('files/csv/proteindomain.csv', sep="\t")

with open('files/csv/proteinfamily.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index, row in proteinfamily.iterrows():
        if "en" in row["labels"].keys():
            print(row['id']+"\tProtein Family\t"+row['labels']['en']['value'], file = file)
        else:
            print(row["id"]+"\tProtein Family\t", file = file)
proteinfamilyfinal = pd.read_csv('files/csv/proteinfamily.csv', sep="\t")

with open('files/csv/sequencevariant.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index, row in sequencevariant.iterrows():
        if "en" in row["labels"].keys():
            print(row['id']+"\tSequence Variant\t"+row['labels']['en']['value'], file = file)
        else:
            print(row["id"]+"\tSequence Variant\t", file = file)
sequencevariantfinal = pd.read_csv('files/csv/sequencevariant.csv', sep="\t")

with open('files/csv/structuralmotif.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index, row in structuralmotif.iterrows():
        if "en" in row["labels"].keys():
            print(row['id']+"\tStructural Motif\t"+row['labels']['en']['value'], file = file)
        else:
            print(row["id"]+"\tStructural Motif\t", file = file)
structuralmotiffinal = pd.read_csv('files/csv/structuralmotif.csv', sep="\t")

with open('files/csv/symptom.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for index, row in symptom.iterrows():
        if "en" in row["labels"].keys():
            print(row['id']+"\tSymptom\t"+row['labels']['en']['value'], file = file)
        else:
            print(row["id"]+"\tSymptom\t", file = file)
symptomfinal = pd.read_csv('files/csv/symptom.csv', sep="\t")

end_time = time.time() # 30 sec remote
print((end_time - start_time)/60, "to convert these .ndjson to .csv") 

import gc

timeStringNow = datetime.now().strftime("+%Y-%m-%dT00:00:00Z") 
start_time = time.time()
compound = pd.read_json('files/ndjson/compound.ndjson', lines=True, chunksize=5)
end_time = time.time() # 1 min remote
print((end_time - start_time)/60, "to read compound .ndjson") 

timeStringNow = datetime.now().strftime("+%Y-%m-%dT00:00:00Z") 
start_time = time.time()
with open('files/csv/compound.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for chunk in compound:
        for index,row in chunk.iterrows():
            if 'en' in row['labels'].keys():
                print(row['id']+"\tCompound\t"+row['labels']['en']['value'], file = file)
            else: 
                print(row['id']+"\tCompound\t", file = file)
end_time = time.time() # 32 min remote
print((end_time - start_time)/60, "to convert compound .ndjson to .csv")

del compound
del file
gc.collect()

import gc
import pandas as pd
from io import StringIO
import time 
from datetime import datetime
import csv

timeStringNow = datetime.now().strftime("+%Y-%m-%dT00:00:00Z") 
start_time = time.time()
gene = pd.read_json('files/ndjson/gene.ndjson', lines=True, chunksize=5)
end_time = time.time() # 15.5 min remote
print((end_time - start_time)/60, "to read gene .ndjson")

timeStringNow = datetime.now().strftime("+%Y-%m-%dT00:00:00Z") 
start_time = time.time()
with open('files/csv/gene.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for chunk in gene:
        for index,row in chunk.iterrows():
            if 'en' in row['labels'].keys():
                print(row['id']+"\tGene\t"+row['labels']['en']['value'], file = file)
            else: 
                print(row['id']+"\tGene\t", file = file)
end_time = time.time() # 39 min remote
print((end_time - start_time)/60, "to convert gene .ndjson to .csv")

del gene
gc.collect()

import pandas as pd
from io import StringIO
import time 
from datetime import datetime
import csv

timeStringNow = datetime.now().strftime("+%Y-%m-%dT00:00:00Z") 
start_time = time.time()
protein = pd.read_json('files/ndjson/protein.ndjson', lines=True, chunksize=5)
end_time = time.time() # 2 min remote
print((end_time - start_time)/60, "to read protein .ndjson")

timeStringNow = datetime.now().strftime("+%Y-%m-%dT00:00:00Z") 
start_time = time.time()
with open('files/csv/protein.csv', 'w') as file:  
    writer = csv.writer(file)
    writer.writerow([':ID\t', ':LABEL\t', 'name'])
    for chunk in protein:
        for index,row in chunk.iterrows():
            if 'en' in row['labels'].keys():
                print(row['id']+"\tProtein\t"+row['labels']['en']['value'], file = file)
            else: 
                print(row['id']+"\tProtein\t", file = file)
end_time = time.time() # 33 min remote
print((end_time - start_time)/60, "to convert protein .ndjson to .csv")

activesitefinal = pd.read_csv('files/csv/activesite.csv', sep="\t") 
anatomyfinal = pd.read_csv('files/csv/anatomy.csv', sep="\t") 
biologicalpathwayfinal = pd.read_csv('files/csv/biologicalpathway.csv', sep="\t")
biologicalprocessfinal = pd.read_csv('files/csv/biologicalprocess.csv', sep="\t")
bindingsitefinal = pd.read_csv('files/csv/bindingsite.csv', sep="\t")
cellularcomponentfinal = pd.read_csv('files/csv/cellularcomponent.csv', sep="\t")
chemicalhazardfinal = pd.read_csv('files/csv/chemicalhazard.csv', sep="\t")
compoundfinal = pd.read_csv('files/csv/compound.csv', sep="\t")
diseasefinal = pd.read_csv('files/csv/disease.csv', sep="\t")
genefinal = pd.read_csv('files/csv/gene.csv', sep="\t")
medicalspecialtyfinal = pd.read_csv('files/csv/medicalspecialty.csv', sep="\t")
molecularfunctionfinal = pd.read_csv('files/csv/molecularfunction.csv', sep="\t")
proteinfinal = pd.read_csv('files/csv/protein.csv', sep="\t")
proteindomainfinal = pd.read_csv('files/csv/proteindomain.csv', sep="\t")
proteinfamilyfinal = pd.read_csv('files/csv/proteinfamily.csv', sep="\t")
sequencevariantfinal = pd.read_csv('files/csv/sequencevariant.csv', sep="\t")
structuralmotiffinal = pd.read_csv('files/csv/structuralmotif.csv', sep="\t")
symptomfinal = pd.read_csv('files/csv/symptom.csv', sep="\t")

nodes = pd.concat([activesitefinal, anatomyfinal, biologicalpathwayfinal, 
                   biologicalprocessfinal, bindingsitefinal, cellularcomponentfinal,
                   chemicalhazardfinal, compoundfinal, diseasefinal, 
                   genefinal, medicalspecialtyfinal, molecularfunctionfinal, 
                   proteinfinal, proteindomainfinal, proteinfamilyfinal, 
                   sequencevariantfinal, structuralmotiffinal, symptomfinal], axis=0)
nodes.to_csv('nodes.csv')