"""Generate the packaged canonical METAPAT semantic module catalog fixture."""

# === MODULE_BUILD ===
# id: metapat_catalog_generator
#   module_name: tools.generate_catalog
#   module_kind: instrument
#   summary: generates or verifies the byte-current packaged semantic-module-catalog-v1 fixture from the canonical catalog constructor
#   owner: The Interdependency
#   public_surface: render_catalog, write_catalog, main
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: read, optional generated-file write
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_catalog
#   rollout: CI compliance gate and explicit regeneration command
#   rollback: restore prior generated fixture only with constructor and digest evidence attached
#   requires: metapat_semantic_catalog
#   since: 2026-07-21
#   unresolved: none
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: metapat_catalog_fixture_generated
#   given: the canonical semantic catalog constructor runs
#   then: the rendered fixture is deterministic JSON with one trailing newline
#   class: evidence
#
# id: metapat_catalog_fixture_current
#   given: the generator runs in check mode against the packaged fixture
#   then: stale or missing fixture bytes fail visibly and current bytes pass
#   class: safety
# === END CONTRACTS ===

from __future__ import annotations

import argparse
from pathlib import Path

from metapat.catalog import canonical_semantic_catalog

OUTPUT = Path("src/metapat/fixtures/semantic-module-catalog-v1.json")


def render_catalog() -> str:
    return canonical_semantic_catalog().to_json() + "\n"


def write_catalog(root: Path, output: Path | None = None) -> Path:
    target = root.resolve() / (output or OUTPUT)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_catalog(), encoding="utf-8")
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--out", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    target = root / (args.out or OUTPUT)
    rendered = render_catalog()
    if args.check:
        try:
            existing = target.read_text(encoding="utf-8")
        except OSError:
            print(f"GAP  semantic catalog fixture missing: {target}")
            return 1
        if existing != rendered:
            print(f"GAP  semantic catalog fixture is stale: {target}")
            return 1
        shown = target.relative_to(root) if target.is_relative_to(root) else target
        print(f"CURRENT  {shown}")
        return 0
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(rendered, encoding="utf-8")
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
