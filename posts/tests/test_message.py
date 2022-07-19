import pytest

from django.urls import reverse

from accounts.tests.fixtures import user_factory

from .fixtures import message_factory


@pytest.fixture
def message_1(user_factory, message_factory):
    user_a = user_factory("user_a")
    user_b = user_factory("user_b")
    message = message_factory(
        created_by=user_a,
        recipient=user_b,
    )
    return message


def test_message_details(message_1, client):
    response = client.get(reverse("message_details", kwargs={"message_id": message_1.id}))
    assert response.status_code == 200
