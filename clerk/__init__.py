from requests import Session

from clerk import wrappers
from clerk.wrappers import InfrastructureException


# TODO: Consider if we should try and read some configuration from the environment. Probably introduce the useage of Pydantic
def setup_session(*options):
    s = Session()

    s.headers["accept"] = "application/json"
    s.headers["user-agent"] = "NwillemsClerkSDK/0.1"

    for option in options:
        option(s)

    return s


generic_wrapped = [
    "products",
    "categories",
    "orders",
    "pages",
    "customers",
    "customized_search",
    "accessories",
    "merchandising",
    "synonyms",
    "redirects",
]


# TODO: Figure if we should make a NullWrapper
def get_wrapper(name):
    if name in generic_wrapped:
        return wrappers.GenericWrapper(name)
    elif name == "subscribers":
        return wrappers.SubscribersWrapper()
    else:
        raise NotImplemented()


def client(name: str, *args):
    wrapper = get_wrapper(name)
    session = setup_session(*args)

    wrapper.session = session
    return wrapper
