# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import print_function

from astropy.tests.helper import remote_data
from astropy.table import Table
import astropy.units as u
import requests
import imp

import sys
sys.path.append("/Users/joel/Documents/school/astroquery/astroquery/")
from astroquery.nist import Nist

imp.reload(requests)


@remote_data
class TestNist:

    def test_query_async(self):
        response = nist.core.Nist.query_async(4000 * u.AA, 7000 * u.AA)
        assert response is not None

    def test_query(self):
        result = nist.core.Nist.query(4000 * u.AA, 7000 * u.AA)
        assert isinstance(result, Table)
