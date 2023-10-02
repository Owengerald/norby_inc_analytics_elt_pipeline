# Configuration settings
config = {
    "bucket_name": "insert bucket name",
    "folder_name": "insert folder name",
    "database_url": "insert database url",
    "schema": "insert schema",
    "tables": {
        "orders": {
            "file_name": "orders.csv",
            "local_file_name": "orders_data.csv",
            "preprocess_function": "preprocess_orders_data"
        },     
        "reviews": {
            "file_name": "reviews.csv",
            "local_file_name": "reviews_data.csv",
            "preprocess_function": None  
        },
        "shipments_deliveries": {
            "file_name": "shipments_deliveries.csv",
            "local_file_name": "shipments_deliveries_data.csv",
            "preprocess_function": "preprocess_shipments_deliveries_data" 
        }
    }
}

# function to return config variable
def get_config():
    return config
