# Evidence ledger

| Item | Basis | Evidence status |
|---|---|---|
| Original research baseline and reference results | ACL Anthology source + official GitHub README | VERIFIED primary source; published repository reference 0.900/0.883 |
| User's prior review topic | Supplied scholarly review PDF, sections 1 and 6 | VERIFIED as user's review; some review references not reverified |
| Original corpus and label counts | Actual Colab data audit and original repository README | VERIFIED in user logs |
| Five-fold index integrity | Modules 5A, 5S actual prints | VERIFIED |
| BioBERT classifier, optimizer tests | Modules 4E–4M actual prints | VERIFIED within tested cases |
| Fold training and final-epoch scores | Modules 5D, 5G, 5J, 5M, 5P | VERIFIED genuine logs |
| Independent per-fold audits | Modules 5E, 5H, 5K, 5N, 5Q, 5S | VERIFIED genuine logs |
| Checkpoint reload | Modules 5F, 5I, 5L, 5O, 5R | VERIFIED as tested |
| Raw Colab CSVs, original manifests, checkpoint blobs accessible in ZIP | Not provided | NOT AVAILABLE; must add |
| New controlled editing experiment | Not performed | NOT EXECUTED |
| External validation and multi-seed study | Not performed | NOT EXECUTED |
| Dataset redistribution license | Not established | [TO VERIFY] |
| Code audit commit diffs | Official upstream source snippets available, student's Git history absent | [TO VERIFY] |

Notes: `fold_metrics_FROM_VERIFIED_CHAT_LOG.csv` and `epoch_losses_FROM_VERIFIED_CHAT_LOG.csv` are **transcriptions of printed output**. They do not establish a clean-runnable reproduction.
