from pydantic import BaseSettings


class APISettings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    VERSION: str = "0.1.0"
    RELEASE_ID: str = "0.1.0"
    TITLE: str = "t5_base_api"


api_settings = APISettings()
