import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import matplotlib.pyplot as plt
import plotly_express as px
import tqdm
from tqdm._tqdm_notebook import tqdm_notebook

baseball_df = pd.read_json('server/data/baseball.json')
# basketball_df = pd.read_json('sprt.dev/server/data/basketball.json')
# football_df = pd.read_json('sprt.dev/server/data/football.json')
# hockey_df = pd.read_json('sprt.dev/server/data/hockey.json')

print(baseball_df.head())
