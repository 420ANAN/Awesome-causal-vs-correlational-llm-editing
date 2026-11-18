# AI Tools for Research — Post-Mid-Semester Project

**Study:** Source-guided modern reproduction and audit of Yu, Li and Wang (2019), *Detecting Causal Language Use in Science Findings*.

**Status:** Five-fold classification baseline trained and independently audited in the author's Google Colab session. **Not yet a complete final assignment** because no separate controlled comparison/extension study has been executed and the formal literature-to-gap research brief, licenses and publicly available executable repository remain to be confirmed.

## Research problem and scope

Scientific conclusions can express no relation, direct causality, conditional causality, or correlation. This project checks whether a modern BioBERT implementation closely reproduces a previously published four-class classification benchmark and whether the saved numerical results withstand independent audit. The motivating literature review concerns preserving causal meaning in LLM-assisted editing; **no LLM-edited sentence pairs were evaluated**. The proposed next question is in `research_decisions.md` and is not represented as an accomplished result.

## Measured baseline results (from genuine Colab logs)

| Fold | Test size | Accuracy | Macro-F1 |
|---|---:|---:|---:|
| 0 | 613 | 0.890701 | 0.878400 |
| 1 | 612 | 0.900327 | 0.887420 |
| 2 | 612 | 0.900327 | 0.883495 |
| 3 | 612 | 0.890523 | 0.871472 |
| 4 | 612 | 0.908497 | 0.890226 |
| **Mean** | — | **0.898075** | **0.882203** |

Sample SD across folds: accuracy 0.007585; macro-F1 0.007465. Pooled out-of-fold accuracy 0.898073 (2,749/3,061); pooled macro-F1 0.882170. Original repository rounded means: 0.900 and 0.883. Different folds and modern implementation prevent a claim of exact historical replication. Figures are generated **from rounded genuine training logs and full-precision verified fold metric logs**, not fabricated runs. `results/` stores transcribed evidence, *not the original Colab result files*.

## Source provenance

- Original study: https://aclanthology.org/D19-1473/ (DOI 10.18653/v1/D19-1473).
- Original code and data: https://github.com/junwang4/causal-language-use-in-science ; inspected commit `84abecc88b201a5ce27e1622597f780a9800c498`.
- Modified historical optimizer/code: https://github.com/junwang4/bert-sklearn-with-class-weight ; inspected commit `5f63b4c3ec3f3c4c06a73713a57f7a5f9354ae10`.
- Modern BioBERT: `dmis-lab/biobert-base-cased-v1.1`, pinned revision `924f12e0c3db7f156a765ad53fb6b11e7afedbc8` (do not redistribute checkpoints without checking terms).

## Environment used for actual Colab experiments

A previously printed environment snapshot reported Python 3.13.16, PyTorch 2.14.1+cu130, Transformers 5.22.1, Hugging Face Hub 1.33.0, NumPy 2.4.6, Pandas 2.2.3, scikit-learn 1.6.1, safetensors 0.8.0 and Tesla T4 CUDA. This is **not a verified dependency lockfile**. The snapshot and gaps are in `configs/environment_observed.txt`; `requirements_observed_NOT_LOCKED.txt` must **not** be mistaken for an installation-tested requirements lock.

## Dataset preparation

The dataset comes from the original public repository under `data/pubmed_causal_language_use.csv`. It has 3,061 rows; label frequencies 1,356/494/213/998 for classes 0/1/2/3. The original CSV was **not provided in this submission ZIP**. Dataset checksum observed in Colab: `f3e50fb07bfe9c9dcbbe3bbfcf0a27e71d460e06895b2867002a61c34ee1f202` (verify locally after obtaining exact data). There were seven duplicate sentence pairs (one conflicting-label pair) and suspected encoding artifacts; original text was not silently cleaned. Source repository code has GPL-3.0 terms; **separate dataset redistribution rights remain [TO VERIFY]**, hence no raw corpus is bundled.

**[TEST REQUIRED]** Reconstruct an equivalent source environment, check access and license terms before downloading, and compare dataset checksum:

```bash
# [TEST REQUIRED; not executed in this submission environment]
git clone https://github.com/junwang4/causal-language-use-in-science
cd causal-language-use-in-science
git checkout 84abecc88b201a5ce27e1622597f780a9800c498
sha256sum data/pubmed_causal_language_use.csv
```

## Reproducing the existing study

**Actually executed:** The author executed Colab modules 4J–5S for architecture/optimizer sanity checks, five fold training, per-fold result audits, checkpoint restoration and aggregation. The authentic runnable notebook(s) and raw checkpoint/prediction/manifest files have **not been uploaded to this package**. The project-relative Colab path was `/content/causal_language_reproduction/`. Do not claim the example scripts here rerun the entire experiment.

**[TEST REQUIRED]** With original raw Colab `results/fold_0`...`fold_4` and `data/manifests` imported into `raw_colab_artifacts/`, run:

```bash
python scripts/audit_original_results.py --root raw_colab_artifacts
```

The audit script is syntactically checked in this package against Python but its execution on the absent original CSV artifacts is **[TEST REQUIRED]**. It expects result files to contain `test_predictions.csv`, `metrics.json`, `training_history.csv`, and matching `fold_*.json` files. It checks row IDs and scores. No retraining command is advertised as verified: see `notebooks/README.md`.

To regenerate the **submission's transcribed-evidence figures**, the script `scripts/plot_transcribed_logs.py` is supplied. It is checked for syntax but a clean-install run in the student's target environment is **[TEST REQUIRED]**. Existing figures already come from actual logged numeric outputs.

## Metrics and comparison protocol

For every fold, 5 epochs, batch size 32, evaluation batch size 8, max sequence length 128, LR 2e-5, 10% linear warmup and historical BertAdam-style optimizer (no bias correction, per-parameter clipping) were used. 2,326 fit/122 validation/613 test for Fold 0; 2,327/122/612 for Folds 1–4. A final-epoch (not best-validation) checkpoint was evaluated. Full-corpus class weights match the original but leak held-out class-frequency information. Modern internal splits and tokenizer/weight provenance are not historically identical by proof.

## Computational resources

Actual GPU: NVIDIA Tesla T4. Observed Fold 0 elapsed code time 283.5 seconds. **Total five-fold runtime [TO VERIFY]**, and GPU memory peak not recorded. Checkpoint file size 433,337,475 bytes for each fold; approximately 2.17 GB across five (not included here). Training 365 optimizer steps per fold, 1,825 total.

## Limitations / fair comparisons

- Single trained model per fold, not multiple random-seed restarts.
- Historical outer fold sizes differ from modern partitions; no paired equivalence test.
- Full-dataset class weights use held-out labels; duplicate texts can cross fold boundaries.
- Original optimizer and historical BioBERT archive not proven equivalent to modern variants.
- Four-class classification is **not** causal-semantic preservation under LLM editing.
- No two-method controlled comparison or new extension has been executed. Assignment gate G3 is **pending**.

## Project organization

`paper/` contains an IEEE LaTeX manuscript and compiled PDF. `results/` contains transcriptions of genuine printed metrics and visualizations; `evidence/` has an evidence ledger, not original generated CSVs. `research_decisions.md`, `baseline_validation.md` and `ai_assistance_log.md` document decisions, limitations and human verification. `configs/` contains an explicit settings record and observed environment versions. `SUBMISSION_STATUS.md` lists missing evidence before a full submission claim.

## License and credits

The original repository identifies GPL-3.0 license terms; no claim is made that those terms necessarily cover all data or external model weights. This submission contains original documentation and analysis assembled from conversation evidence and verified source references. **[TO VERIFY]** licensing choice for the student's newly written files, data and model weight distribution, and any required copyright notices. Do not publish raw dataset or pretrained/fine-tuned weights before checking permissions. Credit Yu, Li, Wang (2019), Lee et al. (2020) for BioBERT and the cited software repositories. ChatGPT-assisted coding and analysis are disclosed in `ai_assistance_log.md`.

## Citation

See `paper/references.bib` for bibliographic entries verified against ACL Anthology and PubMed. For the student reproduction, a repository URL/DOI and final authorship are **[TO VERIFY]**. Do not cite the reproduction as a published peer-reviewed method.

## Minimum second-student reproduction checklist

- [ ] Obtain authorized original CSV; check exact dataset SHA-256, counts and licenses.
- [ ] Pin Python, PyTorch, Transformers, sklearn and model revision; record `pip freeze` and GPU details.
- [ ] Download checked code from verified commits; inspect historical-versus-modern adaptations.
- [ ] Obtain actual runnable Colab source or equivalent tested script; *do not assume this package has it*.
- [ ] Save and verify five fold manifests (all rows tested exactly once).
- [ ] Validate optimizer clipping/warmup and class-weight objective before training.
- [ ] Train five fresh models for five epochs each on immutable partitions.
- [ ] Audit every held-out `row_id`, gold label, argmax, and probability vector.
- [ ] Restore every checkpoint and independently reproduce predictions.
- [ ] Recompute fold arithmetic mean, SD, pooled metrics, confusion matrix and plots.
- [ ] Record deviations, seed variability, leakage and all commands actually executed.
