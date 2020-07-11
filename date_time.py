from datetime import datetime
import pandas as pd

def today():
	today=datetime.now()
	updated_today=today.strftime("%m/%d/%Y")

	return updated_today

today()