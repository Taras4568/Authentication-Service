from dependency_injector import containers, providers
from user.data.dal.user import UserDal
from user.data.dal.access_token import AccessTokensDAL
from user.business.user import UserService

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["api.views","api.views.login_view", "api.views.register_view", "api.views.register_view", "api.views.reset_password_view", "api.views.resend_verification_email_view"])

    user_dal = providers.Factory(UserDal)
    access_token_dal = providers.Factory(AccessTokensDAL)

    user_logic = providers.Factory(
        UserService,
        user_dal=user_dal,
        access_tokens_dal=access_token_dal
    )