from app import ItemServer
import sys
sys.dont_write_bytecode = True

if __name__ == "__main__":
    server = ItemServer()
    server.run()
