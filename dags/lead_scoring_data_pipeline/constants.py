# You can create more variables according to your project.
# The following are the basic variables that have been provided to you
PIPELINE_PATH = "/home/dags/lead_scoring_data_pipeline"
DB_PATH = PIPELINE_PATH
DB_FILE_NAME = "/lead_scoring_data_cleaning.db"
# UNIT_TEST_DB_FILE_NAME =
DATA_DIRECTORY = f"{PIPELINE_PATH}/data"
INTERACTION_MAPPING = f"{PIPELINE_PATH}/mapping/interaction_mapping.csv"
INDEX_COLUMNS = [
    "created_date",
    "city_tier",
    "first_platform_c",
    "first_utm_medium_c",
    "first_utm_source_c",
    "total_leads_droppped",
    "referred_lead",
    "app_complete_flag",
]
LEADSCORING_CSV_PATH = f"{DATA_DIRECTORY}/leadscoring.csv"
