from pathlib import Path


def required(path: str, old: str, new: str) -> None:
    p = Path(path)
    s = p.read_text(encoding="utf-8")
    if old not in s:
        raise SystemExit(f"missing required text in {path}: {old!r}")
    p.write_text(s.replace(old, new), encoding="utf-8")


def bulk(path: str, pairs: list[tuple[str, str]]) -> None:
    p = Path(path)
    s = p.read_text(encoding="utf-8")
    for old, new in pairs:
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8")


required("tools/generate_catalog.py", "root-spine-envelope-v3", "root-spine-envelope-v4")
required("tools/generate_catalog.py", "semantic-module-catalog-v3", "semantic-module-catalog-v4")
required("tools/generate_application_fixtures.py", "quantum-magnetism-application-v3", "quantum-magnetism-application-v4")
required("tools/generate_application_fixtures.py", "three-phase-electromagnetic-pipe-v3", "three-phase-electromagnetic-pipe-v4")
required("src/metapat/quantum_magnetism.py", "canonical semantic catalog v2", "canonical semantic catalog v4")
required("src/metapat/quantum_magnetism.py", "quantum-magnetism-application-v3", "quantum-magnetism-application-v4")
required("src/metapat/electromagnetic_pipe.py", "deterministic fixture in metapat 0.7.0", "deterministic fixture in metapat 0.8.0")
required("src/metapat/electromagnetic_pipe.py", "canonical semantic catalog v2", "canonical semantic catalog v4")
required("src/metapat/electromagnetic_pipe.py", "three-phase-electromagnetic-pipe-application-v3", "three-phase-electromagnetic-pipe-application-v4")
required("src/metapat/affixiation_harmonics.py", "canonical semantic catalog v2", "canonical semantic catalog v4")
required("src/metapat/affixiation_harmonics.py", "affixiation-harmonics-application-v2", "affixiation-harmonics-application-v3")

bulk("README.md", [
    ("METAPAT is the canonical semantic authority for Meta Energy Theory. It reconstructs Platonic energy from structures and actions exposed across domains without allowing any one domain to own the root.\n\nEvery domain exposes some properties of Platonic energy. No domain exposes all of them.",
     "METAPAT is the canonical semantic authority for Meta Energy Theory. It compares structures and actions independently exposed across domains without allowing any one domain to own the root or transfer its vocabulary by resemblance alone.\n\nDifferent domains may expose common structures and actions. Domain-specific names, mechanisms, evidence standards, and conservation laws remain domain-owned unless the target domain independently licenses them."),
    ("Time is sequential transformation.\nEnergy is vectors altering state through transformation across time.\n```\n\nEnergy is therefore derived rather than primitive at this level.",
     "Time is sequential transformation.\nStructural recurrence does not transfer a domain term.\n```\n\nEnergy is domain-qualified: METAPAT does not call every state transformation energy merely because energetic systems can share the same abstract structure."),
    ("metapat-canon-v3", "metapat-canon-v4"),
    ("root-spine-envelope-v3.json", "root-spine-envelope-v4.json"),
    ("metapat-semantic-catalog-v3", "metapat-semantic-catalog-v4"),
    ("semantic-module-catalog-v3.json", "semantic-module-catalog-v4.json"),
    ("quantum-magnetism-application-v3", "quantum-magnetism-application-v4"),
    ("migrated to v3 identities", "migrated to v4 identities"),
])

bulk("AGENTS.md", [
    ("Preserve exact v3 canon", "Preserve exact v4 canon"),
    ("Canon v3 derives energy from prior structure and action rather than assuming energy-state as primitive. Every domain exposes some properties of Platonic energy; no domain exposes all. Catalog v3 makes the current root, axiom, postulate, theorem, and theory surfaces addressable without transferring domain, measurement, theorem, or UCNS validity.",
     "Canon v4 preserves the structure/action root through time and makes domain qualification explicit: structural resemblance does not transfer a domain term, mechanism, evidence standard, or conservation law. Catalog v4 makes the current root, axiom, postulate, theorem, and theory surfaces addressable without transferring domain, measurement, theorem, or UCNS validity."),
    ("#   energy: Vectors altering state through transformation across time.", "#   energy: Domain-qualified; METAPAT does not call every state transformation energy."),
    ("#   semantic_catalog_v3:", "#   semantic_catalog_v4:"),
    ("metapat-canon-v3", "metapat-canon-v4"),
    ("Tensor is not primitive in v3", "Tensor is not primitive in v4"),
    ("Use exact v3 catalog module IDs", "Use exact v4 catalog module IDs"),
    ("Catalog v3 remains exactly", "Catalog v4 remains exactly"),
    ("migrated to v3 identities", "migrated to v4 identities"),
    ("Time is sequential transformation.\nEnergy is vectors altering state through transformation across time.\n```\n\nEnergy is derived rather than primitive.",
     "Time is sequential transformation.\nStructural recurrence does not transfer a domain term.\n```\n\nEnergy is domain-qualified rather than a universal name for state transformation."),
    ("- Every domain exposes some properties of Platonic energy; no domain exposes all.", "- Different domains may independently expose common structures/actions; resemblance alone transfers no domain-specific name or mechanism."),
    ("Catalog v3 makes current doctrine addressable", "Catalog v4 makes current doctrine addressable"),
])

bulk("COMPLIANCE.md", [
    ("Date: 2026-09-13", "Date: 2026-09-15"),
    ("root-spine-envelope-v3.json", "root-spine-envelope-v4.json"),
    ("semantic-module-catalog-v3.json", "semantic-module-catalog-v4.json"),
    ("packaged v3 application fixtures", "packaged v4 application fixtures"),
    ("version, typing marker, v3 fixtures", "version, typing marker, v4 fixtures"),
    ("metapat-canon-v3", "metapat-canon-v4"),
    ("metapat-semantic-catalog-v3", "metapat-semantic-catalog-v4"),
    ("exact v3 catalog identities", "exact v4 catalog identities"),
    ("Time is sequential transformation.\nEnergy is vectors altering state through transformation across time.\n```\n\nTensor is not primitive before simplex in v3. Scalar is not state. Energy-state is not a root primitive. Energy is derived.",
     "Time is sequential transformation.\nStructural recurrence does not transfer a domain term.\n```\n\nTensor is not primitive before simplex in v4. Scalar is not state. Energy-state is not a root primitive. Energy is domain-qualified rather than a universal name for state transformation."),
    ("Every domain exposes some properties of Platonic energy. No domain exposes all.\n\nA candidate shared structure/action survives only while independent domain comparisons fail to add, split, refine, or falsify it. Similarity alone is insufficient; domain-specific implementation must be removed before transfer is claimed.",
     "Different domains may independently expose common structures and actions. A candidate survives only while independent domain comparisons fail to add, split, refine, or falsify it. Similarity alone is insufficient; domain-specific implementation and vocabulary must be removed before structural transfer is claimed, and domain terms require independent target-domain license."),
])

bulk("docs/application-modules.md", [
    ("quantum-magnetism-application-v3", "quantum-magnetism-application-v4"),
    ("three-phase-electromagnetic-pipe-v3", "three-phase-electromagnetic-pipe-v4"),
    ("current v3 bindings", "current v4 bindings"),
])

bulk("docs/semantic-module-catalog.md", [
    ("# METAPAT semantic module catalog v3", "# METAPAT semantic module catalog v4"),
    ("Catalog v3", "Catalog v4"),
    ("metapat-canon-v3", "metapat-canon-v4"),
    ("semantic-module-catalog-v3.json", "semantic-module-catalog-v4.json"),
    ("Energy\n```\n\nTensor is constructed from related simplexes. Scalar is a state metric. Vector alters state and is inferred by scalar measurement. Energy is derived rather than primitive.",
     "Domain Qualification\n```\n\nTensor is constructed from related simplexes. Scalar is a state metric. Vector alters state and is inferred by scalar measurement. Domain-specific terms, including energy, require independent domain license."),
])

bulk("docs/claims-ledger.md", [
    ("exact importable v3 canon", "exact importable v4 canon"),
    ("`energy_is_derived`", "`domain_term_is_qualified`"),
    ("Vector, state, transformation, and time are all required by the encoded condition.", "A domain term is accepted only when the applicable domain independently licenses it; structural similarity alone is insufficient."),
    ("metapat-canon-v3", "metapat-canon-v4"),
    ("metapat-semantic-catalog-v3", "metapat-semantic-catalog-v4"),
    ("Every domain exposes some properties of Platonic energy. | WORKING-POSTULATE | Does not imply every domain exposes the same properties.", "Different domains may independently expose common structures and actions. | WORKING-POSTULATE | Structural recurrence does not transfer domain-specific names or mechanisms."),
    ("No domain exposes all properties of Platonic energy. | WORKING-POSTULATE | Keeps the search open to later domains.", "A domain term applies only where that domain independently licenses it. | DEFINITION | Similarity alone is insufficient for semantic transfer."),
])

for path in ("tests/test_catalog.py", "tests/test_envelope.py", "tests/test_packaging.py", "tests/test_quantum_magnetism.py", "tests/test_electromagnetic_pipe.py"):
    p = Path(path)
    s = p.read_text(encoding="utf-8")
    for old, new in (
        ("root-spine-envelope-v3.json", "root-spine-envelope-v4.json"),
        ("semantic-module-catalog-v3.json", "semantic-module-catalog-v4.json"),
        ("quantum-magnetism-application-v3.json", "quantum-magnetism-application-v4.json"),
        ("three-phase-electromagnetic-pipe-v3.json", "three-phase-electromagnetic-pipe-v4.json"),
        ("metapat-canon-v3", "metapat-canon-v4"),
        ("metapat-semantic-catalog-v3", "metapat-semantic-catalog-v4"),
        ("quantum-magnetism-application-v3", "quantum-magnetism-application-v4"),
        ("three-phase-electromagnetic-pipe-application-v3", "three-phase-electromagnetic-pipe-application-v4"),
        ('== "0.7.0"', '== "0.8.0"'),
    ):
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8")

for name in (
    "src/metapat/fixtures/root-spine-envelope-v3.json",
    "src/metapat/fixtures/semantic-module-catalog-v3.json",
    "src/metapat/fixtures/quantum-magnetism-application-v3.json",
    "src/metapat/fixtures/three-phase-electromagnetic-pipe-v3.json",
):
    p = Path(name)
    if p.exists():
        p.unlink()
