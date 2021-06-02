import logging
# https://docs.python.org/3/library/queue.html
import threading
import queue
import uuid
from flask import Flask, request
from flask.logging import default_handler
from services.enrich_geo_location import EnrichGeoLocation
from services.request_anomaly_ranking import AnomalyRanking
from services.db_service import DBService
from common.record import Record

app = Flask(__name__)

root = logging.getLogger()
root.setLevel(logging.INFO)
root.addHandler(default_handler)

job_queue = queue.Queue()


def worker():
    while True:
        job_id, ip_addr, headers = job_queue.get()
        logging.info(f"Working on {job_id}")
        enrich_geo = EnrichGeoLocation()
        enriched_data = enrich_geo.enrich(ip_addr)

        anomaly_rank = AnomalyRanking()
        request_rank = anomaly_rank.rank_request(headers)

        db_service = DBService()
        db_service.write_to_db(
            Record(
                geo_location=enriched_data, rank=request_rank
            )
        )
        logging.info(f"Finished {job_id}")
        job_queue.task_done()


# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()


@app.route('/')
def serve_requests():
    job_queue.put((uuid.uuid4(), request.remote_addr, request.headers))
    return "Hello world"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
