from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
import os
from config_tr import get_config_tr

def execute_sql_script_files(database_url, script_directory):
    engine = create_engine(database_url, poolclass=QueuePool)
    try:
        # Establish a connection to the database
        conn = engine.connect()

        # Get a list of SQL script files in the script_directory
        script_files = [f for f in os.listdir(script_directory) if f.endswith('.sql')]

        # Execute each SQL script file
        for script_file in script_files:
            script_path = os.path.join(script_directory, script_file)
            with open(script_path, 'r') as sql_file:
                sql_query = sql_file.read()
                conn.execute(sql_query)

        print("SQL script files executed successfully.")
    except Exception as e:
        print(f"Error executing SQL script files: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    # Get configuration settings from the config module
    config_tr = get_config_tr()

    script_directory = config_tr["script_directory"]

    database_url = config_tr["database_url"]

    # Execute SQL script files
    execute_sql_script_files(database_url, script_directory)
