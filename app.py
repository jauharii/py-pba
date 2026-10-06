import streamlit as s
import pandas as p
from biasiswa import *

#PAGE CONFIGURATION
s.set_page_config(
    page_title="Scholarship Qualification System",
    layout="centered"
)
s.title("Scholarship Qualification System")
s.caption( "DFK50083 Python Programming — Problem Based Assignment")

name = s.text_input("Full Name", placeholder="e.g. Ahmad Ali")
cgpa = s.number_input("CGPA", step=0.1)
income = s.number_input("Household Income (RM)", step=100.0)
cocu = False
cocu = s.checkbox("Co-Curricular Activities")
level = s.selectbox(
    "Academic Level",
    ["-- Select Level --", "Diploma", "Degree"]
)

if s.button("Check Qualification"):
    if cgpa <= 0 or cgpa > 4.0:
        s.error("Please enter a valid CGPA between 0.0 and 4.0.")
    elif income < 0:
        s.error("Please enter a valid household income (non-negative).")
    elif level == "-- Select Level --":
        s.error("Please select an academic level.")
    elif name == "":
        s.error("Please enter name.")
    else:
        try:
            app = Application(name, cgpa, income, cocu)
            s.subheader("Results")
            s.write(f"Applicant: {name}")
            s.write(f"Academic Level: {level}")
            s.text(app.describe())
            s.metric("Score", app.score)
            (s.success if is_qualified(cgpa, income, cocu) else s.warning)(app.application_status())

        except Exception as e:
            s.error(f"Processing error: {e}")

