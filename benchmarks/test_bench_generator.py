import uuid

import uuid_utils
from pytest_codspeed import benchmark

node = uuid.getnode()


def test_uuid_uuid1(benchmark):
    def _uuid_uuid1():
        uuid.uuid1(node)

    benchmark(_uuid_uuid1)


def test_uuid_utils_uuid1(benchmark):
    def _uuid_utils_uuid1():
        uuid_utils.uuid1(node)

    benchmark(_uuid_utils_uuid1)


def test_uuid_uuid3(benchmark):
    def _uuid_uuid3():
        uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name="python.org")

    benchmark(_uuid_uuid3)


def test_uuid_utils_uuid3(benchmark):
    def _uuid_utils_uuid3():
        uuid_utils.uuid3(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")

    benchmark(_uuid_utils_uuid3)


def test_uuid_uuid4(benchmark):
    def _uuid_uuid4():
        uuid.uuid4()

    benchmark(_uuid_uuid4)


def test_uuid_utils_uuid4(benchmark):
    def _uuid_utils_uuid4():
        uuid_utils.uuid4()

    benchmark(_uuid_utils_uuid4)


def test_uuid_uuid5(benchmark):
    def _uuid_uuid5():
        uuid.uuid5(namespace=uuid.NAMESPACE_DNS, name="python.org")

    benchmark(_uuid_uuid5)


def test_uuid_utils_uuid5(benchmark):
    def _uuid_utils_uuid5():
        uuid_utils.uuid5(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")

    benchmark(_uuid_utils_uuid5)
