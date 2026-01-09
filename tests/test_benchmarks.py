import uuid

import pytest
import uuid_utils

node = uuid.getnode()


@pytest.mark.benchmark
def test_uuid1_uuid_utils(benchmark):
    def run():
        for _ in range(10_000):
            uuid_utils.uuid1(node)
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid1_stdlib(benchmark):
    def run():
        for _ in range(10_000):
            uuid.uuid1(node)
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid3_uuid_utils(benchmark):
    def run():
        for _ in range(10_000):
            uuid_utils.uuid3(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid3_stdlib(benchmark):
    def run():
        for _ in range(10_000):
            uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name="python.org")
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid4_uuid_utils(benchmark):
    def run():
        for _ in range(10_000):
            uuid_utils.uuid4()
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid4_stdlib(benchmark):
    def run():
        for _ in range(10_000):
            uuid.uuid4()
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid5_uuid_utils(benchmark):
    def run():
        for _ in range(10_000):
            uuid_utils.uuid5(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid5_stdlib(benchmark):
    def run():
        for _ in range(10_000):
            uuid.uuid5(namespace=uuid.NAMESPACE_DNS, name="python.org")
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid_from_hex_uuid_utils(benchmark):
    def run():
        for _ in range(10_000):
            uuid_utils.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid_from_hex_stdlib(benchmark):
    def run():
        for _ in range(10_000):
            uuid.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid_from_bytes_uuid_utils(benchmark):
    test_bytes = bytes.fromhex("a8098c1af86e11dabd1a00112444be1e")
    
    def run():
        for _ in range(10_000):
            uuid_utils.UUID(bytes=test_bytes)
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid_from_bytes_stdlib(benchmark):
    test_bytes = bytes.fromhex("a8098c1af86e11dabd1a00112444be1e")
    
    def run():
        for _ in range(10_000):
            uuid.UUID(bytes=test_bytes)
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid_from_int_uuid_utils(benchmark):
    test_int = 223963103247899774574613849820102934046
    
    def run():
        for _ in range(10_000):
            uuid_utils.UUID(int=test_int)
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid_from_int_stdlib(benchmark):
    test_int = 223963103247899774574613849820102934046
    
    def run():
        for _ in range(10_000):
            uuid.UUID(int=test_int)
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid_from_fields_uuid_utils(benchmark):
    def run():
        for _ in range(10_000):
            uuid_utils.UUID(fields=(2819197978, 63598, 4570, 189, 26, 73622928926))
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid_from_fields_stdlib(benchmark):
    def run():
        for _ in range(10_000):
            uuid.UUID(fields=(2819197978, 63598, 4570, 189, 26, 73622928926))
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid6_uuid_utils(benchmark):
    def run():
        for _ in range(10_000):
            uuid_utils.uuid6()
    
    benchmark(run)


@pytest.mark.benchmark
def test_uuid7_uuid_utils(benchmark):
    def run():
        for _ in range(10_000):
            uuid_utils.uuid7()
    
    benchmark(run)
