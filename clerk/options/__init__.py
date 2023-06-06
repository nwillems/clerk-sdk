from collections.abc import Mapping
from typing import Any, Dict

from urllib.parse import urlparse
from requests import Session, Response
from requests.adapters import BaseAdapter
from requests.models import PreparedRequest, Response as Response


class NullResponse(Response):
    def __init__(self, response_data):
        self.response_data = response_data

    def __getattr__(self, __name: str) -> Any:
        if __name not in self.response_data:
            return ""
        return self.response_data[__name]

    def json(self):
        return self.response_data["json"]


class NullAdapter(BaseAdapter):
    responses: Dict[str, Dict]

    def __init__(self, responses):
        super().__init__()

        self.responses = responses

    def send(
        self,
        request: PreparedRequest,
        stream=False,
        timeout=None,
        verify=True,
        cert=None,
        proxies=None,
    ) -> Response:
        if request.url is None:
            raise Exception("None URL not allowed in NullAdapter")

        url_parts = urlparse(request.url)

        if "raise" in self.responses[url_parts.path]:
            raise self.responses[url_parts.path]["raise"]

        return NullResponse(self.responses[url_parts.path])

    def close(self) -> None:
        # Do nothing, especially dont call super, as it is raising "NotImplemented"
        pass


def WithHttpAdapter(adapter):
    def x(session: Session):
        session.mount("http://", adapter)
        session.mount("https://", adapter)

    return x


def WithPublicKey(public_key: str):
    def opt(session: Session):
        session.params["key"] = public_key

    return opt


def WithPrivateKey(private_key: str):
    def opt(session: Session):
        session.params["private_key"] = private_key

    return opt
