from datetime import date
from spark_optimisation.taxi import raw, cleanse
from spark_optimisation.lib import end_of_months_between

START_DATE = date(2024, 1, 1)
END_DATE = date(2024, 12, 31)

raw.downloads(START_DATE, END_DATE)
cleanse.cleanses(START_DATE, END_DATE)
