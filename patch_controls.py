"""
모든 index.html 파일에 컨트롤 토글 버튼 자동 적용
- Pattern A: 단일 모델 뷰어 (zoom-slider 없음)
- Pattern B: 플레이리스트 뷰어 (zoom-slider 있음) → BJ_INNERRACE/index.html 등
"""
import os, re

REPO = os.path.dirname(os.path.abspath(__file__))

# ── 추가할 CSS ──────────────────────────────────────────────
TOGGLE_CSS = """
      /* ── 컨트롤 토글 버튼 (항상 표시) ── */
      .ctrl-toggle {
        position: fixed;
        bottom: 1rem;
        right: 1rem;
        z-index: 30;
        width: 48px; height: 48px;
        border-radius: 14px;
        border: none;
        background: rgba(0,0,0,.55);
        color: #fff;
        font-size: 1.3rem;
        cursor: pointer;
        display: flex; align-items: center; justify-content: center;
        backdrop-filter: blur(4px);
        transition: background .2s;
      }
      .ctrl-toggle.active { background: rgba(182,95,207,.85); }
"""

# ── 추가할 JS (Pattern A: zoom 없음) ───────────────────────
TOGGLE_JS_A = """
      /* ── 컨트롤 토글 ── */
      const ctrlToggle = document.getElementById('ctrlToggle');
      const controlsEl = document.querySelector('.controls');
      function setControls(show) {
        controlsEl.classList.toggle('show', show);
        ctrlToggle.classList.toggle('active', show);
        ctrlToggle.textContent = show ? '✕' : '⏵';
      }
      ctrlToggle.addEventListener('click', () => setControls(!controlsEl.classList.contains('show')));
      if (window.matchMedia('(hover: none) and (pointer: coarse)').matches) setControls(true);
"""

# ── 추가할 JS (Pattern B: zoom 있음) ───────────────────────
TOGGLE_JS_B = """
        /* ── 컨트롤 토글 ── */
        const ctrlToggle   = document.getElementById('ctrlToggle');
        const controlsEl   = document.querySelector('.controls');
        const zoomSliderEl = document.querySelector('.zoom-slider');
        function setControls(show) {
          controlsEl.classList.toggle('show', show);
          zoomSliderEl.classList.toggle('show', show);
          ctrlToggle.classList.toggle('active', show);
          ctrlToggle.textContent = show ? '✕' : '⏵';
        }
        ctrlToggle.addEventListener('click', () => setControls(!controlsEl.classList.contains('show')));
        if (window.matchMedia('(hover: none) and (pointer: coarse)').matches) setControls(true);
"""

ok = 0
skip = 0

for root, dirs, files in os.walk(REPO):
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root, fname)

        with open(fpath, 'r', encoding='utf-8') as f:
            src = f.read()

        # 이미 수정된 파일 건너뜀
        if 'ctrl-toggle' in src or '.viewer-wrapper:hover' not in src:
            skip += 1
            continue

        has_zoom = '.zoom-slider' in src
        out = src

        # ── CSS 수정 ─────────────────────────────────────────

        # 1) .controls: pointer-events 추가 + 주석 제거 + show 클래스 추가
        out = re.sub(
            r'(?:/\*[^*]*\*/\s*)?(opacity: 0;\s*\n\s*transition: opacity 0\.3s;)\s*\n(\s*\})',
            lambda m: f"opacity: 0;\n      pointer-events: none;\n      transition: opacity 0.3s;\n    }}\n    .controls.show {{ opacity: 1; pointer-events: auto; }}",
            out, count=1
        )

        # 2) hover 규칙 제거 (단일 또는 복합 selector)
        out = re.sub(
            r'\s*\.viewer-wrapper:hover \.controls(?:,\s*\n?\s*\.viewer-wrapper:hover \.zoom-slider)?\s*\{[^}]*\}',
            '', out
        )

        # 3) zoom-slider opacity 제거 (Pattern B)
        if has_zoom:
            out = re.sub(
                r'(\.zoom-slider \{[^}]*?)opacity: 0;\s*\n(\s*transition: opacity 0\.3s;)',
                r'\1opacity: 0;\n      pointer-events: none;\n\2',
                out, count=1
            )
            out = out.replace(
                'transition: opacity 0.3s;\n      display: flex;',
                'transition: opacity 0.3s;\n      display: flex;', 1
            )
            # .zoom-slider.show 추가
            out = re.sub(
                r'(\.zoom-slider \..*?font-weight: bold;\s*\n\s*\})',
                r'\1\n      .zoom-slider.show { opacity: 1; pointer-events: auto; }',
                out, count=1
            )

        # 4) 미디어 쿼리 제거
        out = re.sub(
            r'\s*@media\s*\(hover:\s*none\)\s*and\s*\(pointer:\s*coarse\)\s*\{[^}]*\}',
            '', out
        )

        # 5) 토글 CSS 추가
        out = out.replace('</style>', TOGGLE_CSS + '    </style>', 1)

        # ── HTML 수정 ─────────────────────────────────────────
        out = re.sub(
            r'(\s*)(<div class="controls">)',
            r'\1<button id="ctrlToggle" class="ctrl-toggle" title="컨트롤 표시/숨기기">⏵</button>\n\1\2',
            out, count=1
        )

        # ── JS 수정 ──────────────────────────────────────────
        if has_zoom:
            # Pattern B: window.addEventListener DOMContentLoaded 안에 추가
            out = re.sub(
                r"(window\.addEventListener\('DOMContentLoaded',\s*\(\)\s*=>\s*(?:playModel\(currentIndex\)|{[^}]*})\s*\);)",
                lambda m: m.group(0).rstrip(');') + TOGGLE_JS_B + '      });',
                out, count=1
            )
        else:
            # Pattern A: </script> 바로 앞에 추가
            out = out.replace('  </script>', TOGGLE_JS_A + '\n  </script>', 1)

        if out == src:
            print(f"[SKIP - no change] {fpath}")
            skip += 1
            continue

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(out)
        print(f"[OK] {fpath}")
        ok += 1

print(f"\n완료: {ok}개 수정, {skip}개 건너뜀")
