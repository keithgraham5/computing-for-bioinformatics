"""
NAME:          database\controllers.py
AUTHOR:        Keith Graham (Clinical Scientist)v
EMAIL:         keith.graham5@nhs.net
DATE:          2021
INSTITUTION:   Leeds Teaching Hospital
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""
import numpy
from sqlalchemy import distinct, desc, case
from sqlalchemy.sql import func
from flask import Blueprint

from app import db
from app.database.models import PrescribingData, PracticeData
import sys

database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.query(func.sum(PrescribingData.items).label('total_items')).first()[0])

    def get_prescribed_items_per_pct(self):
        """Return the total items per PCT."""
        return db.session.query(func.sum(PrescribingData.items).label('item_sum')).group_by(PrescribingData.PCT).all()

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        return db.session.query(PrescribingData.PCT).distinct().all()

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()

    def average_act_cost(self):
        """Return the average actual cost for all prescribed medications"""
        avg_cost = db.session.query(func.avg(PrescribingData.ACT_cost)).all()
        avg_cost = float(avg_cost[0][0])
        avg_cost = round(avg_cost, 2)
        return avg_cost

    def number_unique_items(self):
        """Return the number of unique items (prescribed medications)"""
        num_unique = db.session.query(func.count(distinct(PrescribingData.BNF_code))).scalar()
        return num_unique

    def top_prescribed_item(self):
        """Return the name of the top prescribed medication"""
        sum_items = db.session.query(PrescribingData.BNF_code, PrescribingData.BNF_name, func.sum(PrescribingData.items).label('Sum_items')).group_by(PrescribingData.BNF_code).order_by(desc('Sum_items')).first()[1]
        return sum_items

    def percent_total_prescriptions(self):
        """Returns percentage of items"""
        total_items = db.session.query(func.sum(PrescribingData.items)).scalar()
        sum_items2 = db.session.query(PrescribingData.BNF_code, PrescribingData.BNF_name, func.sum(PrescribingData.items).label('Sum_items')).group_by(PrescribingData.BNF_code).order_by(desc('Sum_items')).first()[2]
        percent_total = (sum_items2/total_items)*100
        percent_total = round(percent_total, 2)
        return percent_total

    def get_distinct_infection_groups(self):
        """Returns each unique infection group(based on their BNF code)
        NB: In BNF- infection group treatments are placed under chapter 5; ranging from chapter 5.1 to 5.5
        """
        my_case_stmt = case([(PrescribingData.BNF_code.like('0501%'), 'Antibacterial drugs'),
                             (PrescribingData.BNF_code.like('0502%'), 'Antifungal drugs'),
                             (PrescribingData.BNF_code.like('0503%'), 'Antiviral drugs'),
                             (PrescribingData.BNF_code.like('0504%'), 'Antiprotozoal drugs'),
                             (PrescribingData.BNF_code.like('0505%'), 'Antihelmintics')])
        infection_group_filtered = db.session.query(distinct(my_case_stmt.label('Infection group'))).filter(PrescribingData.BNF_code.like('05%')).all()
        return infection_group_filtered


    def get_prescribed_items_per_infection_group(self):
        """Returns percentage of all treatments for each infection group"""

        my_case_stmt = case([(PrescribingData.BNF_code.like('0501%'), 'Antibacterial drugs'),
                             (PrescribingData.BNF_code.like('0502%'), 'Antifungal drugs'),
                             (PrescribingData.BNF_code.like('0503%'), 'Antiviral drugs'),
                             (PrescribingData.BNF_code.like('0504%'), 'Antiprotozoal drugs'),
                             (PrescribingData.BNF_code.like('0505%'), 'Anthelmintics')])
        query1 = db.session.query(func.sum(PrescribingData.items).label('item_sum')).filter(
            PrescribingData.BNF_code.like('05%')).group_by(my_case_stmt).order_by(PrescribingData.BNF_code).all()
        query2 = int(db.session.query(func.sum(PrescribingData.items).label('total_sum')).filter(PrescribingData.BNF_code.like('05%')).first()[0])
        query1 = numpy.array(query1)
        percent_total = (query1/query2) * 100
        percent_total = list(percent_total.round(2))
        print(percent_total)
        return percent_total






