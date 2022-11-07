from gen_variables import app
from views import UserView, AdsView

app.add_url_rule('/user/<int:user_id>/', view_func=UserView.as_view('users_get'), methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/register/', view_func=UserView.as_view('users'), methods=['POST'])
app.add_url_rule('/ads/<int:ads_id>/', view_func=AdsView.as_view('ads_get'), methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/ads/', view_func=AdsView.as_view('ads'), methods=['POST'])
