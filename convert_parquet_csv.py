import pandas as pd
import pyarrow.parquet as pq

data = pq.read_table('/Users/Lenovo1/Desktop/BAHADIR/Github_Projects/taxidata.parquet').to_pandas()
data.to_csv('/Users/Lenovo1/Desktop/BAHADIR/Github_Projects/taxidata.csv', index=False)