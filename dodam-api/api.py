from client import Client
from utils import Utils
from apis import (
    auth,
    member,
    nightstudy,
    bus
)

class Api() :
    def __init__(self) :
        self.client = Client()
        self.utils = Utils()

    def login(self, id, pw) -> None:
        """
        도담도담에 로그인하여 액세스, 리프레시 토큰을 저장합니다
        
        :param id: 도담도담 ID
        :param pw: 도담도담 PW
        """
        return auth.login(self.client, self.utils, id, pw)

    def refresh_token(self) :
        """
        저장된 리프레시 토큰을 사용해 액세스 토큰을 재발급합니다
        """
        return auth.reissue(self.client, self.utils)
    
    def get_my_info(self) :
        """
        내 유저 정보를 가져옵니다
        """
        return member.getMy(self.client, self.utils)
    
    def get_my_nightstudy(self):
        """
        내 심자 정보를 가져옵니다
        """
        return nightstudy.getMy(self.client, self.utils)
    
    def get_valid_bus(self):
        """
        유효하는 버스를 가져옵니다
        """
        return bus.getValid(self.client, self.utils)