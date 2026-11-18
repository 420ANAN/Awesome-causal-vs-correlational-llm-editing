# Research decision log (evidence-labeled)

| Topic | Decision/evidence | State |
|---|---|---|
| Review linkage | The supplied review *Preservation of Causal Versus Correlational Language During LLM-Assisted Editing*, section 6, proposes an edited-pair benchmark and controlled counterfactual tests. | VERIFIED as proposal in the user-supplied review; not yet experimentally validated |
| Narrow problem | Validate source-guided BioBERT causal-language classification as a prerequisite to investigating meaning-preserving editing. | VERIFIED completed baseline scope |
| Proposed next research question | Can a four-class classifier distinguish meaning-preserving paraphrases from annotated causal inflation/attenuation in matched source–edit pairs? | HYPOTHESIS / NOT TESTED |
| G3 experimental pathway | Pathway A: baseline reproduction plus controlled editing-robustness extension. | PROPOSED; requires approved protocol and authentic edited pairs |
| Output metric | Matched-pair semantic-change detection performance against human judgments; also base class macro-F1 and false alarms on genuine paraphrases. | PROPOSED; define and preregister before seeing test data |
| Baseline strategy | Preserve original modern reproduction and use frozen checkpoints. Separate a human label / simple lexical comparator when feasible. | PROPOSED; not executed |
| Splits | Stored row-wise five-fold manifests, full coverage by row ID. | VERIFIED in user-provided Module 5S log |
| Data issue | Global class weights use all labels; duplicate text overlaps training/test in some folds. | VERIFIED original-method limitation |
| Result | Five-fold accuracy 0.898075; macro-F1 0.882203. | VERIFIED in user-provided Module 5S log |
| Historical equivalence | Original archive, optimizer runtime, fold identity and RNG consumption unverified. | UNCERTAIN |
| Paper contribution | Validated numerical baseline + transparent error and artifact audit, **not novel classification algorithm**. | VERIFIED scope |
| Next action | Acquire genuine paired-edit data; freeze test design; run controlled comparator and capture logs. | NOT EXECUTED |
