import os 


class BaseConfig:
    KIBANA_HOST = "http://elasticsearch"
    BASE_URL = "192.168.1.197"
    
    # LOGSTASH
    if "LOGSTASH_PORT" in os.environ:
        LOGSTASH_PORT = os.environ["LOGSTASH_PORT"]
    else:
        LOGSTASH_PORT = 5045
    
    # KIBANA
    if "BIBANA_HOST" in os.environ:
        LOGSTASH_HOST = os.environ["KIBANA_HOST"]
    else:
        KIBANA_HOST = None 
    if "KIBANA_PORT" in os.environ:
        KIBANA_PORT = os.environ["KIBANA_PORT"]
    else:
        KIBANA_PORT = 5601
        
    # FLASK_API
    if "API_PORT" in os.environ:
        API_PORT = os.environ["API_PORT"]
    else:
        API_PORT = 5000
    
    # ELASTICSEARCH 
    if "ELASTICSEARCH_PORT" in os.environ:
        ELASTICSEARCH_PORT = os.environ["ELASTICSEARCH_PORT"]
    else:
        ELASTICSEARCH_PORT = 9200


class DevConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


if 'ENV' in os.environ:
    if os.environ['ENV'] == 'dev':
        app_config = DevConfig()
    elif os.environ['ENV'] == 'production':
        app_config = ProductionConfig()
else:
    app_config = DevConfig()
