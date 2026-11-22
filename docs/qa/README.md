# Shot-review evidence

`Episode_01.tsv` through `Episode_10.tsv` each contain 80 ordered, unique shot rows. Read them with the [master audit](../AUDIT_EP01_EP10.md), the selected episode's `STORY.md` and `CONTINUITY.md`, and the actual referenced PNG. The baseline cleanup ledger and archive checksums describe commit `09063a7`; they are historical records, not current-image manifests.

The [creator approval record](../../CURRENT_PRODUCTION_STATUS.md) identifies the 621 accepted shots at the November 22 checkpoint. The [blocked image repair list](BLOCKED_IMAGE_REPAIRS.md) links directly to all 179 outstanding shot findings. A later change to reviewed pixels requires fresh review.

Each episode TSV uses these tab-separated columns:

| Column | Meaning |
|---|---|
| `episode`, `board`, `shot` | Episode identity and the four-panel sheet/shot mapping. Earlier records use either `01` or `Episode_01`, and may include the `.png` suffix on board names. |
| `expected` | Current screenplay action, optionally prefixed with the visible cast and location. |
| `observed` | Recorded selected-image observation; this must not be inferred from a matching script alone. |
| `severity` | `major` for a recorded failure; `minor` for a noted concern awaiting review. `review`, `unrated` and `none observed` retain the original review vocabulary and confer no approval. |
| `correction` | Requested repair or remaining review work. |
| `evidence` | Repository-relative selected-image path, panel number and full current SHA-256; some rows also name screenplay/continuity sources. |
| `status` | `FAIL` for a documented major discrepancy, or the historical `NEEDS_HUMAN_REVIEW` label. Read the latter with the dated creator approval record for the specific pixels. |
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

For a checkout without readable artwork, run `python tools/check_audit_qa.py --source-only`. It checks every ledger row against the screenplay, including the action, board, panel and four matching full-length digests per sheet. It also checks prompt dialogue, cast and continuity fields against the script, and checks subtitle text, order, timing bounds and overlaps. The output identifies the omitted image-byte check. The default command above reads each selected PNG and verifies its SHA-256. The strict series checks also validate PNG structure and assets. The current approval record remains the authority for reviewed pixels.

After an authorized image correction, inspect the selected pixels against the source and original references before changing observations or status. Record recovery/provenance and replace all four evidence digests for the edited sheet, including unaffected panels. A digest refresh alone is insufficient to mark a defect repaired. After an authorized story edit, review the expected-action field alongside the episode's regenerated documents. Keep creator acceptance and approved single-shot production frames as explicit separate work.
