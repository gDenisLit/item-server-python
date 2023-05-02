class ItemDTO:
    def __init__(self, name, price, img_url):
        self.name = name
        self.price = price
        self.img_url = img_url

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "imgUrl": self.img_url
        }
