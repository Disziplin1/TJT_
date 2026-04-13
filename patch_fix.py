"""남은 미디어쿼리 잔재 제거"""
import os, re

REPO = os.path.dirname(os.path.abspath(__file__))
ok = 0

for root, dirs, files in os.walk(REPO):
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            src = f.read()

        if '모바일은 항상 표시' not in src:
            continue

        out = src

        # 케이스 1: 주석 + @media 블록 (중첩 중괄호 처리)
        out = re.sub(
            r'\s*/\*[^*]*모바일[^*]*\*/\s*\n\s*@media[^{]*\{[^{}]*\{[^}]*\}\s*\n?\s*\}',
            '', out
        )

        # 케이스 2: 주석만 남은 경우 + 고아 } 제거
        out = re.sub(
            r'\s*/\*[^*]*모바일[^*]*\*/\s*\n\s*\}',
            '', out
        )

        if out != src:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(out)
            print(f'[FIX] {fpath}')
            ok += 1

print(f'\n{ok}개 수정 완료')
