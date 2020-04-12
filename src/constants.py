import os
import toml

config_path = os.path.join(os.path.dirname(__file__), '..', 'config.toml')
config = toml.load(config_path)

AEROSPIKE_CONFIG = config['aerospike']
EMAIL_CONFIG = config['email']
PROFILES = config['instagram']['profiles']
RECIPIENTS = config['sending']['recipients']

