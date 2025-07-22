from typing import Optional, List
from datetime import datetime
from user.data.models.models import TokenBlocklist  # або твій шлях до моделі
from user.data.dto.jwt import JwtDTO  # припускаємо, що твій DTO реалізований для Django

class AccessTokensDAL:
    def save_access_token(self, jwt_dto: JwtDTO) -> Optional[int]:
        jwt_entry = None

        if jwt_dto.id:
            try:
                jwt_entry = TokenBlocklist.objects.get(id=jwt_dto.id)
            except TokenBlocklist.DoesNotExist:
                jwt_entry = None

        if jwt_entry:
            jwt_entry.user_id = jwt_dto.user_id
            jwt_entry.jti = jwt_dto.jti
            jwt_entry.token_type = jwt_dto.token_type
            jwt_entry.token = jwt_dto.token
            jwt_entry.revoked = jwt_dto.revoked
            jwt_entry.expires_at = jwt_dto.expires_at
            jwt_entry.updated_at = datetime.utcnow()
        else:
            jwt_entry = TokenBlocklist(
                user_id=jwt_dto.user_id,
                jti=jwt_dto.jti,
                token_type=jwt_dto.token_type,
                token=jwt_dto.token,
                revoked=jwt_dto.revoked,
                expires_at=jwt_dto.expires_at,
                updated_at=datetime.utcnow()
            )

        jwt_entry.save()
        return jwt_entry.id

    def save_access_tokens(self, jwt_dto_list: List[JwtDTO]):
        for jwt in jwt_dto_list:
            self.save_access_token(jwt)

    def get_access_token_by_id(self, jwt_id: int) -> Optional[TokenBlocklist]:
        return TokenBlocklist.objects.filter(id=jwt_id).first()

    def get_access_token_by_jti(self, jti: str) -> Optional[TokenBlocklist]:
        return TokenBlocklist.objects.filter(jti=jti).first()
