from data_base.models import User, Ads, Session
from errors import HttpError
from flask.views import MethodView
from validators import Type, validate, validate_ads, CreateAdsShema, CreateUserShema, \
    PatchAdsShema, PatchUserShema
from sqlalchemy.exc import IntegrityError
from flask import jsonify, request


def get_user_id(user_id: int, orm_model: Type[User], session: Session):
    with Session() as session:
        orm_item = session.query(orm_model).get(user_id)
        if orm_item is None:
            raise HttpError(404, 'item not found')
        return orm_item


class UserView(MethodView):

    def get(self, user_id: int):
        with Session() as session:
            user = get_user_id(user_id, User, session)
            return jsonify(user_id=user.id,
                           user_name=user.name)

    def post(self):
        json_data = request.json
        with Session() as session:
            try:
                new_user = User(**validate(json_data, CreateUserShema))
                session.add(new_user)
                session.commit()
            except IntegrityError:
                raise HttpError(409, 'this name alredy exists')
            return jsonify(status='OK', id=new_user.id)

    def patch(self, user_id):
        data_to_patch = validate(request.json, PatchUserShema)
        with Session() as session:
            user = get_user_id(user_id, User, session)
            for fields, value in data_to_patch.items():
                setattr(user, fields, value)
            session.commit()
            return jsonify(user=user.id, status='success')

    def delete(self, user_id: int):
        with Session() as session:
            user = get_user_id(user_id, User, session)
            session.delete(user)
            session.commit()
            return jsonify(status='OK', user=f'{user.name} - delete')


def get_ads_id(ads_id: int, orm_model: Type[Ads], session: Session):
    with Session() as session:
        orm_item = session.query(orm_model).get(ads_id)
        if orm_item is None:
            raise HttpError(404, 'item not found')
        return orm_item


class AdsView(MethodView):

    def get(self, ads_id: int):
        with Session() as session:
            ads = get_ads_id(ads_id, Ads, session)
            return jsonify(ads_id=ads.id,
                           ads_title=ads.title,
                           creation_time=ads.creation_time.isoformat())

    def post(self):
        json_data = request.json
        with Session() as session:
            try:
                new_ads = Ads(**validate(json_data, CreateAdsShema))
                session.add(new_ads)
                session.commit()
            except IntegrityError:
                raise HttpError(409, 'this advertisement already exists')
            return jsonify(status='OK', ads_id=new_ads.id)

    def patch(self, ads_id):
        data_to_patch = validate(request.json, PatchAdsShema)
        with Session() as session:
            ads = get_ads_id(ads_id, Ads, session)
            for fields, value in data_to_patch.items():
                setattr(ads, fields, value)
            session.commit()
            return jsonify(title=ads.title, status='success')

    def delete(self, ads_id: int):
        with Session() as session:
            ads = get_user_id(ads_id, Ads, session)
            session.delete(ads)
            session.commit()
            return jsonify(status='OK', ads=f'{ads.title} - delete')
