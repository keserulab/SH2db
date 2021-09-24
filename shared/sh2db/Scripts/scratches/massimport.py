import schrodinger.maestro as sm
import schrodinger.project as sp
import schrodinger.structure as ss


def f():
    
    pt = sm.project_table_get()

    with open("/home/takacsg/Documents/SH2DB/paths.txt") as lista:
        for  line in lista:
                      
            input_file=line.strip('\n')
            #cluster=line.split("/")[1]

        #    for st in ss.StructureReader(input_file):
            pt.importStructureFile(input_file,creategroups='all')

    pt.update()
