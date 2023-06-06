from typing import List, Any, Dict
import requests


# This would be similar for a logging-wrapper, search and similar
# Interesting point about the recommendations-wrapper, something about paging(I've heard that That, is a whole topic of discussion in and of itself)
# My stance on pagination in APIs, do it simple, provide a helper function with an elegant interface that will allow it to behave as an iterable
class SubscribersWrapper:
    target: str
    resource: str
    session: requests.Session

    def __init__(self, name="subscribers", base_url="https://api.clerk.io/v2"):
        self.target = "{base}/{resource}".format(base=base_url, resource=name)
        self.resource = name

    def subscribe(
        self,
        email: str,
        list_id: Any = None,
        redirect: bool = False,
        redirect_url: str = "",
    ):
        """
        Remember to ensure that email and redirect_url are escaped properly
        """
        # Not exactly sure what the redirect option would do in this case, but we should stop requests from doing anything about it
        params: Dict[str, Any] = {
            "email": email,
        }

        if list_id is not None:
            params["list_id"] = list_id

        if redirect:
            params["redirect"] = True
            params["redirect_url"] = redirect_url

        target_url = "{base_target}/subscribe".format(base_target=self.target)
        response = self.session.get(target_url, params=params, allow_redirects=False)

        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    def unsubscribe(
        self,
        email: str,
        list_id: Any = None,
        redirect: bool = False,
        redirect_url: str = "",
    ):
        """
        Remember to ensure that email and redirect_url are escaped properly
        """
        # Not exactly sure what the redirect option would do in this case, but we should stop requests from doing anything about it
        params: Dict[str, Any] = {
            "email": email,
        }

        if list_id is not None:
            params["list_id"] = list_id

        if redirect:
            params["redirect"] = True
            params["redirect_url"] = redirect_url

        target_url = "{base_target}/unsubscribe".format(base_target=self.target)
        response = self.session.get(target_url, params=params, allow_redirects=False)

        if response.status_code == 200:
            return response.json()
        else:
            return response.text
