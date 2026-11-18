#!/usr/bin/env python3
"""[TEST REQUIRED] Read-only audit for authentic Colab outputs, not run here on absent raw files."""
from pathlib import Path
import argparse,json,hashlib
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score,f1_score,confusion_matrix
p=argparse.ArgumentParser();p.add_argument('--root',required=True,help='Root with results/fold_*/ and data/manifests/fold_*.json');a=p.parse_args()
root=Path(a.root);frames=[];records=[]
for i in range(5):
    pred=pd.read_csv(root/'results'/f'fold_{i}'/'test_predictions.csv')
    info=json.loads((root/'results'/f'fold_{i}'/'metrics.json').read_text())
    mb=(root/'data'/'manifests'/f'fold_{i}.json').read_bytes();manifest=json.loads(mb)
    assert len(pred)==(613 if i==0 else 612)
    assert pred.row_id.is_unique
    assert set(pred.row_id)==set(manifest['test_indices'])
    assert set(manifest['fit_indices']).isdisjoint(manifest['test_indices'])
    assert set(manifest['validation_indices']).isdisjoint(manifest['test_indices'])
    h=hashlib.sha256(mb).hexdigest()
    assert info.get('manifest_sha256',info.get('dataset_manifest_sha256'))==h
    prob=pred[['p0','p1','p2','p3']].to_numpy()
    assert np.isfinite(prob).all() and np.allclose(prob.sum(1),1,atol=1e-5)
    assert np.array_equal(prob.argmax(1),pred.pred_label)
    ac=accuracy_score(pred.true_label,pred.pred_label)
    f1=f1_score(pred.true_label,pred.pred_label,labels=[0,1,2,3],average='macro',zero_division=0)
    assert np.isclose(ac,info['accuracy']) and np.isclose(f1,info['macro_f1'])
    records.append((i,len(pred),ac,f1));frames.append(pred)
pooled=pd.concat(frames,ignore_index=True)
assert len(pooled)==3061 and pooled.row_id.is_unique and set(pooled.row_id)==set(range(3061))
print('folds:',records)
print('mean acc:',np.mean([r[2] for r in records]), 'mean macro F1:',np.mean([r[3] for r in records]))
print('pooled confusion:\n',confusion_matrix(pooled.true_label,pooled.pred_label,labels=[0,1,2,3]))
print('READ-ONLY AUDIT PASSED (only if actually executed with raw files)')
