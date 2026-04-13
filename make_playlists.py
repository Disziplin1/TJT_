"""
카테고리별 플레이리스트 index.html 자동 생성
- 애니메이션 방식: BJ_CAGE, CJ_OUTERRACE, TJ_OUTERRACE, TRUNNION
- 자동회전 타이머 방식: GAUGE_
"""
import os

REPO = os.path.dirname(os.path.abspath(__file__))

# ── 카테고리 데이터 ─────────────────────────────────────────────
CATEGORIES = {

    "BJ_CAGE": {
        "title": "BJ 케이지 측정기",
        "mode": "anim",
        "models": [
            { "name": "내경DIA 측정기",          "url": "https://disziplin1.github.io/TJT_/BJ_CAGE/DIA_GAUGE/DIA_GAUGE.glb",           "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "내경기준외경동심도 측정기", "url": "https://disziplin1.github.io/TJT_/BJ_CAGE/ID_Based/ID_Based.glb",             "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "내경심위치 측정기",         "url": "https://disziplin1.github.io/TJT_/BJ_CAGE/Inner_Diameter/Inner_Diameter.glb","cameraOrbit": "45deg 70deg 80%"  },
            { "name": "외경DIA 측정기",            "url": "https://disziplin1.github.io/TJT_/BJ_CAGE/Outer_Dia/Outer_Dia.glb",          "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "외경 심위치 측정기",        "url": "https://disziplin1.github.io/TJT_/BJ_CAGE/Outer_Diameter/Outer_Diameter.glb","cameraOrbit": "45deg 70deg 80%"  },
            { "name": "창폭&창위치 측정기",        "url": "https://disziplin1.github.io/TJT_/BJ_CAGE/Width_/Width_.glb",                "cameraOrbit": "45deg 70deg 80%"  },
        ]
    },

    "CJ_OUTERRACE": {
        "title": "CJ 외륜 측정기",
        "mode": "anim",
        "models": [
            { "name": "4BALL PCD(4구식) 측정기", "url": "https://disziplin1.github.io/TJT_/CJ_OUTERRACE/4Ball_PCD/4Ball_PCD.glb","cameraOrbit": "45deg 70deg 80%"  },
            { "name": "상호차 측정기",            "url": "https://disziplin1.github.io/TJT_/CJ_OUTERRACE/Mutual_/Mutual_.glb",    "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "PCD 측정기",               "url": "https://disziplin1.github.io/TJT_/CJ_OUTERRACE/PCD_/PCD_.glb",          "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "VC 측정기",                "url": "https://disziplin1.github.io/TJT_/CJ_OUTERRACE/VC_/VC_.glb",            "cameraOrbit": "45deg 70deg 80%"  },
        ]
    },

    "TJ_OUTERRACE": {
        "title": "TJ 외륜 측정기",
        "mode": "anim",
        "models": [
            { "name": "CHAMFER부 단차 측정기",               "url": "https://disziplin1.github.io/TJT_/TJ_OUTERRACE/CHAMFER_/CHAMFER_.glb",               "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "CW GAUGE",                            "url": "https://disziplin1.github.io/TJT_/TJ_OUTERRACE/CW_GAUGE/CW_GAUGE.glb",               "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "단면&전장 측정기",                    "url": "https://disziplin1.github.io/TJT_/TJ_OUTERRACE/Cross_Sectional/Cross_Sectional.glb",  "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "DIA 동축도 GAUGE",                    "url": "https://disziplin1.github.io/TJT_/TJ_OUTERRACE/DIA_GAUGE/DIA_GAUGE.glb",             "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "GROOVE 단차 측정기",                  "url": "https://disziplin1.github.io/TJT_/TJ_OUTERRACE/GROOVE/GROOVE.glb",                   "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "글로브 홈경 게이지",                  "url": "https://disziplin1.github.io/TJT_/TJ_OUTERRACE/Globe_Valve/Globe_Valve.glb",          "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "대그루브경 게이지",                   "url": "https://disziplin1.github.io/TJT_/TJ_OUTERRACE/Groove_g/Groove_g.glb",               "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "소재내경기준 외경동심도 측정기",      "url": "https://disziplin1.github.io/TJT_/TJ_OUTERRACE/ID_Based/ID_Based.glb",               "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "외경 측정기",                         "url": "https://disziplin1.github.io/TJT_/TJ_OUTERRACE/Outer_Diameter/Outer_Diameter.glb",   "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "구면거리 측정기",                     "url": "https://disziplin1.github.io/TJT_/TJ_OUTERRACE/Spherometer/Spherometer.glb",         "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "TAPER(CHAMFER)부 기준단차 검사 GAUGE","url": "https://disziplin1.github.io/TJT_/TJ_OUTERRACE/TAPER_CHAMFER/TAPER_CHAMFER.glb",     "cameraOrbit": "45deg 70deg 80%"  },
        ]
    },

    "TRUNNION": {
        "title": "트러니언 측정기",
        "mode": "anim",
        "models": [
            { "name": "분할각(각도) 측정기",                    "url": "https://disziplin1.github.io/TJT_/TRUNNION/Angle_Divider/Angle_Divider.glb",       "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "볼높이 측정기",                          "url": "https://disziplin1.github.io/TJT_/TRUNNION/Ball_/Ball_.glb",                       "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "내경기준(센터기준) 단면거리 측정기",    "url": "https://disziplin1.github.io/TJT_/TRUNNION/Center_Based/Center_Based.glb",           "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "CHAMFER부 단차 게이지",                  "url": "https://disziplin1.github.io/TJT_/TRUNNION/Chamfer_gauge/Chamfer_gauge.glb",         "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "GROOVE 편심 검사 GAUGE",                 "url": "https://disziplin1.github.io/TJT_/TRUNNION/GROOVE_GAUGE/GROOVE_GAUGE.glb",           "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "GROOVE 홈 조립 검사 측정기",             "url": "https://disziplin1.github.io/TJT_/TRUNNION/Groove_Checker/Groove_Checker.glb",       "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "저널DIA단면거리(연삭거리) 측정기",      "url": "https://disziplin1.github.io/TJT_/TRUNNION/Journal_DIA/Journal_DIA.glb",             "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "저널상하차(DIA상하차) 측정기",          "url": "https://disziplin1.github.io/TJT_/TRUNNION/Journal_Diameter/Journal_Diameter.glb",   "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "상하차 전용 측정기",                    "url": "https://disziplin1.github.io/TJT_/TRUNNION/Load_Unload/Load_Unload.glb",             "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "외경R게이지(내경기준 외경동심도)",      "url": "https://disziplin1.github.io/TJT_/TRUNNION/OD_R_gauge/OD_R_gauge.glb",               "cameraOrbit": "45deg 70deg 80%"  },
            { "name": "PCR 측정기",                            "url": "https://disziplin1.github.io/TJT_/TRUNNION/PCR_/PCR_.glb",                           "cameraOrbit": "45deg 70deg 80%"  },
        ]
    },

    "GAUGE_": {
        "title": "게이지 (GAUGE)",
        "mode": "rotate",
        "models": [
            { "name": "C형 스냅게이지",  "url": "https://disziplin1.github.io/TJT_/GAUGE_/C_SNAP_GAUGE/C_SNAP_GAUGE.glb" },
            { "name": "장착거리 게이지", "url": "https://disziplin1.github.io/TJT_/GAUGE_/Distance_Gauge/Distance_Gauge.glb" },
            { "name": "홈경 스냅 게이지","url": "https://disziplin1.github.io/TJT_/GAUGE_/Groove_Snap_Gauge/Groove_Snap_Gauge.glb" },
            { "name": "홈폭 스냅 게이지","url": "https://disziplin1.github.io/TJT_/GAUGE_/Groove_Width/Groove_Width.glb" },
            { "name": "플러그 게이지",   "url": "https://disziplin1.github.io/TJT_/GAUGE_/Plug_Gauge/Plug_Gauge.glb" },
            { "name": "일반 스냅게이지", "url": "https://disziplin1.github.io/TJT_/GAUGE_/SNAP_GAUGE/SNAP_GAUGE.glb" },
            { "name": "폭 게이지",       "url": "https://disziplin1.github.io/TJT_/GAUGE_/Width_Gauge/Width_Gauge.glb" },
        ]
    },
}

# ── 애니메이션 플레이리스트 템플릿 ─────────────────────────────
def make_anim_html(title, models):
    model_list_js = ",\n        ".join(
        f'{{ name: "{m["name"]}", url: "{m["url"]}", cameraOrbit: "{m["cameraOrbit"]}" }}'
        for m in models
    )
    count = len(models)
    return f"""<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <script
      type="module"
      src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"
    ></script>
    <style>
      html, body {{
        margin: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        background-color: #f5f5f5;
        font-family: sans-serif;
      }}

      .viewer-wrapper {{
        width: 100vw;
        height: 100vh;
        position: relative;
      }}

      model-viewer {{
        width: 100%;
        height: 100%;
        display: block;
      }}

      #modelName {{
        position: absolute;
        top: 50px;
        left: 50px;
        z-index: 20;
        font-size: 3rem;
        font-weight: bold;
        padding: 10px 20px;
        background-color: rgba(50, 50, 50, 0.5);
        color: white;
        border-radius: 8px;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        right: 50px;
        z-index: 20;
        width: 200px;
        height: auto;
      }}

      /* ── 컨트롤 토글 버튼 (항상 표시) ── */
      .ctrl-toggle {{
        position: absolute;
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
      }}
      .ctrl-toggle.active {{ background: rgba(182,95,207,.85); }}

      .controls {{
        position: absolute;
        bottom: 12px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 8px;
        border-radius: 10px;
        text-align: center;
        z-index: 10;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s;
      }}
      .controls.show {{ opacity: 1; pointer-events: auto; }}

      .button-row {{
        display: flex;
        justify-content: center;
        gap: 12px;
        margin-bottom: 6px;
      }}

      .controls button {{
        font-size: 1em;
        padding: 0.4em 1em;
        border: none;
        border-radius: 6px;
        background-color: #f5f5f5;
        cursor: pointer;
      }}

      .controls input[type="range"] {{ width: 100%; }}
      .timecode {{ font-size: 0.9em; color: #333; margin-top: 4px; }}

      .zoom-slider {{
        position: absolute;
        left: 20px;
        top: 50%;
        transform: translateY(-50%) rotate(-90deg);
        z-index: 15;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s;
        display: flex;
        align-items: center;
        gap: 10px;
      }}
      .zoom-slider.show {{ opacity: 1; pointer-events: auto; }}

      .zoom-slider label {{
        transform: rotate(90deg);
        color: #333;
        font-size: 14px;
        font-weight: bold;
      }}

      .zoom-slider input[type="range"] {{
        width: 150px;
      }}
    </style>
  </head>

  <body>
    <div class="viewer-wrapper">
      <model-viewer
        id="viewer"
        src=""
        camera-controls
        disable-zoom
        autoplay
        shadow-intensity="0.8"
        exposure="0.9"
        environment-image="neutral"
        interaction-prompt="none"
        camera-orbit="0deg 90deg 100%"
        field-of-view="25deg"
      >
      </model-viewer>

      <div id="modelName">제품명</div>
      <img
        src="https://tjteng.co.kr/images/tjteng.png"
        alt="TJT 로고"
        class="logo"
      />

      <button id="ctrlToggle" class="ctrl-toggle" title="컨트롤 표시/숨기기">⏵</button>

      <div class="zoom-slider">
        <label for="zoomSlider">Zoom</label>
        <input type="range" id="zoomSlider" min="0" max="100" value="10" />
      </div>

      <div class="controls">
        <div class="button-row">
          <button class="nav-button" id="prevBtn">◀</button>
          <button id="toggleBtn">❚❚ 정지</button>
          <button class="nav-button" id="nextBtn">▶</button>
        </div>
        <input
          type="range"
          id="seekBar"
          min="0"
          max="1"
          step="0.001"
          value="0"
        />
        <div class="timecode" id="timeDisplay">00:00 / 00:00</div>
      </div>
    </div>

    <script>
      const viewer       = document.getElementById('viewer');
      const zoomSlider   = document.getElementById('zoomSlider');
      const modelNameBox = document.getElementById('modelName');
      const seekBar      = document.getElementById('seekBar');
      const timeDisplay  = document.getElementById('timeDisplay');
      const toggleBtn    = document.getElementById('toggleBtn');
      const prevBtn      = document.getElementById('prevBtn');
      const nextBtn      = document.getElementById('nextBtn');

      const modelList = [
        {model_list_js}
      ];

      const PAUSE_BETWEEN = 1000;
      let currentIndex = 0;
      let isPlaying    = true;
      let rafId        = null;
      let pendingNext  = null;
      let loadGen      = 0;

      function cancelAll() {{
        if (rafId)       {{ cancelAnimationFrame(rafId); rafId = null; }}
        if (pendingNext) {{ clearTimeout(pendingNext);   pendingNext = null; }}
      }}

      function formatTime(s) {{
        const m = Math.floor(s / 60);
        return `${{String(m).padStart(2,'0')}}:${{String(Math.floor(s % 60)).padStart(2,'0')}}`;
      }}

      function tick() {{
        if (viewer.duration) {{
          seekBar.value = viewer.currentTime / viewer.duration;
          timeDisplay.textContent =
            `${{formatTime(viewer.currentTime)}} / ${{formatTime(viewer.duration)}}`;

          if (isPlaying && viewer.currentTime >= viewer.duration - 0.05) {{
            cancelAll();
            viewer.pause();
            pendingNext = setTimeout(() => {{
              pendingNext  = null;
              currentIndex = (currentIndex + 1) % modelList.length;
              playModel(currentIndex);
            }}, PAUSE_BETWEEN);
            return;
          }}
        }}
        rafId = requestAnimationFrame(tick);
      }}

      zoomSlider.addEventListener('input', () => {{
        viewer.setAttribute('camera-orbit',
          `0deg 90deg ${{110 - parseInt(zoomSlider.value)}}%`);
      }});

      seekBar.addEventListener('input', () => {{
        if (!viewer.duration) return;
        cancelAll();
        viewer.currentTime = parseFloat(seekBar.value) * viewer.duration;
        if (isPlaying) {{
          viewer.play();
          rafId = requestAnimationFrame(tick);
        }}
      }});

      toggleBtn.addEventListener('click', () => {{
        if (isPlaying) {{
          cancelAll();
          viewer.pause();
          toggleBtn.textContent = '▶ 재생';
        }} else {{
          viewer.play();
          toggleBtn.textContent = '❚❚ 정지';
          rafId = requestAnimationFrame(tick);
        }}
        isPlaying = !isPlaying;
      }});

      function playModel(index) {{
        cancelAll();
        const gen   = ++loadGen;
        const model = modelList[index];

        viewer.src               = model.url;
        modelNameBox.textContent = model.name;
        isPlaying                = true;
        toggleBtn.textContent    = '❚❚ 정지';

        viewer.addEventListener('load', () => {{
          if (gen !== loadGen) return;
          viewer.setAttribute('camera-orbit', model.cameraOrbit || '0deg 90deg 100%');
          viewer.currentTime = 0;
          viewer.play();
          rafId = requestAnimationFrame(tick);
        }}, {{ once: true }});
      }}

      prevBtn.addEventListener('click', () => {{
        currentIndex = (currentIndex - 1 + modelList.length) % modelList.length;
        playModel(currentIndex);
      }});

      nextBtn.addEventListener('click', () => {{
        currentIndex = (currentIndex + 1) % modelList.length;
        playModel(currentIndex);
      }});

      window.addEventListener('DOMContentLoaded', () => {{
        playModel(currentIndex);

        const ctrlToggle   = document.getElementById('ctrlToggle');
        const controlsEl   = document.querySelector('.controls');
        const zoomSliderEl = document.querySelector('.zoom-slider');

        function setControls(show) {{
          controlsEl.classList.toggle('show', show);
          zoomSliderEl.classList.toggle('show', show);
          ctrlToggle.classList.toggle('active', show);
          ctrlToggle.textContent = show ? '✕' : '⏵';
        }}

        ctrlToggle.addEventListener('click', () => {{
          setControls(!controlsEl.classList.contains('show'));
        }});

        if (window.matchMedia('(hover: none) and (pointer: coarse)').matches) {{
          setControls(true);
        }}
      }});
    </script>
  </body>
</html>
""".replace("{model_list_js}", model_list_js)

# ── 자동회전 플레이리스트 템플릿 (GAUGE_) ────────────────────
def make_rotate_html(title, models):
    model_list_js = ",\n        ".join(
        f'{{ name: "{m["name"]}", url: "{m["url"]}" }}'
        for m in models
    )
    count = len(models)
    return f"""<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <script
      type="module"
      src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"
    ></script>
    <style>
      html, body {{
        margin: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        background-color: #f5f5f5;
        font-family: sans-serif;
      }}

      .viewer-wrapper {{
        width: 100vw;
        height: 100vh;
        position: relative;
      }}

      model-viewer {{
        width: 100%;
        height: 100%;
        display: block;
      }}

      #modelName {{
        position: absolute;
        top: 50px;
        left: 50px;
        z-index: 20;
        font-size: 3rem;
        font-weight: bold;
        padding: 10px 20px;
        background-color: rgba(50, 50, 50, 0.5);
        color: white;
        border-radius: 8px;
      }}

      .logo {{
        position: absolute;
        top: 40px;
        right: 50px;
        z-index: 20;
        width: 200px;
        height: auto;
      }}

      /* ── 컨트롤 토글 버튼 ── */
      .ctrl-toggle {{
        position: absolute;
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
      }}
      .ctrl-toggle.active {{ background: rgba(182,95,207,.85); }}

      .controls {{
        position: absolute;
        bottom: 12px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 8px;
        border-radius: 10px;
        text-align: center;
        z-index: 10;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s;
      }}
      .controls.show {{ opacity: 1; pointer-events: auto; }}

      .button-row {{
        display: flex;
        justify-content: center;
        gap: 12px;
        margin-bottom: 6px;
      }}

      .controls button {{
        font-size: 1em;
        padding: 0.4em 1em;
        border: none;
        border-radius: 6px;
        background-color: #f5f5f5;
        cursor: pointer;
      }}

      .progress-bar-wrap {{
        width: 100%;
        height: 6px;
        background: #ddd;
        border-radius: 3px;
        overflow: hidden;
        margin: 6px 0 4px;
      }}
      .progress-bar {{
        height: 100%;
        background: #b65fcf;
        border-radius: 3px;
        width: 0%;
        transition: width 0.1s linear;
      }}

      .timecode {{ font-size: 0.9em; color: #333; margin-top: 2px; }}
    </style>
  </head>

  <body>
    <div class="viewer-wrapper">
      <model-viewer
        id="viewer"
        src=""
        camera-controls
        auto-rotate
        rotation-per-second="-15deg"
        auto-rotate-delay="0"
        shadow-intensity="0.8"
        exposure="0.9"
        environment-image="neutral"
        interaction-prompt="none"
      >
      </model-viewer>

      <div id="modelName">제품명</div>
      <img
        src="https://tjteng.co.kr/images/tjteng.png"
        alt="TJT 로고"
        class="logo"
      />

      <button id="ctrlToggle" class="ctrl-toggle" title="컨트롤 표시/숨기기">⏵</button>

      <div class="controls">
        <div class="button-row">
          <button id="prevBtn">◀</button>
          <button id="toggleBtn">❚❚ 정지</button>
          <button id="nextBtn">▶</button>
        </div>
        <div class="progress-bar-wrap">
          <div class="progress-bar" id="progressBar"></div>
        </div>
        <div class="timecode" id="timeDisplay">1 / {count}</div>
      </div>
    </div>

    <script>
      const viewer       = document.getElementById('viewer');
      const modelNameBox = document.getElementById('modelName');
      const toggleBtn    = document.getElementById('toggleBtn');
      const prevBtn      = document.getElementById('prevBtn');
      const nextBtn      = document.getElementById('nextBtn');
      const progressBar  = document.getElementById('progressBar');
      const timeDisplay  = document.getElementById('timeDisplay');

      const modelList = [
        {model_list_js}
      ];

      const DISPLAY_MS  = 8000;   // 모델 1개 표시 시간 (ms)
      let currentIndex  = 0;
      let isPlaying     = true;
      let startTime     = null;
      let rafId         = null;
      let loadGen       = 0;

      function cancelAll() {{
        if (rafId) {{ cancelAnimationFrame(rafId); rafId = null; }}
      }}

      function tick(ts) {{
        if (!isPlaying || startTime === null) return;
        const elapsed = ts - startTime;
        const pct = Math.min(elapsed / DISPLAY_MS * 100, 100);
        progressBar.style.width = pct + '%';
        if (elapsed >= DISPLAY_MS) {{
          currentIndex = (currentIndex + 1) % modelList.length;
          loadModel(currentIndex);
          return;
        }}
        rafId = requestAnimationFrame(tick);
      }}

      function loadModel(index) {{
        cancelAll();
        const gen   = ++loadGen;
        const model = modelList[index];

        viewer.src               = model.url;
        modelNameBox.textContent = model.name;
        timeDisplay.textContent  = (index + 1) + ' / ' + modelList.length;
        progressBar.style.width  = '0%';

        viewer.addEventListener('load', () => {{
          if (gen !== loadGen) return;
          startTime = null;
          rafId = requestAnimationFrame(ts => {{
            startTime = ts;
            tick(ts);
          }});
        }}, {{ once: true }});
      }}

      toggleBtn.addEventListener('click', () => {{
        if (isPlaying) {{
          cancelAll();
          isPlaying = false;
          toggleBtn.textContent = '▶ 재생';
          viewer.autoRotate = false;
        }} else {{
          isPlaying = true;
          viewer.autoRotate = true;
          toggleBtn.textContent = '❚❚ 정지';
          startTime = null;
          rafId = requestAnimationFrame(ts => {{ startTime = ts; tick(ts); }});
        }}
      }});

      prevBtn.addEventListener('click', () => {{
        currentIndex = (currentIndex - 1 + modelList.length) % modelList.length;
        loadModel(currentIndex);
      }});

      nextBtn.addEventListener('click', () => {{
        currentIndex = (currentIndex + 1) % modelList.length;
        loadModel(currentIndex);
      }});

      window.addEventListener('DOMContentLoaded', () => {{
        loadModel(currentIndex);

        const ctrlToggle = document.getElementById('ctrlToggle');
        const controlsEl = document.querySelector('.controls');

        function setControls(show) {{
          controlsEl.classList.toggle('show', show);
          ctrlToggle.classList.toggle('active', show);
          ctrlToggle.textContent = show ? '✕' : '⏵';
        }}

        ctrlToggle.addEventListener('click', () => {{
          setControls(!controlsEl.classList.contains('show'));
        }});

        if (window.matchMedia('(hover: none) and (pointer: coarse)').matches) {{
          setControls(true);
        }}
      }});
    </script>
  </body>
</html>
""".replace("{model_list_js}", model_list_js)

# ── 파일 생성 ───────────────────────────────────────────────────
for cat_key, cat_data in CATEGORIES.items():
    out_path = os.path.join(REPO, cat_key, 'index.html')
    if cat_data["mode"] == "anim":
        html = make_anim_html(cat_data["title"], cat_data["models"])
    else:
        html = make_rotate_html(cat_data["title"], cat_data["models"])
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'[OK] {out_path}')

print('\n완료!')
