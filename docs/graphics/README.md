# Claims ledger graphics

These editable SVGs are reading aids for the [claims ledger](../claims-ledger.md),
not additional doctrine, evidence, or generated catalog relations. The ledger
statements and their boundaries remain authoritative. No canon text changes are
needed to update the illustrations.

## Usage guidance

Read a graphic with the adjacent ledger table. Open the SVG directly to enlarge
it. Keep the Markdown alt text and adjacent text available when reusing a graphic;
color alone does not encode any status. Each asset has a title and description,
uses text rather than outlined lettering, and has no external fonts, scripts,
images, or rendering-service dependency. The opaque background remains readable
in both light and dark Markdown viewers.

From a document in `docs/`, embed an asset with a relative path:

```markdown
![Claim-status categories; consult the ledger for exact boundaries.](graphics/claims-status-map.svg)
```

| Editable source | Owning source and reading boundary |
|---|---|
| `claims-status-map.svg` | Ledger **Status vocabulary**, **Current canon**, **Application and empirical status**, and **Superseded doctrine**. Cards are categories, not a confidence scale or promotion path. |
| `claims-adversary-standing.svg` | Ledger **Independent adversary standing**, the [preregistration](../adversaries/double-entry-prereg.md), and the [result](../adversaries/double-entry-result.md). Preserve bounded survival, unresolved tests, and the distinction between universal naming and the weaker withdrawn proposition. |
| `claims-evidence-boundaries.svg` | Ledger **Implemented architecture contracts**, [semantic catalog](../semantic-module-catalog.md), [application modules](../application-modules.md), and [compliance authority boundaries](../../COMPLIANCE.md). The only arrows show source/identity dependencies, not the 43 catalog derivation edges, execution order, or proof transfer. |

## Maintenance and verification

Edit the SVG source directly with a text or vector editor. No generator or new
package dependency is required. When an owning statement changes, update its
illustration and Markdown description together. Do not infer extra relations,
convert an unresolved outcome to a pass/failure, or use a contract pass to promote
a domain claim. The graphics do not tally statuses or assign confidence scores.

From the repository root, check XML validity and required accessibility metadata:

```bash
python - <<'PY'
from pathlib import Path
from xml.etree import ElementTree

ns = {'svg': 'http://www.w3.org/2000/svg'}
for path in sorted(Path('docs/graphics').glob('claims-*.svg')):
    root = ElementTree.parse(path).getroot()
    assert root.attrib['role'] == 'img', path
    assert root.find('svg:title', ns).text.strip(), path
    assert root.find('svg:desc', ns).text.strip(), path
    print(f'Valid SVG with title and description: {path}')
PY
```

Open all three files in a browser and inspect the rendered ledger at ordinary
reading width as well as enlarged. Check for clipped text, overlapping labels,
arrow direction, legibility, and complete scope qualifications. XML validity is
not a visual or semantic correctness test. Run the repository checks in
[`AGENTS.md`](../../AGENTS.md#evidence-discipline), including canon byte identity,
after documentation edits. A graphic-only change does not authorize a canon,
fixture, dependency, or generated-metadata rotation.

## hmmm

These hand-maintained summaries can drift when their owning sources change.
There is no automatic semantic-equivalence claim; review the source mapping above
alongside each change. The empirical and adversary uncertainties in the ledger
remain unresolved by illustration.
