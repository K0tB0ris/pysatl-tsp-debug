from collections.abc import Iterator
from typing import Any

import cffi
from pysatl_tsp._c.lib import (
    tsp_free_handler,
    tsp_init_handler,
    tsp_next_buffer,
)
from pysatl_tsp.core import Handler
from pysatl_tsp.core.data_providers import SimpleDataProvider

ffi = cffi.FFI()


data = [1.2]
for i in range(1, 20):
    data.append(data[0] + i)
print(data)

provider = SimpleDataProvider(data)
for elem in provider:
    print(elem, end=" ")
print("\n-------------------------------------------\n")


