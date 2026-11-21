# Shot-review evidence

`Episode_01.tsv` through `Episode_10.tsv` each contain 80 ordered, unique shot rows. Read them with the [master audit](../AUDIT_EP01_EP10.md), the selected episode's `STORY.md` and `CONTINUITY.md`, and the actual referenced PNG. The baseline cleanup ledger and archive checksums describe commit `09063a7`; they are historical records, not current-image manifests.

Each episode TSV uses these tab-separated columns:

| Column | Meaning |
|---|---|
| `episode`, `board`, `shot` | Episode identity and the four-panel sheet/shot mapping. Earlier records use either `01` or `Episode_01`, and may include the `.png` suffix on board names. |
| `expected` | Current screenplay action, optionally prefixed with the visible cast and location. |
| `observed` | Recorded selected-image observation; this must not be inferred from a matching script alone. |
| `severity` | `major` for a recorded failure; `minor` for a noted concern awaiting review. `review`, `unrated` and `none observed` retain the original review vocabulary and confer no approval. |
| `correction` | Requested repair or remaining review work. |
| `evidence` | Repository-relative selected-image path, panel number and full current SHA-256; some rows also name screenplay/continuity sources. |
| `status` | `FAIL` for a documented major discrepancy, or `NEEDS_HUMAN_REVIEW` for unresolved acceptance and fine-detail review. |
| `verification` | Scope of inspection and any pending creator acceptance. |

Run from the repository root:

```sh
python tools/check_audit_qa.py
python tools/check_series.py --strict-art
python tools/audit_series.py --strict-art
python tools/check_root_docs.py
for episode_dir in Episode_??; do
  python "$episode_dir/sync.py" --check || exit "$?"
done
python tools/production_handoff.py --output-dir /tmp/maple-audit-handoff
python -m unittest discover -s tests -v
git diff --check
```

The QA checker fails for missing/duplicate rows, blank cells, wrong board/panel references, incomplete or stale hashes, stale expected actions and unsupported status/severity pairs. It succeeds when the records are internally consistent, even when they contain visual failures. The strict series checks separately validate PNG structure, assets and source alignment. Neither grants creator approval.

After an authorized image correction, inspect the selected pixels against the source and original references before changing observations or status. Record recovery/provenance and replace all four evidence digests for the edited sheet, including unaffected panels. A digest refresh alone is insufficient to mark a defect repaired. After an authorized story edit, review the expected-action field alongside the episode's regenerated documents. Keep creator acceptance and approved single-shot production frames as explicit separate work.
