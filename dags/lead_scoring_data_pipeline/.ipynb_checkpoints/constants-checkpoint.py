{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bf398c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# You can create more variables according to your project. The following are the basic variables that have been provided to you\n",
    "DB_PATH = \"/Users/varunssharma/codepro-mlops-assignment/dags/lead_scoring_data_pipeline\"\n",
    "DB_FILE_NAME = \"lead_scoring_data_cleaning.db\"\n",
    "# UNIT_TEST_DB_FILE_NAME =\n",
    "DATA_DIRECTORY = \"/Users/varunssharma/codepro-mlops-assignment/dags/lead_scoring_data_pipeline/data/\"\n",
    "INTERACTION_MAPPING = \"/Users/varunssharma/codepro-mlops-assignment/dags/lead_scoring_data_pipeline/mapping/interaction_mapping.csv\"\n",
    "INDEX_COLUMNS = [\n",
    "    \"created_date\",\n",
    "    \"city_tier\",\n",
    "    \"first_platform_c\",\n",
    "    \"first_utm_medium_c\",\n",
    "    \"first_utm_source_c\",\n",
    "    \"total_leads_droppped\",\n",
    "    \"referred_lead\",\n",
    "    \"app_complete_flag\",\n",
    "]\n",
    "LEADSCORING_CSV_PATH = f\"{DATA_DIRECTORY}leadscoring.csv\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
