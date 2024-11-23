from elasticsearch import Elasticsearch
from datetime import datetime, timedelta

from configs.elk_config import app_config


es = Elasticsearch([f"{app_config.KIBANA_HOST}:{app_config.ELASTICSEARCH_PORT}"])
retention_times = 60
cutoff_date = datetime.now() - timedelta(days=retention_times)
print(cutoff_date)
indices = es.cat.indices(index="logs-*", format="json")
for index in indices:
    index_date = datetime.strptime(index["index"].split("-")[-1], "%Y.%m.%d")
    if index_date < cutoff_date:
        es.indices.delete(index=index["index"])
