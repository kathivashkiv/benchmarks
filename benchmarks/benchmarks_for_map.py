# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import sunpy.data.sample
import sunpy.map

class TimeSuite:
    """
    An example benchmark that times the performance of sunpy map
    creation
    """
    def setup(self):
        self._map = sunpy.data.sample.AIA_171_IMAGE

    def time_create_sunpy_map(self):
        aia_map = sunpy.map.Map(self._map)

class MemSuite:
    def mem_sunpy_map(self):
        return sunpy.map.Map(AIA_MAP)

class PeakMemorySuite:
    def setup(self):
        self._map = sunpy.data.sample.AIA_171_IMAGE

    def peakmem_sunpy_map(self):
        aia_map = sunpy.map.Map(AIA_MAP)
