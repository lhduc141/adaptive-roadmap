#!/usr/bin/env python3
"""Read-only sanity checks for the Adaptive SE Roadmap bundle (stdlib only)."""
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parent.parent
MANDATORY=[
  '00_START_HERE.md','AGENT_ENTRY.md','docs/01_ROADMAP_MAIN.md',
  'docs/02_COMPETENCY_AND_COURSE_MAP.md','docs/03_CURRENT_STATE.md',
  'docs/04_EXECUTION_PROTOCOL.md','docs/05_CONTEXT_PROFILE.md',
  'docs/06_MARKET_BASELINE.md','docs/07_TODOIST_BRIDGE.md','docs/08_DATA_CONTRACT.md',
  'history/00_EVENT_INDEX.md','history/01_CHANGELOG.md',
  'history/02_DIAGNOSTICS.md','history/03_LEARNING_SESSIONS.md',
  'history/04_REVIEWS.md','subjects/SUB-OOP_COVERAGE.md',
  'reference/IU_REPORT_2026.md','reference/IU_COURSE_INDEX.md',
]
SKILLS=['roadmap-context-loader','adaptive-study-planner','subject-mastery-coach','roadmap-history-manager','market-signal-reviewer']
errors=[]
for f in MANDATORY:
 p=ROOT/f
 if not p.is_file(): errors.append('Missing '+f)
for s in SKILLS:
 p=ROOT/'skills'/s/'SKILL.md'
 if not p.is_file():
  errors.append('Missing skill '+s); continue
 body=p.read_text(encoding='utf-8')
 if not body.startswith('---\n'): errors.append('No YAML frontmatter '+s)
 if f'name: {s}' not in body: errors.append('Skill name mismatch '+s)
 if not re.search(r'^description: .+',body,re.M): errors.append('Missing skill description '+s)
 if len(body.splitlines())>500: errors.append('Skill excessive length '+s)
state=(ROOT/'docs/03_CURRENT_STATE.md').read_text(encoding='utf-8')
index=(ROOT/'history/00_EVENT_INDEX.md').read_text(encoding='utf-8')
changelog=(ROOT/'history/01_CHANGELOG.md').read_text(encoding='utf-8')
# Event ID is the second table column. Event type controls the referenced log.
rows=[]
for line in index.splitlines():
  if not re.match(r'^\|\s*\d{3}\s*\|',line): continue
  parts=[v.strip().strip('`') for v in line.split('|')[1:-1]]
  if len(parts)<7: errors.append('Malformed event index row: '+line[:50]); continue
  rows.append({'id':parts[1], 'logfile':parts[5], 'applied':parts[6]})
ids=[row['id'] for row in rows]
if not ids:errors.append('Event index empty')
else:
  applied=[row['id'] for row in rows if row['applied'].upper().startswith('YES')]
  if applied:
    last=applied[-1]
    if f'last_applied_event_id: "{last}"' not in state: errors.append('Snapshot last event differs from latest applied event in index')
  for row in rows:
    logfile=ROOT/row['logfile']
    if not logfile.is_file():errors.append('Missing log for '+row['id']+': '+row['logfile'])
    elif row['id'] not in logfile.read_text(encoding='utf-8'):
      errors.append('Index event not recorded in log: '+row['id'])
  if len(set(ids))!=len(ids): errors.append('Duplicate event index IDs')
main=(ROOT/'docs/01_ROADMAP_MAIN.md').read_text(encoding='utf-8')
for x in ['SUB-OOP','SUB-DSA','SUB-DBMS','SUB-OS','SUB-CN','SUB-SE']:
 if x not in main:errors.append('Missing course anchor in main: '+x)
if 'active_learning_unit_ids: []' in state and 'verified_completed_milestones: []' not in state:
 errors.append('No active units but completed milestone state unexpected')
print('Adaptive SE Roadmap validation:', 'PASS' if not errors else 'FAIL')
print('Checked',len(MANDATORY),'core files and',len(SKILLS),'skills,',len(ids),'indexed event(s).')
for e in errors:print('ERROR:',e)
sys.exit(1 if errors else 0)
