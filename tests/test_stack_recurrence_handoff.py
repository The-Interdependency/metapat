"""Usage: pytest this file; set STACK_SOURCE_ROOT to replay the exact producer."""

# === CHECKS ===
# id: check_stack_recurrence_handoff
#   proves: recurrence_unresolved_fails_closed, recurrence_no_semantic_transfer, recurrence_catalog_bound
#   call: self::test_stack_handoff_preserves_identity_without_granting_recurrence
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

from metapat.catalog import CATALOG_VERSION, canonical_semantic_catalog
from metapat.structural_recurrence import RecurrenceEvidence, adjudicate_recurrence


def test_stack_handoff_preserves_identity_without_granting_recurrence():
    root = Path(__file__).resolve().parents[1]
    fixture = json.loads((root / "tests/fixtures/stack-system-set-trajectories.json").read_text())
    graph = json.loads((root / "docs/work-graphs/system-set-recurrence-v0.json").read_text())
    assert graph["work_graph_sha256"] == sha256(json.dumps(
        {key: graph[key] for key in ("repositories", "boundaries")},
        sort_keys=True, separators=(",", ":"),
    ).encode()).hexdigest()
    producer = fixture["producer"]
    participant = next(row for row in graph["repositories"] if row["repository"] == producer["repository"])
    assert participant["commit"] == producer["commit"]
    consumer = next(row for row in graph["repositories"] if row["repository"] == "The-Interdependency/metapat")
    consumer_module = "src/metapat/structural_recurrence.py"
    pinned_consumer = subprocess.check_output(
        ["git", "show", f"{consumer['commit']}:{consumer_module}"], cwd=root,
    )
    assert pinned_consumer == (root / consumer_module).read_bytes(), "recurrence work graph source drift"
    assert graph["boundaries"]["authority_transfer"] is False
    assert graph["boundaries"]["proof_status_transfer"] is False
    assert graph["boundaries"]["measurement_status_transfer"] is False

    payloads = fixture["outputs"]
    for payload in payloads:
        assert payload["schema"] == "english-gonol.system-set-trajectory"
        assert payload["version"] == "0.1.0"
        receipt_body = {key: value for key, value in payload.items() if key != "structure_id"}
        assert payload["structure_id"] == sha256(json.dumps(
            receipt_body, sort_keys=True, ensure_ascii=False, separators=(",", ":"),
            allow_nan=False,
        ).encode()).hexdigest()
        assert {"equivalence", "analogy", "recurrence", "proof_status", "measurement"}.isdisjoint(payload)

    if "STACK_SOURCE_ROOT" in os.environ:
        source_root = Path(os.environ["STACK_SOURCE_ROOT"]).resolve()
        assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source_root, text=True).strip() == producer["commit"]
        assert sha256((source_root / producer["module_path"]).read_bytes()).hexdigest() == producer["module_sha256"]
        script = """
import json, sys
from english_gonol.system_set_trajectory import SemanticStep, SystemSetTrajectory
outputs = []
for record in json.load(sys.stdin):
    record['steps'] = [SemanticStep(**step) for step in record['steps']]
    outputs.append(SystemSetTrajectory(**record).to_ucns_comparison_input())
print(json.dumps(outputs))
"""
        result = subprocess.run(
            [sys.executable, "-c", script], input=json.dumps(fixture["inputs"]),
            text=True, capture_output=True, check=True, cwd=root,
            env={**os.environ, "PYTHONPATH": str(source_root / "research/english-gonol")},
        )
        assert json.loads(result.stdout) == payloads

    source, target = payloads
    catalog = canonical_semantic_catalog()
    evidence = RecurrenceEvidence(
        source_domain="fixture:domain-a", target_domain="fixture:domain-b",
        source_origin_id=source["origin_id"], target_origin_id=target["origin_id"],
        source_path_id=source["path_id"], target_path_id=target["path_id"],
        declared_invariants=("fixture:ordered-relation",), preserved_invariants=(),
        mapping_complete=None, replay_passed=None, ancestry_resolved=False,
        unresolved=tuple(source["unresolved"] + target["unresolved"]),
        catalog_version=CATALOG_VERSION, catalog_digest=catalog.catalog_digest,
        catalog_module_ids=(
            "metapat.axiom.12.domain_qualification",
            "metapat.postulate.1.partial_domains",
            "metapat.postulate.6.cross_domain_falsification",
            "metapat.theory.11.cross_domain_reconstruction",
        ),
    )
    decision = adjudicate_recurrence(evidence)
    assert decision.outcome == "HMMM"
    assert decision.independent is None
    assert decision.equivalence_proof_id is None
    assert decision.unresolved == evidence.unresolved
    assert decision.source_origin_id == source["origin_id"]
    assert decision.target_path_id == target["path_id"]
    assert decision.semantic_transfer is False
    assert decision.proof_status_transfer is False
    assert decision.measurement_status_transfer is False
