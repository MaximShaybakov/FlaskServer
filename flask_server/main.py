import os
import time
from gen_variables import app
from data_base.models import Base, engine
import urls


if __name__ == '__main__':
    run_bd = os.system('cd data_base/ && docker-compose up -d')
    time.sleep(5)
    Base.metadata.create_all(engine)
    app.run(host='127.0.0.1', port=5000)
