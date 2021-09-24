
import schrodinger.maestro as sm
import schrodinger.project as sp
import schrodinger.structure as ss

with open("/home/takacsg/Documents/sh2db/data/path_to_pdbs.txt") as lista:
        for  line in lista:
                      
            input_file=line.strip('\n')
            #entry_name = input_file.split('\')[-1]

            #cluster=line.split("/")[1]
            print(input_file[-1])



def f():
    
    pt = sm.project_table_get()

    

    with open("/home/takacsg/Documents/sh2db/data/path_to_pdbs.txt") as lista:
        for  line in lista:
                      
            input_file=line.strip('\n')
            
            entry_name = input_file.split('/')[-1]
            entry_name = entry_name.split('.')[0]

        #    for st in ss.StructureReader(input_file):
            pt.importStructureFile(input_file,creategroups='all')
            #st = pt.importStructureFile
            #entry_dict[entry_name]= st.property['s_m_entry_id']
    pt.update()

entry_dict = {}
pt.update()
for st in pt:
    entry_dict[structure.property['s_m_title']] = st.property['s_m_entry_id']