import pandas as pd

# Read and process the CSV file
df = pd.read_csv('taxidata.csv')
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

# Define a function to convert pandas data types to SQL data types
def pandas_dtype_to_sql(dtype):
    if dtype == 'int64':
        return 'INTEGER'
    elif dtype == 'float64':
        return 'FLOAT'
    elif dtype == 'datetime64[ns]':
        return 'TIMESTAMP'
    elif dtype == 'object':
        return 'TEXT'
    else:
        return 'TEXT'

# Generate the SQL schema
schema = 'CREATE TABLE taxidata (\n'
for column, dtype in df.dtypes.items():
    schema += f'  {column} {pandas_dtype_to_sql(dtype)},\n'
schema = schema.rstrip(',\n') + '\n);\n'

# Generate the COPY statement
copy_statement = "COPY taxidata FROM '/tmp/taxidata.csv' DELIMITER ',' CSV HEADER;\n"

# Combine the schema and COPY statement and write to init.sql
with open('init.sql', 'w') as f:
    f.write(schema + copy_statement)

# Print the generated SQL
print(schema + copy_statement)