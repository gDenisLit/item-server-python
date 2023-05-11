class User:
    def __init__(self, _id: str, username: str, password: str, fullname: str, imgUrl: str, isAdmin: bool = False):
        self._id = _id
        self.username = username
        self.password = password
        self.fullname = fullname
        self.img_url = imgUrl
        self.is_admin = isAdmin

    def to_dict(self):
        return {
            "_id": str(self._id),
            "username": self.username,
            "fullname": self.fullname,
            "imgUrl": self.img_url
        }

    @staticmethod
    def login_credentials(username: str, password: str):
        return {
            "username": username,
            "password": password
        }

    @staticmethod
    def signup_credentials(username: str, password: str, fullname: str, imgUrl: str):
        return {
            "username": username,
            "password": password,
            "fullname": fullname,
            "imgUrl": imgUrl,
            "isAdmin": False
        }
