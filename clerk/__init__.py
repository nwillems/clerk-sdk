from requests import Session

from clerk import wrappers


def setup_session(*options):
    s = Session()

    s.headers["accept"] = "application/json"

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
    else:
        raise NotImplemented()


def client(name: str, *args):
    wrapper = get_wrapper(name)
    session = setup_session(*args)

    wrapper.session = session
    return wrapper
