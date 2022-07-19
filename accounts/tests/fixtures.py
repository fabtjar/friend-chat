import pytest

from ..models import User


@pytest.fixture
def user_factory(db):
    def create_user(
        username,
        password=None,
        first_name="Joe",
        last_name="Blogs",
        email=None,
        is_staff=False,
        is_superuser=False,
        is_active=True,
    ):
        return User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
    return create_user
