from structure.models import Structure, Chain, StructureDomain

import requests

def pdb_list_from_pdb(uniprot_id):
    '''Return list of PDB IDs for a Uniprot ID from the PDB database.'''
    request = {
    "query": {
        "type": "group",
        "logical_operator": "and",
        "nodes": [
        {
            "type": "terminal",
            "service": "text",
            "parameters": {
            "operator": "exact_match",
            "value": uniprot_id,
            "attribute": "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession"
            }
        },
        {
            "type": "terminal",
            "service": "text",
            "parameters": {
            "operator": "exact_match",
            "value": "UniProt",
            "attribute": "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_name"
            }
        }
        ]
    },
    "return_type": "entry"
    }

    request_str = str(request).replace(":","%3A").replace(',','%2C').replace(' ','').replace('\'','\"')

    res=requests.get('https://search.rcsb.org/rcsbsearch/v2/query?json='+ request_str )

    return [ i['identifier'] for i in res.json()['result_set'] ]

def pdb_list_from_sh2db(uniprot_id):
    '''Return list of PDB IDs for a Uniprot ID from the SH2db database.'''

    structure_domains = StructureDomain.objects.filter(domain__isoform__protein__accession=uniprot_id)

    pdb_list = []

    for structure_domain in structure_domains:
        pdb_list.append(structure_domain.chain.structure.pdb_code)

    return pdb_list

def to_include(pdb_list, sh2db_list):
    '''Return difference of two lists.'''

    return [ i for i in pdb_list if i not in sh2db_list ]