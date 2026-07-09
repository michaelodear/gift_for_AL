# ACT 3 — "A SUCCULENT CHINESE MEAL"
*The courtroom. Draft 6.*

**Legend** — [PAGE] fade-to-black narration (`narration.html`, "you" = defendant) · [CLIP] objection.lol chain (Phoenix/Edgeworth/Judge only) built by `generate_clips.py` · [PANEL] interactive component · `[FRIEND]` = the friend's name (via `--name`).

Because the clips are generated programmatically, the old A/B/C are merged into fewer, longer chains.

---

## SCENE 1 — TOKYO  *(narration.html — already built)*
Arrival → arrest (Airport bg) → the trap → holding cell, Phoenix walks in (Detention bg, sprite). Ends → Proceed to courtroom.

---

## SCENE 2 — THE COURTROOM

### [CLIP 1] — Opening → the charge  *(Judge · Edgeworth · Phoenix)*

> **JUDGE** *(Stand)*: Court is now in session for the trial of `[FRIEND]`. On all seven counts.
> **EDGEWORTH** *(Confident Smirk)*: The prosecution is ready, Your Honour. Frankly, over-ready.
> **EDGEWORTH** *(Point)*: Seven victims. Seven countries. And a signature so exact it reads like a calling card — each one killed by the very food that shares the name of the place they died.
> **EDGEWORTH** *(Stand)*: A mob fixer crushed under a runaway cheese wheel on a hill road in Edam. A spacefaring billionaire face-down in a brine barrel in Kalamata. A drinks-startup “disruptor” poured into the floor of his own launch party in Tequila. A crypto founder buried to the collar in beans in Lima.
> **EDGEWORTH** *(Confident Smirk)*: The world did not mourn them. A mobster, a huckster, a billionaire who wanted off the planet — no great loss, the papers agreed.
> **EDGEWORTH** *(Desk Slam)*: But no loss is not no crime. Seven murders remain seven murders.
> **EDGEWORTH** *(Point)*: For two years this killer left nothing. No print, no trace. Until Sydney. The seventh — a star auctioneer, shucked on the harbour rocks like the morning's catch. The signature, intact.
> **EDGEWORTH** *(Stand)*: But this time they were careless. Beside the body they left something that does *not* fit the pattern: a Chinese-noodle takeaway container. And on it — one clean DNA profile.
> **EDGEWORTH** *(Confident Smirk)*: It belongs to the defendant. The prosecution needs one match. It has it.

> **PHOENIX** *(Point, HOLD IT bubble)*: HOLD IT!
> **PHOENIX** *(Desk Slam)*: That's my client you're filing under "already decided."
> **PHOENIX** *(Stand)*: Wright, for the defence.
> **PHOENIX** *(Read — reading the charge sheet)*: So let me be sure I follow the charge. Seven murders — the cheese, the brine, the beans — none of which you can place on my client.
> **PHOENIX** *(Read)*: The one thing you *can* place on them is a takeaway container. Stripped down, the charge is... eating a meal.
> **PHOENIX** *(Silly — the cheeky grin)*: A **succulent Chinese meal**.
> **EDGEWORTH** *(Cornered)*: The *murder* is the charge, Wright. The meal is merely where they got careless.
> **PHOENIX** *(Point)*: Then let's look at the one thing tying my client to any of it. I move to enter the raw DNA read into evidence.
> **JUDGE** *(Stand)*: Granted. The court will recess to examine it.

### [PAGE] — recess
> *Fade to black. One line:*
> **Is there anything off about the prosecution's one piece of evidence? Look again.**
> → *[the container's DNA trace — the forged victim trace]*

### [PANEL] — MULTIPLE-CHOICE OBJECTION  *(component to build)*
Prompt: *Is there anything off about the prosecution's evidence?*
- **A)** It's clean through the *middle* of the read. *(Not quite.)*
- **B)** The peak heights rise and fall across the read. *(Not quite.)*
- **C)** It's clean right to *both edges.* **← CORRECT**
- **D)** There's faint baseline noise between the peaks. *(Not quite.)*

*(Wrong picks: "Not quite." and re-enable.)*

### [CLIP 2] — objection sustained  *(Phoenix · Edgeworth)*
> **PHOENIX** *(Point, OBJECTION bubble)*: OBJECTION! Look at the edges of that trace.
> **PHOENIX** *(Desk Slam)*: A real read is a mess at both ends. This one is flawless corner to corner.
> **PHOENIX** *(Confident)*: Nobody *recovered* this sequence. Somebody *built* it.
> **EDGEWORTH** *(Cornered)*: ...You're alleging the trace is synthetic.
> **PHOENIX** *(Stand)*: I'm alleging it was forged from scratch — to read as my client.

### [PAGE] — the frame
> If the trace was forged, the forger built it from *real* DNA — their own — and edited a handful of bases so it would read as someone else. So whose sequence is underneath?
> The defence pulls the three names with any grudge against `[FRIEND]`. Align each against the fake.
> → *[the three suspect traces]*

### [PANEL] — SUSPECT DOSSIERS ×3  *(component — detailed copy still TBD together)*
Framing only, for now: two are people `[FRIEND]` genuinely has beef with (the renamed job-board "headhunter"; the surgeon(s) who ghost every email — no trace they ever existed). The **third — Xanthea Yee —** she has no quarrel with at all: a near-stranger who only surfaced because a rushed database confused *her* name for `[FRIEND]`'s. The obvious read: she's the unlikely one, mistaken identity.
Then you align + translate. Two suspects' edits spell garbage. **Xanthea Yee's** — the no-quarrel near-stranger — spell a confession. *(Her trace = the current `suspect_Wren.ab1`, to be renamed.)*

### [PANEL] — ALIGN & TRANSLATE → the reveal  *(stub for Part-2 of the DNA puzzle: the hint ladder guiding align → translate → find-the-confession, in `hint-panel.html`)*
> Translate Xanthea Yee's trace. One clean ORF, starting (as every protein must) with **M**:
>
> `MWAHAHAHAITSAMEIMTHEIMPASTA` → **MWAHAHAHA · IT'S-A ME · I'M THE IMPASTA**

### [PANEL] — `accuse.html`  *(accusation board — built; now BEFORE the summation)*
> You name the Grocer. Not the enemies who'd want `[FRIEND]` gone — the stranger whose name was one keystroke away. **Accuse Xanthea Yee.**

### [CLIP 3] — THE FINAL SOLUTION  *(Phoenix · Judge · Edgeworth — the full frame, one chain)*
> **PHOENIX** *(Point, TAKE THAT bubble)*: TAKE THAT! That "one clean match" was never recovered off the container. It was forged *onto* it.
> **PHOENIX** *(Stand)*: The real Grocer — Xanthea Yee, the name you just put on that board — left her own DNA in Sydney, panicked, and rebuilt the trace to read as someone else. She didn't pick my client at random. She picked the name that was already almost hers.
> **PHOENIX** *(Read — holding the two names side by side)*: One letter added to the front. One letter changed at the end. `[FRIEND]` becomes **Xanthea Yee.** A rushed database doesn't look twice. It didn't.
> **PHOENIX** *(Desk Slam)*: So my client never *stumbled* into this case. They were **cast** in it. Handed a part in someone else's production and walked to each mark on cue.
> **PHOENIX** *(Point)*: Cue one — a "misdirected" letter. Sent, not slipped. It put the Grocer's trail in my client's hands and pointed them up it. Which is how they came to be inside an Interpol evidence locker without, strictly speaking, a key—
> **PHOENIX** *(Damage — hearing himself say it)*: —which I. did not. mean to say. out loud.
> **JUDGE** *(Surprised)*: Mr Wright. Did your client break into an Interpol facility?
> **PHOENIX** *(Cornered)*: The facility was unmanned. The door was — I'm reliably told — *ajar.* That's barely a break-in. That's a firm knock. Not the crime we're here about. Moving on—
> **PHOENIX** *(Point)*: Cue two — Tokyo. The one city left unstruck on the Grocer's list, dangled as bait, so whoever was chasing the killer would be standing at the next scene when the net dropped. Cue three — the container. A signed confession, wrong name, left where it couldn't be missed.
> **PHOENIX** *(Stand)*: You don't hack Interpol, forge a genome, and stage a lure across three continents on a whim. Someone wrote the shopping list. Someone with a state behind them — call them the **Buyer.** The Grocer only ever filled the order.
> **PHOENIX** *(Confident)*: As for the Grocer herself — she couldn't help the flourish. The same vanity that signed seven kills with the food of the place signed the forgery too. Undo her edits, translate what's left, and she confesses in her own hand —
> **PHOENIX** *(Desk Slam)*: **MWAHAHAHA. IT'S-A ME. I'M THE IMPASTA.**
> **PHOENIX** *(Point)*: An imposter. A pasta. Take your pick. Either way — *not my client.*
> **EDGEWORTH** *(Cornered)*: ...A trace built from nothing. And a forger too pleased with herself to keep quiet.
> **EDGEWORTH** *(Bow)*: The prosecution has no interest in convicting the wrong person. Your Honour — the state withdraws its match.

### [CLIP 4] — verdict  *(Judge)*
> **JUDGE** *(Stand)*: With its sole piece of evidence withdrawn, this court finds the defendant...
> **JUDGE** *(Positive)*: **NOT GUILTY.**
> **JUDGE** *(Surprised)*: ...And someone notify Interpol. It appears they're looking for an *impasta.*

### [PAGE] — closer
> **CASE FILE 0507 — CLOSED.**
> Happy birthday, `[FRIEND]`. Framed for seven murders across seven countries, extradited, tried in a foreign court, and cleared over a tub of noodles. Only you could turn a birthday into an international incident — and walk out acquitted.

---

## STATUS OF THE FLAGGED BEATS
1. **Victims** — reconciled against the **locked crime map** (D6): Edam = mob fixer *crushed under the cheese wheel* (not drowned in dairy); Lima = *crypto founder* (not a mining magnate); Kalamata = *spacefaring* billionaire. Tequila unchanged. ✔
2. **Break-in** — now an *accidental blurt* (D6): Phoenix says it mid-flow, **Damage** pose as he hears himself, Judge double-takes, **Cornered** backpedal ("a firm knock"). Reads as a slip, not a knowing half-admission. ✔
3. **Handler** — named **the Buyer**; state-backed-assassin angle folded in (the shopping list = the order). Veto the name if it doesn't land. ✔
4. **Dossier card copy** — still deferred (the "handle separately" item). ✔
5. **Pose note:** meal-joke beat is now **Silly** (the cheeky grin) — swapped from Confident in D6. All poses in this draft are verified against `poses.json`. New in D6: **Read** (name-collision, id 59) and **Damage** (the blurt, id 129) — both real Phoenix poses.
6. **"Cast in it" (D6):** restored — the frame is now staged as a three-cue "production" (letter → Tokyo bait → container), with the defendant "cast" rather than stumbling in. The name-collision line (`[FRIEND]` → Xanthea Yee) sits right before it as the setup.

## CLIPS TO GENERATE (once locked)
- **Clip 1** — opening → charge (Judge, Edgeworth, Phoenix)
- **Clip 2** — objection sustained (Phoenix, Edgeworth)
- **Clip 3** — final solution / frame reveal (Phoenix, Edgeworth)
- **Clip 4** — verdict (Judge)
