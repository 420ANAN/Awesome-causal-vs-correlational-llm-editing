# Baseline validation report — verified evidence vs unresolved claims

**VERIFIED from actual Colab outputs:** Data labels/counts, five-fold row coverage, source-guided architecture, head initialization sanity check, historical-style optimizer toy step consistency, actual BioBERT gradient updates, 25 epochs training, fold metrics independently recomputed from raw original results in Colab, all five checkpoint restoration tests, Module 5S full coverage and aggregate.

**Numerical result:** fold-mean accuracy 0.8980749341607226 (sample SD 0.007585466900178226); fold-mean macro-F1 0.8822025345457721 (sample SD 0.007464542238939849). Published repository rounded: accuracy 0.900, macro-F1 0.883. The difference is descriptive and does NOT constitute a statistical equivalence test.

**UNCERTAIN:** historical split identity (published sizes 614, 613, 613, 611, 610 vs modern 613, 612, 612, 612, 612), original BioBERT checkpoint tensor equivalence, exact historical BertAdam runtime behavior, full reproducibility from a clean runtime, final dataset distribution rights, multiple-seed stability and external-domain generalization.

**NEEDS CORRECTION for leakage-free claims:** historical full-corpus class weights incorporate held-out class frequencies, duplicate text crosses partitions; rerun separately with fitting-only weights and grouped splits before describing a leakage-free evaluation. Do not retrofit new results into the historical-style baseline.

**Known caveat:** Fold 0 saved checkpoint restoration tested 8 examples, Folds 1–4 all held-out samples. Full original Colab artifacts and execution notebook are NOT in this submission kit.
