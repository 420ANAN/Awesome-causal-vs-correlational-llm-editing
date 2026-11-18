# Reference fixes and verification wording

`main_references_fixed.tex` preserves all original wording and formatting commands. The only changes are loading `hyperref` with `hidelinks` and wrapping the two DOI strings in hyperlinks.

`main.tex` uses the same formatting commands and also replaces the five visible [TO VERIFY] passages with the wording below. Text replacement can naturally change line and page breaks. The unused verification macro definitions remain unchanged.

Both versions use the existing inline `thebibliography`. A BibTeX run is not needed. `references.bib` is included as a companion record; it is not read by either version.

## Compilation

Use pdfLaTeX on `main.tex` (or `main_references_fixed.tex`) twice. Keep the `figures/` directory next to the selected main file. Overleaf: upload this ZIP, select the desired main document and compile with pdfLaTeX. The IEEEtran document class is required.

## Exact replacements

### 1. Related Work: Language-preserving editing

Replace the complete sentence or passage:

```latex
A comprehensive current novelty search and the review's nonprimary bibliographic metadata remain [TO VERIFY].
```

with:

```latex
A comprehensive current novelty assessment is outside the scope of this reproduction, and no claim of novelty for the proposed editing-preservation extension is made. Bibliographic details from the prior review that have not been checked against primary sources are not relied upon.
```

### 2. Experimental Setup: environment

Replace the complete sentence or passage:

```latex
Full dependency freeze, GPU memory-peak logging and the original experiment notebook export remain [TO VERIFY].
```

with:

```latex
A complete dependency freeze, peak GPU-memory measurements and an export of the original experiment notebook are not available in the materials accompanying this report.
```

### 3. Experimental Setup: artifact archive

Replace the complete sentence or passage:

```latex
The five manifest hashes were verified against the saved per-fold metadata; Their values were recorded in the execution logs, but a publicly accessible raw artifact archive and permanent deposit reference remain [TO VERIFY].
```

with:

```latex
The five manifest hashes were verified against the saved per-fold metadata; their values were recorded in the execution logs, but no publicly accessible raw artifact archive or permanent deposit identifier is provided with this report.
```

### 4. Results and Discussion: computational cost

Replace the complete sentence or passage:

```latex
Total observed runtime across all five folds was not supplied and remains [TO VERIFY].
```

with:

```latex
Total elapsed runtime across all five folds is unavailable from the supplied records and is therefore not reported.
```

### 5. Limitations: rights, annotation agreement and text overlap

Replace the complete sentence or passage:

```latex
Dataset-specific reuse rights, annotation reliability and exact overlap counts under archived folds remain [TO VERIFY].
```

with:

```latex
The \href{https://github.com/junwang4/causal-language-use-in-science}{source repository} displays a GPL-3.0 license, but dataset-specific reuse rights for the underlying PubMed text have not been independently established. Yu et al.~\cite{yu2019detecting} report Cohen's $\kappa=0.98$ for two annotators labeling conclusion sentences from 30 randomly selected abstracts; annotation agreement was not reassessed in this reproduction. Exact duplicate-text overlap counts under the archived folds are not available in the supplied records.
```

## Evidence and limits

- Yu et al. (2019), Section 3, p. 4667: Cohen's kappa 0.98 was reported for conclusion sentences from 30 randomly selected abstracts, labeled by two annotators. The remainder was annotated by one annotator with discussion of uncertain cases. This is a published source result, not a new annotation audit.
  https://aclanthology.org/D19-1473.pdf
- Yu et al. citation metadata: https://aclanthology.org/D19-1473/
- BioBERT issue year is 2020; online publication was 2019. The existing 2020 reference is retained. https://academic.oup.com/bioinformatics/article/36/4/1234/5566506
- The source repository displays GPL-3.0. This observation alone is not a determination of rights in every underlying PubMed sentence. https://github.com/junwang4/causal-language-use-in-science
- No total runtime, peak GPU memory, complete dependency freeze, public archive identifier or per-fold text-overlap count was invented. Export those from original experiment records before replacing the corresponding absence statements with values.
- These edits repair links and provide evidence-bounded wording. They do not rerun or validate the reported model experiments.
- Figure PDFs and the companion BibTeX file were copied unchanged from the earlier submission bundle.
- All table definitions, figure widths, captions, section structure, fonts, margins, IEEE class options and reported experimental values are retained.

## Validation performed

Both citation keys, all five internal reference uses, all labels, and the two figure-file paths were checked. No missing or duplicate reference targets were found. Reversing the declared changes reproduces the uploaded source exactly, so unrelated text and formatting commands are unchanged.

A full PDF build was attempted but could not be completed in this environment: the system LaTeX binaries have no format/package installation, and the alternate compiler bundle service returned HTTP 403. No successful PDF compilation is claimed. Compile twice with pdfLaTeX in Overleaf or a complete TeX Live/MiKTeX installation.
