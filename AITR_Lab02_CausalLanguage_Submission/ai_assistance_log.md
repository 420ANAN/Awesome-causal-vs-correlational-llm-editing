# AI-assisted research provenance (concise)

Tool: OpenAI ChatGPT. Exact historical model identifiers, full prompt exports and corresponding commit diffs **[TO VERIFY]**. No claim of exact human-written versus AI-written line attribution is made.

| Task | AI proposal | Human verification | Observed result |
|---|---|---|---|
| Audit published optimizer | Compare historical BertAdam implementation with modern optimizer assumptions | Inspected class source, ran Modules 4J–4L | Confirmed absence of bias correction, first-step zero LR, tested per-tensor clipping and updates |
| Build classifier and test gradients | BioBERT pooled output + dropout + linear 4-class head | Model and gradient sanity checks Modules 4E–4M | Forward, losses and real parameter update checks passed |
| Validate splits | Fivefold manifests with seeded internal validation | Module 5A generated and checked manifests | Every original row in exactly one held-out fold; historical folds not identical |
| Train/evaluate | Five epochs per fold with controlled settings | Actual printed five-fold epoch logs and metrics | 0.898075 accuracy; 0.882203 macro-F1 mean |
| Independently audit saved results | Validate row IDs, labels, probabilities and recompute scores | Modules 5E,5H,5K,5N,5Q,5S | All tested predictions and metrics consistent |
| Verify checkpoints | Fresh architecture, strict checkpoint loading and re-inference | Modules 5F,5I,5L,5O,5R | Fold 0: 8 checked; Folds 1–4: all test labels reproduced |
| Scientific writing | Distinguish verified result and conjecture | Compared draft with logs; technical review noted citation and leakage limits | Unsupported preservation / exact-replication claims deliberately excluded |

**Three real AI limitations or purposeful checks:** (1) AdamW not assumed equivalent to historical BertAdam; source and toy updates checked. (2) differing historical vs current fold sizes explicitly disclosed, not suppressed. (3) metric output revalidated from CSV rather than accepted on faith. (4) checkpoint file presence independently tested by restoration.

**Human scientific decisions reflected in reported workflow:** preserve final-epoch rule; keep historical weighting for reproduction but flag leakage; freeze modern manifests; distinguish causal classification from editing fidelity. These actions are supported by conversation logs, but dated personal decision records and commit provenance remain [TO VERIFY].

**Lessons:** AI assistance expedites drafting code, but executable outputs, methodological checks and honest limitation reporting are essential. No quantified productivity gain or new model performance gain is claimed.

**Integrity controls:** Do not fabricate experiment outputs, commit history, human annotation or licensing; archive prompt-to-code decisions, verify redistributed files, remove secrets before publication.
