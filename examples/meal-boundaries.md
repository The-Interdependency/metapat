# What counts as one thing when someone eats?

**Working hypothesis.** The energy systems through which things interact determine which distinctions matter and how much information an account needs to preserve them. A change in those interactions can alter what counts as one thing, which relations it participates in, and where its boundary lies. No partition has permanent priority.

**Proposed invariant.** When two accounts cover the same transformation, it must be possible to trace their shared observations to a compatible causal history. A coarse account can omit steps from view and retain a reference to them. Evidence that cannot distinguish two histories leaves that distinction open.

METAPAT already lets a related whole participate as one thing at another scale (Third Postulate). This example tests what must survive a change of boundary. Consequences already propagate. An interaction can change the material itself, and an account can redraw its boundary around the same event. Those operations answer different questions.

| Question | Participants the account needs | What excretion means here |
| --- | --- | --- |
| What entered and left this person? | Person, meal, waste | Material crossed out of the person. |
| What became of material from this meal? | Gut contents, absorbed material, microbes, residue | Some meal-derived material left along one branch. Other branches had other outcomes. |
| Where did that material go in the local ecology? | Food supply, person, sanitation, receiving soil | Excretion transferred material internally when the system included person and sanitation. Its transfer to soil matters to the receiving system. |

## Replay one synthetic meal

Run `python -m doctest examples/meal-boundaries.md` from the repository root. The identifiers below are stipulated traces of material from one meal. Actual feces can include material from other sources. This example follows one residue branch and retains the identity of a sibling branch where the material separates.

Each record names its inputs and outputs. The person-level account records two crossings. The sanitation account groups the same excretion with treatment. Each account names the record supporting each observation. The shared question is whether the material handed to sanitation can be traced back to this ingestion through the stated transformations.

    >>> records = {
    ...     "ingest": (("meal",), ("gut contents",)),
    ...     "separate": (("gut contents",), ("absorbed fraction", "residue")),
    ...     "microbial change": (("residue",), ("changed residue",)),
    ...     "excrete": (("changed residue",), ("waste portion",)),
    ...     "treat": (("waste portion",), ("soil amendment",)),
    ... }
    >>> person = {"entry": "ingest", "exit": "excrete"}
    >>> sanitation = {"internal handoff": "excrete", "treatment": "treat"}
    >>> def sources(material, history):
    ...     return [event for event, (_, outputs) in history.items() if material in outputs]
    >>> def follows(material, history, expected_steps):
    ...     for expected_event, expected_input in expected_steps:
    ...         if sources(material, history) != [expected_event]:
    ...             return False
    ...         inputs, _ = history[expected_event]
    ...         if inputs != (expected_input,):
    ...             return False
    ...         material = expected_input
    ...     return material == "meal" and not sources(material, history)
    >>> def reconcile(person, sanitation, history):
    ...     handoff = sanitation["internal handoff"]
    ...     if handoff != person["exit"]:
    ...         return False
    ...     steps = (
    ...         (sanitation["treatment"], "waste portion"),
    ...         (handoff, "changed residue"),
    ...         ("microbial change", "residue"),
    ...         ("separate", "gut contents"),
    ...         (person["entry"], "meal"),
    ...     )
    ...     return follows("soil amendment", history, steps)
    >>> reconcile(person, sanitation, records)
    True

Keep both crossings and every event name. Give the excreted portion the absorbed fraction as its source. Both coarse observations still look right. Replay must reject the altered history. Deleting the intervening transformation or identifying treatment as the shared handoff must also fail.

    >>> rerouted = dict(records, excrete=(("absorbed fraction",), ("waste portion",)))
    >>> reconcile(person, sanitation, rerouted)
    False
    >>> reconcile(person, sanitation, {e: r for e, r in records.items() if e != "microbial change"})
    False
    >>> reconcile(person, {**sanitation, "internal handoff": "treat"}, records)
    False

**hmmm** — This fixture supplies the event correspondence. Independently observed accounts may lack common identifiers or enough evidence to connect a particular meal to a particular output. What observation would distinguish two histories that fit both accounts? That is the next evidentiary question. How much detail a given energy-system configuration requires remains open.
