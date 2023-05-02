class Item:
    def __init__(self, _id: str, name: str, price: str, imgUrl: str):
        self._id = _id
        self.name = name
        self.price = price
        self.img_url = imgUrl

    def to_dict(self):
        return {
            "_id": str(self._id),
            "name": self.name,
            "price": self.price,
            "imgUrl": self.img_url
        }

    @staticmethod
    def item_dto(name: str, price: str, imgUrl: str):
        return {
            "name": name,
            "price": price,
            "imgUrl": imgUrl
        }