# Five-minute technical demonstration guide

**0:00–0:45 (problem)** Identify class 0=no relationship, 1=direct causal, 2=conditional causal, 3=correlation. Explain why category labels are not edited-pair semantic judgments.

**0:45–1:45 (source verification)** Show original ACL paper and source repository commit, user review section 6, four-class label counts. Mention 3,061 records and ethical data handling.

**1:45–2:45 (method)** Show actual original Colab notebook (to be attached): frozen split manifests, classifier head, full-corpus weighted loss, historical-style optimizer, final epoch rule. Explain held-out-label leakage without hiding it.

**2:45–3:45 (results)** Display independently audited fold score table, pooled confusion matrix and figure derived from genuine epochs. Identify 77 no-relation→correlation mistakes.

**3:45–4:30 (validation)** Re-run a **previously tested** prediction/metric audit in the Colab runtime or run clean replay only after verifying it. Show all row IDs held out once and checkpoint restoration output.

**4:30–5:00 (boundaries)** Name unverified historical-equivalence steps, missing new comparison/extension and future edit-pair study. Be prepared to explain optimizer bias correction, per-tensor clipping, cross-validation vs repeated seeds and why 0.8981 accuracy does not demonstrate editing preservation.

**[TEST REQUIRED]** Actual live demo rehearsal and timing.
