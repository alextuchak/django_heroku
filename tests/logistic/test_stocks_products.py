import pytest
from django.urls import reverse


# проверка получения 1го курса (retrieve-логика)
@pytest.mark.django_db
def test_get_products(client, product_factory):
    product = product_factory()
    url = reverse('products-detail', args=[product.id])
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == product.id


@pytest.mark.django_db
def test_get_stocks(client, product_factory):
    url_stocks = 'http://localhost:8000/api/v1/stocks/'
    url_products = 'http://localhost:8000/api/v1/products/'
    create_product = client.post(url_products, {
                                                "title": "Помидор",
                                                "description": "Лучшие помидоры на рынке"
                                                },
                                                format='json'
                                )
    response = client.post(url_stocks, {"address": '1',
                                        "positions": [{
                                            "product": 1,
                                            "quantity": 250,
                                            "price": 120.50
                                        }]},
                           format='json')
    assert create_product.status_code == 201
    assert response.status_code == 201
