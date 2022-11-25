import django
#django.setup()

from django.test import TestCase

# Create your tests here.
import sys
import os

sys.path.append('.')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh2db.settings")
django.setup()

import structure.update

print ( to_include(pdb_list_from_pdb('P40763'), pdb_list_from_sh2db('P40763') ) )