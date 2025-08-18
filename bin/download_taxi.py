from datetime import date
from spark_optimisation.taxi import raw

START_DATE = date(2024, 1, 1)
END_DATE = date(2024, 12, 31)

raw.downloads(raw.START_DATE, raw.END_DATE)