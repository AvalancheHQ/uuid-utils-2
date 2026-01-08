"""CodSpeed benchmarks for UUID parsing functions."""
import uuid

import pytest
import uuid_utils


@pytest.mark.benchmark
def test_from_hex_stdlib():
    """Benchmark standard library UUID from hex."""
    for _ in range(10_000):
        uuid.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")


@pytest.mark.benchmark
def test_from_hex_utils():
    """Benchmark uuid_utils UUID from hex."""
    for _ in range(10_000):
        uuid_utils.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")


@pytest.mark.benchmark
def test_from_bytes_stdlib():
    """Benchmark standard library UUID from bytes."""
    test_bytes = bytes.fromhex("a8098c1af86e11dabd1a00112444be1e")
    for _ in range(10_000):
        uuid.UUID(bytes=test_bytes)


@pytest.mark.benchmark
def test_from_bytes_utils():
    """Benchmark uuid_utils UUID from bytes."""
    test_bytes = bytes.fromhex("a8098c1af86e11dabd1a00112444be1e")
    for _ in range(10_000):
        uuid_utils.UUID(bytes=test_bytes)


@pytest.mark.benchmark
def test_from_int_stdlib():
    """Benchmark standard library UUID from int."""
    test_int = 223367005834136838440840479305942820382
    for _ in range(10_000):
        uuid.UUID(int=test_int)


@pytest.mark.benchmark
def test_from_int_utils():
    """Benchmark uuid_utils UUID from int."""
    test_int = 223367005834136838440840479305942820382
    for _ in range(10_000):
        uuid_utils.UUID(int=test_int)


@pytest.mark.benchmark
def test_from_fields_stdlib():
    """Benchmark standard library UUID from fields."""
    for _ in range(10_000):
        uuid.UUID(fields=(2819197978, 63598, 4570, 189, 26, 73622928926))


@pytest.mark.benchmark
def test_from_fields_utils():
    """Benchmark uuid_utils UUID from fields."""
    for _ in range(10_000):
        uuid_utils.UUID(fields=(2819197978, 63598, 4570, 189, 26, 73622928926))
