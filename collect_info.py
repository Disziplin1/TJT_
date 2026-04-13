import os, re

REPO = r'C:\Users\Owner\Desktop\신정훈\3D 애니메이션\TJT_repo'
cats = ['BJ_CAGE','CJ_OUTERRACE','TJ_OUTERRACE','TRUNNION','GAUGE_']

for cat in cats:
    cat_path = os.path.join(REPO, cat)
    print('=== ' + cat + ' ===')
    for sub in sorted(os.listdir(cat_path)):
        sub_path = os.path.join(cat_path, sub)
        idx = os.path.join(sub_path, 'index.html')
        if not os.path.isfile(idx):
            continue
        with open(idx, encoding='utf-8') as f:
            c = f.read()
        title = re.search(r'<title>([^<]+)</title>', c)
        src = re.search(r'src="(https://[^"]+\.glb)"', c)
        t = title.group(1) if title else '?'
        s = src.group(1) if src else 'NO_GLB'
        print('  ' + sub + ' | ' + t + ' | ' + s)
