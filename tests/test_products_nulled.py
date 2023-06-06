import clerk
import clerk.options as options

import requests


# TODO: Output tracking
# TODO: Test GenericWrapper separately
# TODO: Actually test with products
# TODO: Do something with error handling
def test_products_get():
    nullAdapter = options.NullAdapter(
        {
            "/v2/products": {
                "status_code": 200,
                "json": {"status": "TEST", "products": [{"name": "THIS IS A TEST"}]},
                "elapsed": 0,
            }
        }
    )
    client = clerk.client(
        "products",
        options.WithHttpAdapter(nullAdapter),
        options.WithPublicKey("PUB_KEY"),
        options.WithPrivateKey("PRIV_KEY"),
    )

    product_list = client.get(resource_ids=["aaa", "bbb"])
    print(product_list)

    assert product_list["status"] == "TEST"


def test_products_get_exception():
    nullAdapter = options.NullAdapter(
        {
            "/v2/products": {
                "raise": requests.ConnectionError(),
            }
        }
    )
    client = clerk.client(
        "products",
        options.WithHttpAdapter(nullAdapter),
        options.WithPublicKey("PUB_KEY"),
        options.WithPrivateKey("PRIV_KEY"),
    )

    try:
        product_list = client.get(resource_ids=["aaa", "bbb"])

        assert False  # This should not be reached, test should fail
    except clerk.InfrastructureException:
        assert True


def test_products_post():
    nullAdapter = options.NullAdapter(
        {
            "/v2/products": {
                "status_code": 200,
                "json": {"status": "TEST"},
                "elapsed": 0,
            }
        }
    )

    client = clerk.client(
        "products",
        options.WithHttpAdapter(nullAdapter),
        options.WithPublicKey("PUB_KEY"),
        options.WithPrivateKey("PRIV_KEY"),
    )

    response = client.post(
        resource_list=[
            {
                "id": 135,
                "name": "Green Lightsaber",
                "description": "Antique Rebel Lightsaber",
                "price": 99995.95,
                "image": "https://galactic-empire-merch.com/images/a-r-lightsaber.jpg",
                "url": "https://galactic-empire-merch.com/antique-rebel-lightsaber",
                "brand": "Je’daii",
                "categories": [987, 654],
                "created_at": 1199145600,
            }
        ]
    )
    print(response)

    assert response["status"] == "TEST"
