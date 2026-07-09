# Act 3 — the courtroom (drop-in folder)

Open **index.html** and click straight through to **closer.html**. Chain:

`index → narration → clip1 → panel_objection → clip2 → reveal1a → panel_dossiers → reveal1b → panel_decode → accuse → reveal2 → clip4 → closer`

## What you need to do
1. **Export the 6 clips to MP4.** In the objection.lol Maker: Project → Load each `*.objection`, then Export MP4. Name the outputs exactly:
   `clip1.mp4 · clip2.mp4 · reveal1a.mp4 · reveal1b.mp4 · reveal2.mp4 · clip4.mp4`
   Drop them in this folder. (The `.objection` sources are here; the wrapper pages already point at those filenames.)
2. **Add `narration.html`** (your locked Scene-1 file) to this folder, and point its final link at `clip1.html`.
3. **Push the folder to GitHub Pages.** All links are relative, so it just works.

## The `.ab1` downloads (⚠ placeholders)
`evidence_trace.ab1`, `seek_com.ab1`, `the_surgeon.ab1`, `xanthea_yee.ab1`, `reference.fasta` are the *current* traces, wired so the download flow is live. The **rework is the next task** — forgery reads as Anthea, surgeon no-align, seek.com gappy, only Xanthea a near-match carrying the 27-AA confession. Re-upload `make_ab1.py` / `encode_protein_orf.py` / `build_case_ab1s.py` and I'll regenerate them in place.

## Resume
Every page records progress in localStorage; `index.html` offers **Resume**. So she can download the traces, disappear into SnapGene for as long as she likes, and pick up exactly where she left off.

## Editable bits
- `panel_objection.html` — the multiple-choice `CHOICES`.
- `accuse.html` — `SUSPECTS` (Xanthea's icon = `xanthea_yee.png`, drop the headshot in).
- `panel_dossiers.html` / `panel_decode.html` — suspect list, hint ladder, `.ab1` links.
- `act3.css` — the shared parchment theme.
