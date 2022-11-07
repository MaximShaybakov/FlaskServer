from gen_variables import app
from data_base.models import Base, engine
import urls


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(host='127.0.0.1', port=5000)
