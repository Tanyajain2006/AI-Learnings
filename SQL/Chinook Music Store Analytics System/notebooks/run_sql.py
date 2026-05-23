import pandas as pd
def run_sql(file_path, conn):
    with open(file_path, 'r') as file:
        query = file.read()
    
    print(f"Running query from {file_path}:\n{query}\n")

    return pd.read_sql_query(query, conn)