from __future__ import annotations

import base64
import unittest
from pathlib import Path

from tools.generate_application_fixtures import render_electromagnetic_pipe_fixture
from tools.generate_msdmd import render_collection


def _emit(label: str, content: str) -> None:
    encoded = base64.b64encode(content.encode("utf-8")).decode("ascii")
    print(f"{label}_BEGIN")
    for index in range(0, len(encoded), 120):
        print(encoded[index : index + 120])
    print(f"{label}_END")


class TestReleaseMaterialization(unittest.TestCase):
    def test_emit_release_artifacts(self) -> None:
        root = Path(__file__).resolve().parents[1]
        _emit("PIPE_FIXTURE", render_electromagnetic_pipe_fixture())
        _emit("MSDMD", render_collection(root))
        self.fail("release artifacts emitted")


if __name__ == "__main__":
    unittest.main()
