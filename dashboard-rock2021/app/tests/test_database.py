"""
NAME:          test_database.py
AUTHOR:        Keith Graham (Clinical Scientist)v
EMAIL:         keith.graham5@nhs.net
DATE:          2021
INSTITUTION:   Leeds Teaching Hospital
DESCRIPTION:   Suite of tests for testing the dashboards database
               functionality.
"""

from app.views.controllers import creatinine_clearance_calculator
import unittest
from app.database.controllers import Database


class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()

    def tearDown(self):
        """Run post each test."""
        pass

    def test_get_total_number_items(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_total_number_items(), 8218165)

    def test_get_number_unique_items(self):
        """Test that the total number of unique items returns the correct value."""
        self.assertEquals(self.db_mod.number_unique_items(), 13935)

    def test_top_prescribed_item(self):
        """Test that the top_prescribed_item returns the correct medicine."""
        self.assertEquals(self.db_mod.top_prescribed_item(), "Omeprazole_Cap E/C 20mg")

    def test_percent_total_prescriptions(self):
        """Test that the top_prescribed_item returns the correct medicine."""
        self.assertEquals(self.db_mod.percent_total_prescriptions(), 2.75)


    def test_get_prescribed_items_per_infection_group(self):
        """Test that the function returns the correct percentages"""
        self.assertEquals(self.db_mod.get_prescribed_items_per_infection_group(), ([82.25, 5.22, 2.68, 9.62, 0.23]))

    def test_get_distinct_infection_groups(self):
        """Test that the function returns a list of drug categories"""
        self.assertEquals(self.db_mod.get_distinct_infection_groups(), [('Antibacterial drugs',), ('Antifungal drugs',),
                                                                        ('Antiviral drugs',), ('Antiprotozoal drugs',), ('Antihelmintics',)])


   

class ViewsControllersTests(unittest.TestCase):
    """Class for testing ...."""
    def test_creatinine_calc(self):
        self.assertEquals(creatinine_clearance_calculator(80, 80, 'm', 80), 73.8)

if __name__ == "__main__":
    unittest.main()

