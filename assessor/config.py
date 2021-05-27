#
# This loads the configuration
#
# This is configuration for the assessor 

import os
import yaml

default_file = os.path.join(os.path.dirname(__file__), "defaults.yml")
local_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "machine.cfg"))
user_file = '_assessor.yml'

config = {}

if os.path.exists(default_file):
    with open(default_file) as file:
        config.update(yaml.load(file, Loader=yaml.FullLoader))

if os.path.exists(local_file):
    with open(local_file) as file:
        config.update(yaml.load(file, Loader=yaml.FullLoader))

if os.path.exists(user_file):
    with open(user_file) as file:
        config.update(yaml.load(file, Loader=yaml.FullLoader))

if config=={}:
    raise ValueError(
        "No configuration file found at either "
        + user_file
        + " or "
        + local_file
        + " or "
        + default_file
        + "."
    )

        
short_name = config['assessment_short_name']
long_name = config['assessment_long_name']
year = config['assessment_year']
data_directory = os.path.expandvars(config['data_directory'])

instructor_email = config['instructor_email']
instructor_name = config['instructor_name']
assessor_group_email = config['assessor_group_email']

participant_key = config['participant_list_key']
participant_sheet = config['participant_list_sheet']
marksheets_filename = config['class_marksheets_pickle']

