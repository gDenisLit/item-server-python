from flask import jsonify


class ResponseService:

    @staticmethod
    def success(data=None, status=200):
        response = {
            "status": status,
            "data": data,
            "message": "success"
        }
        return jsonify(response), status

    @staticmethod
    def created(data=None, status=201):
        response = {
            "status": status,
            "data": data,
            "message": "The request has been fulfilled, and a new resource has been created."
        }
        return jsonify(response), status

    @staticmethod
    def server_error(status=500):
        response = {
            "status": status,
            "message": "Internal server error"
        }
        return jsonify(response), status

    @staticmethod
    def bad_request(message="Bad request", status=400):
        response = {
            "status": status,
            "message": message
        }
        return jsonify(response), status
