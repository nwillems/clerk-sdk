# Clerk.io Python SDK - Example

This is a brief implementation of a clerk.io api wrapper.

```python

import clerk

client = clerk.client(
        "products",
        options.WithHttpAdapter(nullAdapter),
        options.WithPublicKey("SOMETHING PUBLIC KEY GOES HERE"),
        options.WithPrivateKey("PRIVATE KEY HERE")
    )

products_resp = client.get(["ab11", "ba22"])
if products_resp["status"] == "error":
  # Ooops
  return

products = products_resp["products"]
...

```

Highlights:

- API split into "generic resources", which is handled by a single class and Non-resource APIs implemented with "meaningful" method names
- Use of nullable pattern for testing, to avoid over-the-wire requests
- Simple usage, see above
- Uses requests underneath, and doesn't hide it(Maybe a little).

Thoughts from the code
Comment above subscribers wrapper

```
subscribers.py
# This would be similar for a logging-wrapper, search and similar
# Interesting point about the recommendations-wrapper, something about paging(I've heard that That, is a whole topic of discussion in and of itself)
# My stance on pagination in APIs, do it simple, provide a helper function with an elegant interface that will allow it to behave as an iterable
```

**Pagination**, an elegant solution would be something similar to:

```python
client = clerk.client("recommendations", ...)

for product in Paginated(client.complementary, products=["ab11", "ba22"], visitor="Johnie"):
  # Do something with the product

```

**Filtering**, is an obvious rabbit hole, providing a simple builder like interface, would probably
improve user experience. But mostly it would stroke my lust for coding...

```python
import clerk.filters as filters

filters.and(filters.attribute("brand") == "Imperial Inc.", filters.attribute("price") > 100)
```

Just from the example, the readability quickly goes down. What could be done instead, is provide
some guidance on serializing a filter, eg should you just do `urllib.parse.quote_plus(filter)` or ??

Comments from nulled tests

```
test_products_nulled.py
# TODO: Output tracking
# TODO: Test GenericWrapper separately
# TODO: Do something with error handling
```

**Output Tracking** - https://www.jamesshore.com/v2/projects/nullables/testing-without-mocks#output-tracking
Balancing between doing it on the Wrapper or on the adapter. It is a single point to do in the
NullAdapter, however that is also solely on the HTTP level, which for testing purposes is somewhat
askew. However, implementing output tracking separately for all wrapper-types would be a larger
undertaking.

Possible solution, provide a BaseWrapper that handles storing the session, and output-tracking.

**Error Handling** All errors from requests are passed along, these are infrastructure concerns,
and should probably be wrapped somehow, but in the end, the end-user will probably need to figure
out if its a timeout(or rate-limit or ..) or a DNS issue(its always DNS) or ...

The API returns 200 and an error-type. These should probably be wrapped - but not raised. In that
regard, I like the golang way of error-handling, essentially with an either-type.

The difference between the two scenarios is that, applicaiton-wise, the 200-errors are probably
recoverable, eg we can display a user error and tell them something "nice" about it.
Whereas the infrastructure errors, are sort of, get out of the chair and fix this, as-in, not
recoverable from an application point-of-view.
