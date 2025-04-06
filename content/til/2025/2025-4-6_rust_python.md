+++
title = "Writing Python Like It's Rust"
date = 2025-04-06T11:38:22-05:00
draft = false
tags = ['python', 'rust', 'dataclass', 'newtype','Jakub Beránek']
summary = 'Good article from Jakub.'
comments = true
+++

From
https://kobzol.github.io/rust/python/2023/05/20/writing-python-like-its-rust.html

This will not include everything because I don't use all the stuff.


## Dataclasses instead of tuples or dictionaries

Instead of using:

```python
def find_person(...) -> Tuple[str, str, int]:
```

or dictionary:

```python
def find_person(...) -> Dict[str, Any]:
    ...
    return {
        "name": ...,
        "city": ...,
        "age": ...
    }
```

Actually it is easier to describe using a `dataclass`:

```python
@dataclasses.dataclass
class City:
    name: str
    zip_code: int


@dataclasses.dataclass
class Person:
    name: str
    city: City
    age: int


def find_person(...) -> Person:
```

This will make it easier to understand the output of the function.

## Being Able to Use Different Classes in a Function

There are times where a function may accept multiple classes but how do you
support that using type hints.

```python
@dataclass
class Header:
  protocol: Protocol
  size: int

@dataclass
class Payload:
  data: str

@dataclass
class Trailer:
  data: str
  checksum: int

Packet = typing.Union[Header, Payload, Trailer]
# or `Packet = Header | Payload | Trailer` since Python 3.10
```

`Packet` here defines a new type, which can be one of the three classes we
defined.

```python
def handle_is_instance(packet: Packet):
    if isinstance(packet, Header):
        print("header {packet.protocol} {packet.size}")
    elif isinstance(packet, Payload):
        print("payload {packet.data}")
    elif isinstance(packet, Trailer):
        print("trailer {packet.checksum} {packet.data}")
    else:
        assert False

def handle_pattern_matching(packet: Packet):
    match packet:
        case Header(protocol, size): print(f"header {protocol} {size}")
        case Payload(data): print("payload {data}")
        case Trailer(data, checksum): print(f"trailer {checksum} {data}")
        case _: assert False
```

## Using newtypes

In Rust it is common to define data types that do not add any new behavior but
server simply to specify the domain and intended usage of some other, otherwise
quite generate data type -- for example integers.

```python
class Database:
  def get_car_id(self, brand: str) -> int:
  def get_driver_id(self, name: str) -> int:
  def get_ride_info(self, car_id: int, driver_id: int) -> RideInfo:

db = Database()
car_id = db.get_car_id("Mazda")
driver_id = db.get_driver_id("Stig")
info = db.get_ride_info(driver_id, car_id)
```

The error is in `get_ride_info` arguments are swapped.
This won't cause a type error since both are suppose to be integers.

```python
from typing import NewType

# Define a new type called "CarId", which is internally an `int`
CarId = NewType("CarId", int)
# Ditto for "DriverId"
DriverId = NewType("DriverId", int)

class Database:
  def get_car_id(self, brand: str) -> CarId:
  def get_driver_id(self, name: str) -> DriverId:
  def get_ride_info(self, car_id: CarId, driver_id: DriverId) -> RideInfo:


db = Database()
car_id = db.get_car_id("Mazda")
driver_id = db.get_driver_id("Stig")
# Type error here -> DriverId used instead of CarId and vice-versa
info = db.get_ride_info(<error>driver_id</error>, <error>car_id</error>)
```

This is a very simple pattern that can help catch errors that are otherwise
hard to spot.
It is especially useful e.g. if you’re dealing with a lot of different kinds of
IDs (`CarId` vs `DriverId`) or with some metrics (`Speed` vs `Length` vs
`Temperature` etc.) that should not be mixed together.
