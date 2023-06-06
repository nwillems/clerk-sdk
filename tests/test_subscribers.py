import clerk
import clerk.options as options


def test_products_get_nulled():
    nullAdapter = options.NullAdapter(
        {
            "/v2/subscribers/subscribe": {
                "status_code": 200,
                "json": {"status": "TEST"},
                "elapsed": 0,
            }
        }
    )
    client = clerk.client(
        "subscribers",
        options.WithHttpAdapter(nullAdapter),
        options.WithPublicKey("PUB_KEY"),
        options.WithPrivateKey("PRIV_KEY"),
    )

    result = client.subscribe(email="john2@nwillems.dk")
    print(result)

    assert result["status"] == "TEST"
