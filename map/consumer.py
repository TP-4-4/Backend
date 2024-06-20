import queue
import tempfile

import requests
from kafka import KafkaConsumer

url = "https://storage.yandexcloud.net/cloud-certs/CA.pem"
response = requests.get(url)
if response.status_code == 200:
    cert_data = response.content.decode('utf-8')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".crt") as temp_cert_file:
        temp_cert_file.write(cert_data.encode('utf-8'))
        temp_cert_path = temp_cert_file.name
else:
    print("Ошибка при загрузке файла:", response.status_code)

coord_queue = queue.Queue()


def get_coord_from_kafka():
    consumer = KafkaConsumer(
        'coordinates',
        bootstrap_servers=['rc1a-1v00ge0ve2fc0v3l.mdb.yandexcloud.net:9091','rc1a-2v4ibf0ob81q9ia8.mdb.yandexcloud.net:9091','rc1a-qkq6q3nadesff69e.mdb.yandexcloud.net:9091','rc1b-899943l1rfaf2ghc.mdb.yandexcloud.net:9091','rc1b-brqnu1mp5aiduuaq.mdb.yandexcloud.net:9091','rc1b-ubqhqs0m5rpjisuu.mdb.yandexcloud.net:9091','rc1d-j0ohei4htscbku4d.mdb.yandexcloud.net:9091','rc1d-tfupvefodh1d8p2d.mdb.yandexcloud.net:9091','rc1d-uqekgkq34ju68r89.mdb.yandexcloud.net:9091'],
        security_protocol="SASL_SSL",
        sasl_mechanism="SCRAM-SHA-512",
        sasl_plain_username='read',
        sasl_plain_password='12345678',
        ssl_cafile=temp_cert_path)
    print("ready")
    # coord_queue.put(None)
    for msg in consumer:
        data = [data for data in msg.value.decode("utf-8").split(' ', maxsplit=1)]
        coord_queue.put(data)
