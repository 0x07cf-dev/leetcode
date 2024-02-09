import unittest
from packages.test import (
    test_linkedlist, test_queue, test_stack
)

# There's probably a better way, but...

tests = {
    "LinkedList": test_linkedlist,
    "Queue": test_queue,
    "Stack": test_stack
}

i = 1
for t in tests:
    print(f"\n======================================================================\nTest #{i}: {t}")
    exit = i == len(tests)
    unittest.main(tests[t], exit=exit)
    i += 1
