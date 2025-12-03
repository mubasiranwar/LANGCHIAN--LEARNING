<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>LangChain Practice — README</title>

  <!-- Google font -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">

  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --muted:#94a3b8;
      --accent:#7c3aed;
      --glass: rgba(255,255,255,0.03);
      --white: #e6eef8;
      --radius: 12px;
      font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }

    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      background: linear-gradient(180deg,#071029 0%, #081226 60%);
      color:var(--white);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      padding:32px;
      display:flex;
      justify-content:center;
      font-size:15px;
      line-height:1.45;
    }

    .container{
      width:100%;
      max-width:1100px;
      background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border-radius:18px;
      padding:28px;
      box-shadow: 0 10px 40px rgba(2,6,23,0.7);
      display:grid;
      grid-template-columns: 1fr 360px;
      gap:20px;
      align-items:start;
    }

    header{
      grid-column:1/-1;
      display:flex;
      justify-content:space-between;
      align-items:center;
      gap:16px;
      margin-bottom:4px;
    }

    .title{
      display:flex;
      gap:16px;
      align-items:center;
    }

    .logo{
      width:52px;
      height:52px;
      border-radius:12px;
      background: linear-gradient(135deg,var(--accent), #2dd4bf);
      display:flex;
      align-items:center;
      justify-content:center;
      font-weight:700;
      color:white;
      font-size:18px;
      box-shadow: 0 6px 18px rgba(124,58,237,0.18), inset 0 -4px 12px rgba(0,0,0,0.18);
    }

    h1{font-size:20px;margin:0}
    p.lead{color:var(--muted);margin:4px 0 0;font-size:13px}

    .left{
      background: linear-gradient(180deg, rgba(255,255,255,0.015), rgba(255,255,255,0.01));
      border-radius:var(--radius);
      padding:20px;
      min-height:420px;
      box-shadow:0 6px 20px rgba(2,6,23,0.5);
    }

    .right{
      background: linear-gradient(180deg, rgba(255,255,255,0.012), rgba(255,255,255,0.008));
      border-radius:var(--radius);
      padding:20px;
      height:100%;
      box-shadow: inset 0 1px 0 rgba(255,255,255,0.01);
    }

    section h2{
      margin:0 0 12px 0;
      font-size:15px;
    }

    .meta{
      display:flex;
      gap:8px;
      flex-wrap:wrap;
      margin-bottom:14px;
    }

    .badge{
      background:var(--glass);
      padding:6px 10px;
      border-radius:999px;
      color:var(--muted);
      font-weight:600;
      font-size:13px;
    }

    pre.tree{
      background: linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.006));
      border-radius:10px;
      padding:14px;
      overflow:auto;
      color:#cfe7ff;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", "Courier New", monospace;
      font-size:13px;
      line-height:1.6;
      border:1px solid rgba(255,255,255,0.02);
    }

    .cmd{
      display:flex;
      gap:8px;
      align-items:center;
      background:rgba(255,255,255,0.02);
      border-radius:10px;
      padding:10px;
      margin:12px 0;
      box-shadow:inset 0 -2px 6px rgba(0,0,0,0.35);
    }

    .cmd code{
      flex:1;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", "Courier New", monospace;
      font-size:13px;
      color: #dff1ff;
      overflow:auto;
    }

    .copy-btn{
      border:0;
      background:linear-gradient(180deg,var(--accent), #5b21b6);
      color:white;
      padding:8px 12px;
      border-radius:8px;
      cursor:pointer;
      font-weight:600;
      font-size:13px;
      transition:transform .12s ease, box-shadow .12s ease;
      box-shadow: 0 6px 18px rgba(124,58,237,0.18);
    }
    .copy-btn:active{transform:translateY(1px)}

    .notes{
      color:var(--muted);
      font-size:13px;
      background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.008));
      border-left:3px solid rgba(124,58,237,0.18);
      padding:12px;
      border-radius:8px;
    }

    .section-block{margin-bottom:20px}

    .right .card{
      background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.008));
      border-radius:10px;
      padding:12px;
      margin-bottom:12px;
      border:1px solid rgba(255,255,255,0.02);
    }

    .footer{
      grid-column:1/-1;
      margin-top:6px;
      display:flex;
      justify-content:space-between;
      align-items:center;
      color:var(--muted);
      font-size:13px;
    }

    a.btn{
      text-decoration:none;
      background:transparent;
      border:1px solid rgba(255,255,255,0.04);
      color:var(--white);
      padding:8px 12px;
      border-radius:8px;
      font-weight:600;
      font-size:13px;
    }

    /* Responsive */
    @media (max-width:980px){
      .container{ grid-template-columns: 1fr; padding:18px; }
      .right{ order:2 }
      .left{ order:1 }
    }
  </style>
</head>
<body>
  <div class="container" role="main">
    <header>
      <div class="title">
        <div class="logo">LC</div>
        <div>
          <h1>LangChain Practice Repository</h1>
          <p class="lead">Hands-on examples: LLMs, Chat Models, Embeddings, ChromaDB, Document Loaders & Agents</p>
        </div>
      </div>
      <div style="text-align:right">
        <div class="badge">Python • LangChain • ChromaDB</div>
        <div style="height:6px"></div>
        <div class="badge">Repo: Practical Demos</div>
      </div>
    </header>

    <main class="left">
      <section class="section-block">
        <h2>About</h2>
        <p class="notes">This repository contains modular examples for learning LangChain end-to-end: LLM initialization, chains, chat models, embeddings, ChromaDB usage, and document loaders. Use this as a study reference or base for RAG/agent projects.</p>
      </section>

      <section class="section-block">
        <h2>Repository Structure</h2>
        <pre class="tree" aria-label="Folder tree">
LANGCHAIN/
├── 1.LLMS/
│   └── llm.py
├── 2.CHATS-MODELS/
│   ├── chain.py
│   ├── chatmodel.py
│   ├── conditional.py
│   └── hugging_face_chatmodel.py
├── 3.EMBIDDING-MODELS/
│   ├── chromaEmbd.py
│   └── query_chroma.py
├── 4.CHOROMADB/
│   └── p1.py
├── 5.Documents_loader/
│   ├── Directory_load.py
│   ├── adden_load.py
│   └── Andrew Ng Deep Learning Notes.pdf
└── .venv/
        </pre>
      </section>

      <section class="section-block">
        <h2>Quick Start</h2>

        <div class="cmd">
          <code>git clone https://github.com/&lt;your-username&gt;/&lt;repo-name&gt;.git
cd &lt;repo-name&gt;</code>
          <button class="copy-btn" data-copy="git clone https://github.com/&lt;your-username&gt;/&lt;repo-name&gt;.git
cd &lt;repo-name&gt;">Copy</button>
        </div>

        <div class="cmd">
          <code>python -m venv .venv
source .venv/bin/activate  # mac / linux
.venv\Scripts\activate     # windows</code>
          <button class="copy-btn" data-copy="python -m venv .venv
source .venv/bin/activate  # mac / linux
.venv\Scripts\activate     # windows">Copy</button>
        </div>

        <div class="cmd">
          <code>pip install -r requirements.txt
# or install langchain, chromadb, etc individually</code>
          <button class="copy-btn" data-copy="pip install -r requirements.txt">Copy</button>
        </div>

        <p style="color:var(--muted);margin-top:10px">Create a <code>.env</code> file with your API keys (OpenRouter, HuggingFace, etc.).</p>
      </section>

      <section class="section-block">
        <h2>Usage Examples</h2>
        <div class="card">
          <strong>Run a chat model demo</strong>
          <div style="height:8px"></div>
          <div class="cmd">
            <code>python 2.CHATS-MODELS/chatmodel.py</code>
            <button class="copy-btn" data-copy="python 2.CHATS-MODELS/chatmodel.py">Copy</button>
          </div>
        </div>

        <div class="card">
          <strong>Load a document directory</strong>
          <div style="height:8px"></div>
          <div class="cmd">
            <code>python 5.Documents_loader/Directory_load.py</code>
            <button class="copy-btn" data-copy="python 5.Documents_loader/Directory_load.py">Copy</button>
          </div>
        </div>

        <div class="card">
          <strong>Query Chroma embeddings</strong>
          <div style="height:8px"></div>
          <div class="cmd">
            <code>python 3.EMBIDDING-MODELS/query_chroma.py</code>
            <button class="copy-btn" data-copy="python 3.EMBIDDING-MODELS/query_chroma.py">Copy</button>
          </div>
        </div>
      </section>

      <section class="section-block">
        <h2>Future Plans</h2>
        <ul style="color:var(--muted);margin:0 0 0 18px">
          <li>Add agentic tool-calling examples (DocDock & tools)</li>
          <li>Complete RAG pipeline with persistent deployment</li>
          <li>Streamlit / FastAPI demo UI for each module</li>
          <li>CI, tests & GitHub Actions for reproducible demos</li>
        </ul>
      </section>
    </main>

    <aside class="right">
      <div class="card">
        <strong>What you'll learn</strong>
        <div style="height:10px"></div>
        <p class="meta">
          <span class="badge">LLMs</span>
          <span class="badge">Chat Models</span>
          <span class="badge">Embeddings</span>
          <span class="badge">ChromaDB</span>
        </p>
        <p style="color:var(--muted);margin:8px 0 0">This repo is structured to teach practical flows commonly used in production RAG systems and agentic pipelines.</p>
      </div>

      <div class="card">
        <strong>Technologies</strong>
        <p style="color:var(--muted);margin:8px 0 0">Python, LangChain, ChromaDB, HuggingFace, OpenRouter, sentence-transformers, dotenv</p>
      </div>

      <div class="card">
        <strong>Helpful Tips</strong>
        <ol style="color:var(--muted);margin:8px 0 0 18px;padding:0">
          <li>Keep your API keys in <code>.env</code>.</li>
          <li>Test each module independently before integrating.</li>
          <li>Use virtual environments to manage dependencies.</li>
        </ol>
      </div>

      <div class="card">
        <strong>Contribute</strong>
        <p style="color:var(--muted);margin:8px 0 0">PRs welcome — open an issue for major changes. Add examples, docs, or tests to improve clarity.</p>
      </div>
    </aside>

    <div class="footer">
      <div>Made with ❤ — LangChain Practice</div>
      <div style="display:flex;gap:8px">
        <a class="btn" href="#" title="Star the repo">⭐ Star</a>
        <a class="btn" href="#" title="Open issues">🐞 Issues</a>
      </div>
    </div>
  </div>

  <script>
    // Copy buttons
    document.querySelectorAll('.copy-btn').forEach(btn=>{
      btn.addEventListener('click', async ()=>{
        const text = btn.getAttribute('data-copy');
        try {
          await navigator.clipboard.writeText(text);
          btn.textContent = 'Copied ✓';
          setTimeout(()=> btn.textContent = 'Copy', 1400);
        } catch(err){
          // fallback
          const ta = document.createElement('textarea');
          ta.value = text;
          document.body.appendChild(ta);
          ta.select();
          document.execCommand('copy');
          ta.remove();
          btn.textContent = 'Copied ✓';
          setTimeout(()=> btn.textContent = 'Copy', 1400);
        }
      });
    });
  </script>
</body>
</html>
