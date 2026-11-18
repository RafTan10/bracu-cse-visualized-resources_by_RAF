#!/usr/bin/env python3
"""CSE422 Lab Mid drill checker (offline). Needs only the Python standard library.

    python check.py lab1_01_astar_expand.py      mark one drill
    python check.py --hint lab1_01_astar_expand.py
    python check.py --solution lab1_01_astar_expand.py
    python check.py                               list drills and your progress
"""
import sys, os, json, io, random, traceback, contextlib

HERE = os.path.dirname(os.path.abspath(__file__))
DRILLS = json.load(open(os.path.join(HERE, '_drills.json'), encoding='utf-8'))
PROG = os.path.join(HERE, '.progress.json')

def load_progress():
    try: return json.load(open(PROG))
    except Exception: return {}

def run_src(src, name):
    ns = {'__name__': '__main__'}
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        exec(compile(src, name, 'exec'), ns)
    return ns, out.getvalue()

def mark(fname):
    d = DRILLS[fname]
    student_src = open(os.path.join(HERE, fname), encoding='utf-8').read()
    random.seed(0); ref, _ = run_src(d['prelude'] + d['solution'] + d['postlude'], 'reference')
    print('=' * 66); print(' ', fname, '—', d['title']); print('=' * 66)
    try:
        random.seed(0); ns, out = run_src(student_src, fname)
    except SyntaxError as e:
        print('  ERROR  SyntaxError:', e); return False
    except Exception as e:
        print('  ERROR  your program crashed:'); sys.stdout.flush(); traceback.print_exc(limit=-3); return False
    print('Your program printed:'); print('  ' + out.rstrip().replace('\n', '\n  ') if out.strip() else '  (nothing)')
    tns = {}; exec(d['tests'], tns); random.seed(0)
    try:
        tns['check'](ns, ref)
    except AssertionError as e:
        print('\n  FAIL   ' + (str(e) or 'a check failed')); return False
    except Exception as e:
        print('\n  FAIL   your code raised %s: %s' % (type(e).__name__, e)); return False
    print('\n  PASS   all checks passed.')
    p = load_progress(); p[fname] = True; json.dump(p, open(PROG, 'w'))
    return True

def main(argv):
    flags = [a for a in argv if a.startswith('--')]; files = [a for a in argv if not a.startswith('--')]
    if not files:
        p = load_progress()
        for lab in (1, 2, 3):
            print('\nLab %d' % lab)
            for f, d in DRILLS.items():
                if d['lab'] == lab:
                    print('  %s %-32s %-16s %s' % ('[x]' if p.get(f) else '[ ]', f, d['tag'], d['title']))
        print('\nRun:  python check.py <file>')
        return
    all_ok = True
    for f in files:
        f = os.path.basename(f)
        if f not in DRILLS: print('Unknown drill', f); all_ok = False; continue
        if '--hint' in flags: print('HINT:', DRILLS[f]['hint']); continue
        if '--solution' in flags: print(DRILLS[f]['solution']); print('NOTES:', DRILLS[f]['notes']); continue
        if not mark(f): all_ok = False
    sys.exit(0 if all_ok else 1)

if __name__ == '__main__':
    main(sys.argv[1:])
