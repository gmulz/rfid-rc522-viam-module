import asyncio
from viam.module.module import Module
try:
    from models.rfid_rc522 import RfidRc522
except ModuleNotFoundError:
    # when running as local module with run.sh
    from .models.rfid_rc522 import RfidRc522


if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
