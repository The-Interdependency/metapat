from __future__ import annotations

from importlib.metadata import version
from importlib.resources import files

import metapat


def test_public_version_matches_distribution_metadata() -> None:
    assert version("metapat") == metapat.__version__


def test_typed_marker_is_packaged() -> None:
    assert files("metapat").joinpath("py.typed").is_file()


def test_base_import_does_not_require_ucns() -> None:
    assert callable(metapat.root_spine_module_envelope)
    envelope = metapat.root_spine_module_envelope()
    assert envelope.module_id == "metapat.root_spine"
    assert envelope.provenance_digest


def test_public_surface_contains_no_local_ucns_object_class() -> None:
    assert "UCNSObject" not in metapat.__all__
    assert not hasattr(metapat, "UCNSObject")
