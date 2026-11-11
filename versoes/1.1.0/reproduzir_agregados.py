import sys, csv
from collections import Counter, defaultdict
from openpyxl import load_workbook
wb=load_workbook(sys.argv[1],data_only=True,read_only=False)
it=wb['Dados'].iter_rows(values_only=True); headers=next(it)
rows=[dict(zip(headers,r)) for r in it if r[0] is not None]
assert len(rows)==len({r['ID'] for r in rows})==9585
counts=Counter(str(r['Processo_SIAD']).split()[0] for r in rows)
print('Unidades:',dict(sorted(counts.items())), 'Total:',sum(counts.values()))
groups=defaultdict(lambda:[0,0,0.0])
for r in rows:
 if r['Origem'] in ('NACIONAL','MULTIPLANTA'):
  g=groups[r['Classificacao_P_final']]; g[0]+=1
  v=r['Valor_homologado_item_real_2025']
  if v is not None: g[1]+=1; g[2]+=v
total=sum(g[2] for g in groups.values())
for k,g in sorted(groups.items()): print(k,g[0],g[1],g[2] if g[1] else None,100*g[2]/total if g[1] else None)
print('Denominador:',total)
