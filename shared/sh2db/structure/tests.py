from django.test import TestCase

# Create your tests here.
import sys

sys.path.append('.')

import update

print ( update.to_include(update.pdb_list_from_pdb('P40763'), update.pdb_list_from_sh2db('P40763') ) )