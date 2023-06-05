from typing import List
import requests


class GenericWrapper:
    target: str
    resource: str
    session: requests.Session

    def __init__(self, name, base_url="https://api.clerk.io/v2"):
        self.target = "{base}/{resource}".format(base=base_url, resource=name)
        self.resource = name

    def get(self, resource_ids: List[str]):
        params = {self.resource: ",".join(resource_ids)}

        resp = self.session.get(self.target, params=params)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def post(self, resource_list):
        raise NotImplemented()

    def patch(self, resource_list):
        raise NotImplemented()

    def delete(self, resource_ids: List[str]):
        raise NotImplemented()
