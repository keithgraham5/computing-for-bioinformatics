"""
NAME:          views\controllers.py
AUTHOR:        Keith Graham (Clinical Scientist)v
EMAIL:         keith.graham5@nhs.net
DATE:          2021
INSTITUTION:   Leeds Teaching Hospital
DESCRIPTION:   Views module. Renders HTML pages and passes in associated data to render on the
               dashboard.
"""

from flask import Blueprint, render_template, request
from app.database.controllers import Database


views = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# get the database class
db_mod = Database()

# Set the route and accepted methods
@views.route('/home/', methods=['GET', 'POST'])
def home():
    """Render the home page of the dashboard passing in data to populate dashboard."""

    pcts = [r[0] for r in db_mod.get_distinct_pcts()]
    if request.method == 'POST':

        form = request.form
        result = 0
        # if selecting PCT for table, update based on user choice
        try:
            selected_pct_data = db_mod.get_n_data_for_PCT(str(form['pct-option']), 5)
        except:
            result = creatinine_clearance_calculator(form['patients-age'],  form['patients-weight'], form['sex'], form['patients-serum'])
            # pick a default PCT to show
            selected_pct_data = db_mod.get_n_data_for_PCT(str(pcts[0]), 5)

            # keep pop up open
            #popup.showCeatCalcFormPopup()

    else:
        # pick a default PCT to show
        selected_pct_data = db_mod.get_n_data_for_PCT(str(pcts[0]), 5)
        # pick a default creatinine rate to show
        result = 0

    # prepare data
    bar_data = generate_barchart_data()
    bar_values = bar_data[0]
    bar_labels = bar_data[1]
    title_data_items = generate_data_for_tiles()


    infection_group_bars = generate_infection_drug_treatment_percent_bars()


    # render the HTML page passing in relevant data
    return render_template('dashboard/index.html', tile_data=title_data_items,
                           pct={'data': bar_values, 'labels': bar_labels}, infection_drug_bars=infection_group_bars,
                           pct_list=pcts, pct_data=selected_pct_data, clearance_data=result)

def generate_data_for_tiles():
    """Generate the data for the four home page titles."""
    return [db_mod.get_total_number_items(), db_mod.average_act_cost(), db_mod.number_unique_items(), db_mod.top_prescribed_item(), db_mod.percent_total_prescriptions()]

def generate_barchart_data():
    """Generate the data needed to populate the barchart."""
    data_values = db_mod.get_prescribed_items_per_pct()
    pct_codes = db_mod.get_distinct_pcts()

    # convert into lists and return
    data_values = [r[0] for r in data_values]
    pct_codes = [r[0] for r in pct_codes]
    return [data_values, pct_codes]

def generate_infection_drug_treatment_percent_bars():
    """Generate percentage bars for infection drug treatments"""
    idata_values = db_mod.get_prescribed_items_per_infection_group()
    idata_labels = db_mod.get_distinct_infection_groups()

    # convert into lists and return
    data_values = [r[0] for r in idata_values]
    pct_codes = [r[0] for r in idata_labels]
    return [idata_values, idata_labels]

def creatinine_clearance_calculator(age, weight, sex, serum):

    if sex == 'm':
        constant = 1.23
        creatinine_clearance_rate = ((140 - int(age)) * int(weight) * constant) / int(serum)
    elif sex == 'f':
        constant = 1.04
        creatinine_clearance_rate = ((140 - int(age)) * int(weight) * constant) / int(serum)
    else:
       creatinine_clearance_rate = 0
    return creatinine_clearance_rate



