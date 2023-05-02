class ItemService:

    @staticmethod
    async def query():
        return "items..."

    @staticmethod
    async def get_by_id(id):
        return f"item: {id}"

    @staticmethod
    async def remove_item(id):
        return id

    @staticmethod
    async def add_item(item):
        print(f"adding item: {item}")
        return item

    @staticmethod
    async def update_item(item):
        print(f"adding item: {item}")
        return item
