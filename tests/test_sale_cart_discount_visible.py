#!/usr/bin/env python
# This file is part sale_cart_discount_visible module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class SaleCartDiscountVisibleTestCase(unittest.TestCase):
    'Test Sale Cart Discount Visible module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('sale_cart_discount_visible')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleCartDiscountVisibleTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
