import pytest

from ..models import Message


@pytest.fixture
def message_factory(db):
    def create_message(
        recipient,
        created_by,
        title="Title",
        text="Some text",
    ):
        return Message.objects.create(
            title=title,
            text=text,
            created_by=created_by,
            recipient=recipient,
        )
    return create_message
