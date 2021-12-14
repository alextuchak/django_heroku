import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def product_factory():
    def factory(**kwargs):
        return baker.make('Product', **kwargs)

    return factory
