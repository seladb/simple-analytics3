import logging
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


@app.route('/')
def serve_requests():
    enrich_geo = EnrichGeoLocation()
    enriched_data = enrich_geo.enrich(request.remote_addr)

    anomaly_rank = AnomalyRanking()
    request_rank = anomaly_rank.rank_request(request)

    db_service = DBService()
    db_service.write_to_db(
        Record(
            geo_location=enriched_data, rank=request_rank, request=request
        )
    )
    return "Hello world"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
