# Configuration settings
config2 = {
    "database_url": "insert database url",
    "schema": "insert schema",  
    "bucket_name": "insert bucket name",
    "folder_name": "insert folder name",
    "group_id": "insert id",  
    "tables": {
        "agg_public_holiday": {
            "file_name": "agg_public_holiday.csv",
        },
        "agg_shipments": {
            "file_name": "agg_shipments.csv",
        },
        "best_performing_product": {
            "file_name": "best_performing_product.csv",
        },
        
    }
}

# defining function to access config dictionary
def get_config2():
    return config2
