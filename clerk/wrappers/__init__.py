from typing import List, Any, Dict
import requests

from .subscribers import SubscribersWrapper


class InfrastructureException(Exception):
    pass


class GenericWrapper:
    target: str
    resource: str
    session: requests.Session

    output_trackers = []

    def __init__(self, name, base_url="https://api.clerk.io/v2"):
        self.target = "{base}/{resource}".format(base=base_url, resource=name)
        self.resource = name

    def get(self, resource_ids: List[str]):
        params = {self.resource: ",".join(resource_ids)}

        try:
            resp = self.session.get(self.target, params=params)
            if resp.status_code == 200:
                return resp.json()
            else:
                return resp.text
        except requests.RequestException as e:
            raise InfrastructureException(e)

    def post(self, resource_list):
        body = {
            "key": self.session.params["key"],
            "private_key": self.session.params["private_key"],
            self.resource: resource_list,
        }

        headers = {"Content-Type": "application/json"}

        response = self.session.post(self.target, json=body, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    def patch(self, resource_list):
        # Same as POST
        raise NotImplemented()

    def delete(self, resource_ids: List[str]):
        # Same serialisation as GET(Probably), and then provided in body
        raise NotImplemented()
