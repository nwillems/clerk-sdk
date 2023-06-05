import clerk
import clerk.options as options


# TODO: Consider if this should be an "integration test", that would also clean up aftewr itself
def test_products_get():
    # nullAdapter = NullAdapter({"response": "YES"})
    client = clerk.client(
        "products",
        options.WithPublicKey("2EXSs1OJI9aFFdfZK9a4YuYPtKFtsjFJ"),
        options.WithPrivateKey("5HfKYFZoYINv1xjmWB5glh3zxBJPMOX9"),
    )

    product_list = client.get(resource_ids=["aaa", "bbb"])
    print(product_list)

    assert True == False


# TODO: Output tracking
# TODO: Test GenericWrapper separately
# TODO: Actually test with products
# TODO: Do something with error handling
def test_products_get_nulled():
    nullAdapter = options.NullAdapter(
        {
            "/v2/products": {
                "status_code": 200,
                "json": {"status": "ok", "products": []},
                "elapsed": 0,
            }
        }
    )
    client = clerk.client(
        "products",
        options.WithHttpAdapter(nullAdapter),
        options.WithPublicKey("2EXSs1OJI9aFFdfZK9a4YuYPtKFtsjFJ"),
        options.WithPrivateKey("5HfKYFZoYINv1xjmWB5glh3zxBJPMOX9"),
    )

    product_list = client.get(resource_ids=["aaa", "bbb"])
    print(product_list)

    assert True == False
