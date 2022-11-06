from gen_variables import app, bcrypt
from errors import HttpError, error_handler
from data_base.models import Base, Session, User, Ads, engine
from validators import CreateUserShema, CreateAdsShema, PatchUserShema, PatchAdsShema, \
    validate, validate_ads, Type
from views import UserView, AdsView, get_user_id, get_ads_id
from urls import *


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(host='127.0.0.1', port=5000)
