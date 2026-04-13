"""
PC: 마우스 hover 시 컨트롤 표시 (원래 방식)
Touch(아이패드/모바일): 항상 표시
토글 버튼은 두 경우 모두 숨김 (CSS로 처리하므로 불필요)
"""
import os, re

REPO = os.path.dirname(os.path.abspath(__file__))

# </style> 바로 앞에 삽입할 CSS
EXTRA_CSS = """
      /* ── PC: hover 표시 / 터치: 항상 표시 ── */
      @media (hover: hover) and (pointer: fine) {
        .ctrl-toggle { display: none; }
        .viewer-wrapper:hover .controls  { opacity: 1; pointer-events: auto; }
        .viewer-wrapper:hover .zoom-slider { opacity: 1; pointer-events: auto; }
      }
      @media (hover: none) and (pointer: coarse) {
        .ctrl-toggle { display: none; }
        .controls    { opacity: 1 !important; pointer-events: auto !important; }
        .zoom-slider { opacity: 1 !important; pointer-events: auto !important; }
      }
"""

ok = skip = 0

for root, dirs, files in os.walk(REPO):
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            src = f.read()

        # 이미 적용된 파일 건너뜀
        if 'hover: hover' in src and 'pointer: fine' in src:
            skip += 1
            continue

        # ctrl-toggle 이 없는 파일 건너뜀 (대시보드 등)
        if 'ctrl-toggle' not in src:
            skip += 1
            continue

        out = src.replace('</style>', EXTRA_CSS + '    </style>', 1)

        if out == src:
            skip += 1
            continue

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(out)
        print(f'[OK] {fpath}')
        ok += 1

print(f'\n완료: {ok}개 수정, {skip}개 건너뜀')
