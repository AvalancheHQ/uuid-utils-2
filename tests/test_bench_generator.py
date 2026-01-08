"""CodSpeed benchmarks for UUID generation functions."""
import uuid

import pytest
import uuid_utils


@pytest.fixture
def node():
    return uuid.getnode()


@pytest.mark.benchmark
def test_uuid1_stdlib(node):
    """Benchmark standard library uuid1."""
    for _ in range(10_000):
        uuid.uuid1(node)


@pytest.mark.benchmark
def test_uuid1_utils(node):
    """Benchmark uuid_utils uuid1."""
    for _ in range(10_000):
        uuid_utils.uuid1(node)


@pytest.mark.benchmark
def test_uuid3_stdlib():
    """Benchmark standard library uuid3."""
    for _ in range(10_000):
        uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid3_utils():
    """Benchmark uuid_utils uuid3."""
    for _ in range(10_000):
        uuid_utils.uuid3(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid4_stdlib():
    """Benchmark standard library uuid4."""
    for _ in range(10_000):
        uuid.uuid4()


@pytest.mark.benchmark
def test_uuid4_utils():
    """Benchmark uuid_utils uuid4."""
    for _ in range(10_000):
        uuid_utils.uuid4()


@pytest.mark.benchmark
def test_uuid5_stdlib():
    """Benchmark standard library uuid5."""
    for _ in range(10_000):
        uuid.uuid5(namespace=uuid.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid5_utils():
    """Benchmark uuid_utils uuid5."""
    for _ in range(10_000):
        uuid_utils.uuid5(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid6_utils():
    """Benchmark uuid_utils uuid6."""
    for _ in range(10_000):
        uuid_utils.uuid6()


@pytest.mark.benchmark
def test_uuid7_utils():
    """Benchmark uuid_utils uuid7."""
    for _ in range(10_000):
        uuid_utils.uuid7()
