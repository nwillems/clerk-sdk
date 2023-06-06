import clerk
import clerk.options as options


# TODO: Consider if this should be an "integration test", that would also clean up after itself
def test_products_get():
    # nullAdapter = NullAdapter({"response": "YES"})
    client = clerk.client(
        "products",
        options.WithPublicKey("2EXSs1OJI9aFFdfZK9a4YuYPtKFtsjFJ"),
        options.WithPrivateKey("5HfKYFZoYINv1xjmWB5glh3zxBJPMOX9"),
    )

    product_list = client.get(resource_ids=["aaa", "bbb"])
    print(product_list)

    assert product_list["status"] == "ok"


def test_products_post():
    # nullAdapter = NullAdapter({"response": "YES"})
    client = clerk.client(
        "products",
        options.WithPublicKey("2EXSs1OJI9aFFdfZK9a4YuYPtKFtsjFJ"),
        options.WithPrivateKey("5HfKYFZoYINv1xjmWB5glh3zxBJPMOX9"),
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

    assert response["status"] == "ok"


# TODO: Output tracking
# TODO: Test GenericWrapper separately
# TODO: Actually test with products
# TODO: Do something with error handling
