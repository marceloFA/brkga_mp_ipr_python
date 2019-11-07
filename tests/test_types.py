"""
test_types.py: tests for types.

(c) Copyright 2019, Carlos Eduardo de Andrade. All Rights Reserved.

This code is released under LICENSE.md.

Created on:  Nov 06, 2019 by ceandrade
Last update: Nov 06, 2019 by ceandrade

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

import unittest
from brkga_mp_ipr.types import *

class Test(unittest.TestCase):
    """
    Test units for types.
    """

    ###########################################################################

    def setUp(self):
        """
        Set up some configurations.
        """

        Test.maxDiff = None

    ###########################################################################

    def test_BrkgaParams(self):
        """
        Test BrkgaParams constructor.
        """

        brkga_params = BrkgaParams()

        self.assertEqual(brkga_params.population_size, 0)
        self.assertEqual(brkga_params.elite_percentage, 0.0)
        self.assertEqual(brkga_params.mutants_percentage, 0.0)
        self.assertEqual(brkga_params.num_elite_parents, 0)
        self.assertEqual(brkga_params.total_parents, 0)
        self.assertEqual(brkga_params.bias_type, BiasFunction.CONSTANT)
        self.assertEqual(brkga_params.num_independent_populations, 0)
        self.assertEqual(brkga_params.pr_number_pairs, 0)
        self.assertEqual(brkga_params.pr_minimum_distance, 0.0)
        self.assertEqual(brkga_params.pr_type, PathRelinkingType.DIRECT)
        self.assertEqual(brkga_params.pr_selection, PathRelinkingSelection.BESTSOLUTION)
        self.assertEqual(brkga_params.alpha_block_size, 0.0)
        self.assertEqual(brkga_params.pr_percentage, 0.0)

    ###########################################################################

    def test_ExternalControlParams(self):
        """
        Test ExternalControlParams constructor.
        """

        extra_params = ExternalControlParams()
        self.assertEqual(extra_params.exchange_interval, 0)
        self.assertEqual(extra_params.num_exchange_indivuduals, 0)
        self.assertEqual(extra_params.reset_interval, 0)

        extra_params = ExternalControlParams(10, 20, 30)
        self.assertEqual(extra_params.exchange_interval, 10)
        self.assertEqual(extra_params.num_exchange_indivuduals, 20)
        self.assertEqual(extra_params.reset_interval, 30)

        extra_params = ExternalControlParams(
            exchange_interval = 30,
            num_exchange_indivuduals = 10,
            reset_interval = 20
        )
        self.assertEqual(extra_params.exchange_interval, 30)
        self.assertEqual(extra_params.num_exchange_indivuduals, 10)
        self.assertEqual(extra_params.reset_interval, 20)

    ###########################################################################

    def test_PathRelinkingResult(self):
        """
        Test PathRelinkingResult bitwise operations.
        """

        PRR = PathRelinkingResult
        self.assertEqual(PRR.TOO_HOMOGENEOUS | PRR.TOO_HOMOGENEOUS, PRR.TOO_HOMOGENEOUS)
        self.assertEqual(PRR.TOO_HOMOGENEOUS | PRR.NO_IMPROVEMENT, PRR.NO_IMPROVEMENT)
        self.assertEqual(PRR.TOO_HOMOGENEOUS | PRR.ELITE_IMPROVEMENT, PRR.ELITE_IMPROVEMENT)
        self.assertEqual(PRR.TOO_HOMOGENEOUS | PRR.BEST_IMPROVEMENT, PRR.BEST_IMPROVEMENT)
        self.assertEqual(PRR.NO_IMPROVEMENT | PRR.NO_IMPROVEMENT, PRR.NO_IMPROVEMENT)
        self.assertEqual(PRR.NO_IMPROVEMENT | PRR.ELITE_IMPROVEMENT, PRR.ELITE_IMPROVEMENT)
        self.assertEqual(PRR.NO_IMPROVEMENT | PRR.BEST_IMPROVEMENT, PRR.BEST_IMPROVEMENT)
        self.assertEqual(PRR.ELITE_IMPROVEMENT | PRR.ELITE_IMPROVEMENT, PRR.ELITE_IMPROVEMENT)
        self.assertEqual(PRR.ELITE_IMPROVEMENT | PRR.BEST_IMPROVEMENT, PRR.BEST_IMPROVEMENT)
        self.assertEqual(PRR.BEST_IMPROVEMENT | PRR.BEST_IMPROVEMENT, PRR.BEST_IMPROVEMENT)

###############################################################################

if __name__ == "__main__":
    unittest.main()