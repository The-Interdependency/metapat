# When status crosses a domain boundary

**Standing: proposed clarification of Chapter Zero; canon is unchanged.**

![A commutative square maps state transitions between systems A and B. A bijection preserving the transition carries an invariant and its proof. Structural proofs require preserved hypotheses; empirical findings require an applicability bridge; resemblance leaves target validity unresolved. The current recurrence classifier records proof IDs without verifying their proofs.](domain-status-transfer-card.png)

[Download the vector PDF](domain-status-transfer-card.pdf) ·
[High-resolution PNG](domain-status-transfer-card.png) ·
[Rendering source](render.py)

## Explanation

The card proposes a positive counterpart to Chapter Zero's restriction on transfer
by resemblance alone: a claim can retain its standing under a verified mapping
that preserves what its justification depends on.

The mathematical example is sufficient for one formal case. Let
$T_A:A\to A$ and $T_B:B\to B$ be state transitions, and let $f:A\to B$ be a
bijection satisfying $f\circ T_A=T_B\circ f$ on all of $A$. If
$I_A\circ T_A=I_A$, define $I_B=I_A\circ f^{-1}$. For any $y=f(x)$,

$$
I_B(T_B(y))=I_A(T_A(x))=I_A(x)=I_B(y).
$$

Thus the invariant carries across with its proof. Bijection and transition
preservation are sufficient here; this example does not prescribe the mapping
required by every possible claim. Applying a formal model to a physical system
still requires evidence for that interpretation. Transferred empirical evidence
retains its source dependence and uncertainty; reuse is not independent replication.

## Sources and provenance

The card refers to `The-Interdependency/metapat` at the exact commit
`7480d6d6d42cded74a9d69aeac975e590368c097`:

1. [Chapter Zero, Seventh Theorem](https://github.com/The-Interdependency/metapat/blob/7480d6d6d42cded74a9d69aeac975e590368c097/CHAPTER_ZERO.md#seventh-theorem-domain-terms-do-not-transfer-by-structure-alone).
2. [Structural recurrence, verification and limits](https://github.com/The-Interdependency/metapat/blob/7480d6d6d42cded74a9d69aeac975e590368c097/docs/structural-recurrence.md#verification-and-limits).

The formal example and proposed clarification were derived for this card.
GPT generated; context and prompt: Erin Spencer. Created November 4, 2026.

## Usage guidance

Read the diagram from source transition to mapped transition, then inspect the
equality that must hold. Check the assumptions before reusing the proof. The table
distinguishes mathematical justification, empirical applicability, and resemblance.
Use the PNG for inline display and the vector PDF for printing or publication;
the PDF retains selectable text and clickable source links.

To rebuild from the repository root, use Python 3.11 or newer in an environment
with the optional rendering dependencies:

```bash
python -m pip install -r docs/graphics/domain-status-transfer/requirements.txt
python docs/graphics/domain-status-transfer/render.py --out-dir /tmp/domain-status-transfer
```

The renderer writes the PNG, PDF, previews, and a validation JSON file only to the
selected output directory. The dependencies belong to this optional documentation
tool; METAPAT's runtime dependencies are unchanged. The pinned direct versions
record the authoring environment. PDF creation metadata and embedded provenance
can differ between builds; no byte-identical PDF rebuild is claimed.

The included checks exercise an exact finite conjugacy, its transported invariant,
and a deliberately broken mapping that destroys both the correspondence and the
invariant. They also check text bounds/overlap and text contrast. These finite
checks validate the example; the displayed algebra is the general argument.
Inspect the rebuilt PDF and grayscale preview for layout and legibility.

Publishing this card changes no canon file, semantic catalog, application fixture,
recurrence decision, or transfer flag. To withdraw it, remove this directory and
its entries in the repository and graphics READMEs.

## hmmm

The recurrence classifier retains a supplied proof identifier but does not verify
the proof. Its transfer flags remain false, including for `SAME_STRUCTURE`. A
verified implementation of justified status transfer remains separate work.
