from flask import jsonify, make_response


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
    def login_success(token: str, data=None, status=200):
        response = make_response(jsonify({
            "message": "Login successfull",
            "status": status,
            "data": data
        }))
        response.set_cookie(
            "loginToken",
            value=token,
            httponly=True
        )
        return response, status

    @staticmethod
    def logout_success(status=200):
        response = make_response(jsonify({
            "message": "Logged out succesfully",
            "status": status
        }))
        response.delete_cookie("loginToken")
        return response, 200

    @staticmethod
    def bad_request(message="Bad request", status=400):
        response = {
            "status": status,
            "message": message
        }
        return jsonify(response), status

    @staticmethod
    def unauthorized(message="Unauthorized", status=401):
        response = {
            "status": status,
            "message": message
        }
        return jsonify(response), status

    @staticmethod
    def server_error(status=500):
        response = {
            "status": status,
            "message": "Internal server error"
        }
        return jsonify(response), status
