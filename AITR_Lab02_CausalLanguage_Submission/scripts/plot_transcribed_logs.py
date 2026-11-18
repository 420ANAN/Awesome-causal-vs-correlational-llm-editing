#!/usr/bin/env python3
"""[TEST REQUIRED on student machine] Plot transcribed authentic Colab logs."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
x=pd.read_csv(ROOT/'results/fold_metrics_FROM_VERIFIED_CHAT_LOG.csv')
y=pd.read_csv(ROOT/'results/epoch_losses_FROM_VERIFIED_CHAT_LOG.csv')
out=ROOT/'results/figures';out.mkdir(exist_ok=True)
plt.figure(figsize=(7,4))
plt.plot(x.fold,x.accuracy,marker='o',label='Accuracy');plt.plot(x.fold,x.macro_f1,marker='s',label='Macro-F1')
plt.xlabel('Fold');plt.ylabel('Held-out score');plt.ylim(.85,.93);plt.legend();plt.grid(alpha=.25);plt.tight_layout();plt.savefig(out/'fold_scores.png',dpi=200);plt.close()
plt.figure(figsize=(7,4))
for fold,group in y.groupby('fold'):plt.plot(group.epoch,group.validation_loss_rounded,marker='o',label=f'Fold {fold}')
plt.xlabel('Epoch');plt.ylabel('Validation loss');plt.legend();plt.grid(alpha=.25);plt.tight_layout();plt.savefig(out/'validation_losses.png',dpi=200);plt.close()
print('Figures generated from VERIFIED, TRANSCRIBED log values only.')
