# One-page research brief — Gate G1 (draft, requires approval)

**Review topic:** Preservation of causal versus correlational language during LLM-assisted editing (supplied literature review, section 6).

**Source-supported gap statement:** The review identifies a need for an edit-pair benchmark incorporating the original claim, methodological context, edited wording and expert assessment of whether causal interpretation changed. This is a *proposal from the review*, not proof that no such benchmark exists; an updated gap search and source verification remain [TO VERIFY].

**Primary proposed RQ (not yet studied):** How reliably can a frozen four-class causal-language classifier flag meaning-altering changes in LLM-edited scientific sentences, compared with human annotation and a prespecified control?

**Supporting questions:** Which edit types (causal inflation, attenuation, hedge deletion, reversed direction) cause errors? Does category-level prediction stability agree with human meaning-preservation judgments?

**Study pathway:** A — reproduction + extension. The baseline reproduction is COMPLETE; extension is [NOT EXECUTED].

**Baseline:** Yu et al. (2019) four-class BioBERT; reproduced modern version five-fold mean accuracy 0.898075 and macro-F1 0.882203. This score does NOT measure paired editing fidelity.

**Data:** Existing 3,061-label PubMed sentences for baseline; paired-edit study needs new, independently labeled source–edit data [TO ACQUIRE]. Check licensing and permissible sharing.

**Variables and comparators:** Input: paired original/edited sentence. Outcome: annotated causal-status preservation / change. Compare frozen classifier change detector vs a justified simple control and human labels; **both comparator definition and actual experiment are pending**.

**Metrics:** Prespecify change-detection macro-F1, false-positive rate on accepted paraphrases, class-conditional errors and confidence intervals, with a clearly separated holdout split. Threshold and sample-size plan [TO VERIFY].

**Compute:** Existing Tesla T4 demonstrated; frozen-model inference cheaper than five-fold retraining. Human labeling burden and annotation agreement [TO VERIFY].

**Feasibility / go-no-go:** No ready-to-submit extension without an authentic evaluation corpus and proper comparisons. Preserve existing baseline outputs unchanged.
