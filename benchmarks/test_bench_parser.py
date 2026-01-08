import uuid

import uuid_utils
from pytest_codspeed import benchmark


def test_uuid_from_hex(benchmark):
    def _uuid_from_hex():
        uuid.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")

    benchmark(_uuid_from_hex)


def test_uuid_utils_from_hex(benchmark):
    def _uuid_utils_from_hex():
        uuid_utils.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")

    benchmark(_uuid_utils_from_hex)


def test_uuid_from_bytes(benchmark):
    def _uuid_from_bytes():
        uuid.UUID(bytes=b"\xa8\t\x8c\x1a\xf8n\x11\xda\xbd\x1a\x00\x11$D\xbe\x1e")

    benchmark(_uuid_from_bytes)


def test_uuid_utils_from_bytes(benchmark):
    def _uuid_utils_from_bytes():
        uuid_utils.UUID(bytes=b"\xa8\t\x8c\x1a\xf8n\x11\xda\xbd\x1a\x00\x11$D\xbe\x1e")

    benchmark(_uuid_utils_from_bytes)


def test_uuid_from_int(benchmark):
    def _uuid_from_int():
        uuid.UUID(int=223359981843454034376424264993384135198)

    benchmark(_uuid_from_int)


def test_uuid_utils_from_int(benchmark):
    def _uuid_utils_from_int():
        uuid_utils.UUID(int=223359981843454034376424264993384135198)

    benchmark(_uuid_utils_from_int)


def test_uuid_from_fields(benchmark):
    def _uuid_from_fields():
        uuid.UUID(fields=(2819197978, 63598, 4570, 189, 26, 73622928926))

    benchmark(_uuid_from_fields)


def test_uuid_utils_from_fields(benchmark):
    def _uuid_utils_from_fields():
        uuid_utils.UUID(fields=(2819197978, 63598, 4570, 189, 26, 73622928926))

    benchmark(_uuid_utils_from_fields)
