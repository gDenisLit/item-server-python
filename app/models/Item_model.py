class Item:
    def __init__(self, _id, name, price, img_url):
        self._id = _id
        self.name = name
        self.price = price
        self.img_url = img_url

    def to_dict(self):
        return {
            "_id": self._id,
            "name": self.name,
            "price": self.price,
            "imgUrl": self.img_url
        }
