<div align="center">

<!-- Terminal Window Header -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0d1117&height=60&section=header"/>

<table>
<tr>
<td width="100%" align="left" style="border: none;">

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  🔴 🟡 🟢   rishi@github:~/profile                                                    ─ □ x  │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
```

</td>
</tr>
</table>

<!-- Animated Typing with Cursor -->
<a href="https://github.com/rishi-sangare">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=00D4FF&center=true&vCenter=true&multiline=true&repeat=true&width=700&height=100&lines=%24+echo+%22Welcome+to+my+terminal%22;%24+./init_profile.sh" alt="Typing SVG" />
</a>

<br/>

<a href="https://github.com/rishi-sangare">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&duration=2000&pause=3000&color=3FB950&center=true&vCenter=true&repeat=true&width=500&height=30&lines=%E2%96%88+System+initialized.+Loading+modules..." alt="Typing SVG" />
</a>

<br/><br/>

<!-- Social Badges -->
[![LinkedIn](https://img.shields.io/badge/-%40rishi--sangare-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/)
[![HuggingFace](https://img.shields.io/badge/-Rishi--19-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/Rishi-19)
[![Gmail](https://img.shields.io/badge/-sangarerishi-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sangarerishi@gmail.com)
[![GitHub](https://img.shields.io/badge/-rishi--sangare-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

</div>

---

<img src="https://img.shields.io/badge/rishi%40github%3A~%24-whoami-00D4FF?style=for-the-badge&labelColor=0d1117&color=00D4FF"/>

```yaml
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   Name           Rishi Sangare                                              │
│   Role           Backend & LLM Systems Engineer                             │
│   Location       Mumbai, India                                              │
│   Education      MBATech (CS + Finance) @ NMIMS | 2021-2026                │
│                                                                             │
│   Focus          ▸ Production LLM Systems                                   │
│                  ▸ Search Infrastructure                                    │
│                  ▸ Cloud Architecture                                       │
│                  ▸ API Pipeline Design                                      │
│                                                                             │
│   Philosophy     "Treat LLMs as unreliable. Add guardrails. Validate."     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<img src="https://img.shields.io/badge/rishi%40github%3A~%24-cat%20tech__stack.json-3FB950?style=for-the-badge&labelColor=0d1117"/>

```json
{
  "languages": {
    "primary": ["Python", "SQL"],
    "secondary": ["Java", "JavaScript", "C++"]
  },
  "backend": {
    "frameworks": ["FastAPI", "Flask"],
    "patterns": ["REST APIs", "Async Pipelines", "Event-Driven"]
  },
  "cloud": {
    "aws": ["ECS", "ECR", "Lambda", "API Gateway", "CDK", "CloudWatch"],
    "containers": ["Docker", "Docker Compose"],
    "other": ["Linode", "RunPod"]
  },
  "search": {
    "engines": ["Elasticsearch", "OpenSearch"],
    "techniques": ["Hybrid RAG", "BM25", "Vector Search", "Re-ranking"]
  },
  "ai_ml": {
    "apis": ["OpenAI", "Claude", "Gemini"],
    "local": ["Fine-tuning", "Transformers", "Mistral-7B"]
  },
  "devops": {
    "ci_cd": ["GitHub Actions", "Blue-Green Deployment"],
    "monitoring": ["CloudWatch", "Slack Alerts", "Dozzle"]
  }
}
```

---

<img src="https://img.shields.io/badge/rishi%40github%3A~%24-ls%20--la%20projects%2F-F778BA?style=for-the-badge&labelColor=0d1117"/>

```
total 5
drwxr-xr-x   recruiter-copilot    4.0K   production   LLM + Search Pipeline
drwxr-xr-x   hybrid-rag           3.2K   production   RAG Architecture
drwxr-xr-x   cloud-infra          2.8K   production   AWS + Linode CI/CD
drwxr-xr-x   chrome-extension     2.1K   production   LinkedIn Data Pipeline
drwxr-xr-x   llm-from-scratch     1.5K   learning     Transformer Implementation
```

---

<img src="https://img.shields.io/badge/▸-recruiter--copilot-00D4FF?style=flat-square&labelColor=0d1117"/>

**Production LLM + Search Pipeline** — Evaluates 40+ candidates per job description

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#00d4ff', 'edgeLabelBackground':'#0d1117', 'tertiaryColor': '#161b22', 'lineColor': '#3fb950', 'textColor': '#c9d1d9'}}}%%
flowchart LR
    A[📄 Job Description] --> B[🔍 Feature Extraction]
    B --> C[⚡ Query Generation]
    C --> D[(OpenSearch)]
    D --> E[👥 Candidate Pool]
    E --> F[🤖 LLM Evaluation]
    F --> G[📊 Ranked Results]
    
    style A fill:#1f6feb,stroke:#00d4ff
    style D fill:#238636,stroke:#3fb950
    style F fill:#8957e5,stroke:#bc8cff
    style G fill:#da3633,stroke:#f85149
```

| Metric | Before | After |
|:-------|:------:|:-----:|
| **Latency** | `2.5 min` | `40 sec` |
| **Tokens/Batch** | — | `~80,000` |
| **Candidates** | — | `~40/request` |

---

<img src="https://img.shields.io/badge/▸-hybrid--rag-3FB950?style=flat-square&labelColor=0d1117"/>

**Retrieval Augmented Generation** — BM25 + Vector dual retrieval

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#3fb950', 'tertiaryColor': '#161b22', 'lineColor': '#00d4ff'}}}%%
flowchart LR
    Q[🔎 Query] --> T[Transform]
    T --> B[BM25<br/>Lexical]
    T --> V[Vector<br/>Semantic]
    B --> M[🔀 Merge]
    V --> M
    M --> R[Re-rank]
    R --> C[📝 Context]
    C --> L[🤖 LLM]
    
    style B fill:#1f6feb,stroke:#00d4ff
    style V fill:#8957e5,stroke:#bc8cff
    style M fill:#238636,stroke:#3fb950
    style L fill:#da3633,stroke:#f85149
```

```
✓ Deterministic Retrieval    ✓ Bounded Context    ✓ Testable    ✓ Anti-Hallucination
```

---

<img src="https://img.shields.io/badge/▸-cloud--infra-F778BA?style=flat-square&labelColor=0d1117"/>

**AWS + Linode Deployment** — Blue-Green CI/CD with zero downtime

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#f778ba', 'tertiaryColor': '#161b22', 'lineColor': '#00d4ff'}}}%%
flowchart LR
    subgraph AWS ["☁️ AWS Stack"]
        A1[GitHub] --> A2[Actions]
        A2 --> A3[ECR]
        A3 --> A4[ECS Fargate]
    end
    
    subgraph LIN ["🖥️ Linode Stack"]
        L1[GitHub] --> L2[Actions]
        L2 --> L3[🔵 Blue]
        L2 --> L4[🟢 Green]
    end
    
    style A4 fill:#ff7b00,stroke:#ffa657
    style L3 fill:#1f6feb,stroke:#00d4ff
    style L4 fill:#238636,stroke:#3fb950
```

| Environment | Stack |
|:------------|:------|
| **AWS** | ECS + ECR + CDK + API Gateway |
| **Linode** | Blue-Green + Health Checks + Rollback |

---

<img src="https://img.shields.io/badge/▸-chrome--extension-FFA657?style=flat-square&labelColor=0d1117"/>

**LinkedIn Data Pipeline** — Production tool for recruiters

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#ffa657', 'tertiaryColor': '#161b22', 'lineColor': '#3fb950'}}}%%
sequenceDiagram
    participant E as 🔌 Extension
    participant L as 💼 LinkedIn
    participant A as ⚡ Lambda
    participant D as 🗄️ DynamoDB
    
    E->>L: Extract Profile
    E->>A: POST /candidate
    A->>D: Upsert Record
    A->>E: Structured Response
```

| Production Stats | |
|:-----------------|:--|
| Daily API Hits | `~70-80` |
| Active Users | Sachi (Japan) |
| Uptime | `99.9%` |

---

<img src="https://img.shields.io/badge/▸-llm--from--scratch-FFD93D?style=flat-square&labelColor=0d1117"/>

**Transformer Implementation** — Following *Attention Is All You Need*

```
┌─────────────────────────────────────────────────────────────┐
│                    TRANSFORMER BLOCK                        │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Multi-Head Self-Attention                │  │
│  │         Q ──┐                                         │  │
│  │         K ──┼──► Scaled Dot-Product ──► Concat        │  │
│  │         V ──┘                                         │  │
│  └───────────────────────────────────────────────────────┘  │
│                           │                                 │
│                      Add & Norm                             │
│                           │                                 │
│  ┌───────────────────────────────────────────────────────┐  │
│  │               Feed Forward Network                    │  │
│  └───────────────────────────────────────────────────────┘  │
│                           │                                 │
│                      Add & Norm                             │
└─────────────────────────────────────────────────────────────┘

Outcome: Understanding why LLM failures are system-level, not model-level.
```

---

<img src="https://img.shields.io/badge/rishi%40github%3A~%24-git%20log%20--oneline%20experience-8957E5?style=for-the-badge&labelColor=0d1117"/>

```diff
+ Feb 2025   LD Technologies ─────────────── Backend & LLM Systems Engineer
             │ FastAPI • AWS CDK • OpenSearch • LLM Pipelines • Chrome Extension

  Jul 2024   Splan Infocom ──────────────── Backend API Developer
             │ Invoice Processing • OpenAI API • AWS EC2

  Jun 2024   Paragon Dynamics ───────────── Backend Intern
             │ Logistics Chatbot • Ledger Reconciliation

  Dec 2023   Mitwa.ai ───────────────────── Founding Engineer
             │ MERN Stack • LLM Fine-tuning (Mistral-7B) • RunPod
```

---

<img src="https://img.shields.io/badge/rishi%40github%3A~%24-cat%20education.txt-DA3633?style=for-the-badge&labelColor=0d1117"/>

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  NMIMS Mumbai                                                             ║
║  ├── Degree     MBATech (Computer Engineering + Finance)                  ║
║  ├── Duration   2021 - 2026                                               ║
║  ├── GPA        3.09 / 4.00                                               ║
║  └── Courses    DSA • ML • AI • DBMS • Financial Planning • Tech Mgmt    ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  Certifications                                                           ║
║  ├── Generative AI with LLMs ──────── DeepLearning.AI & AWS              ║
║  └── Advanced Data Science & AI ───── IIT Madras                         ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

<div align="center">

<img src="https://img.shields.io/badge/rishi%40github%3A~%24-neofetch-00D4FF?style=for-the-badge&labelColor=0d1117"/>

<br/><br/>

<!-- GitHub Stats with Private Contributions -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=rishi-sangare&show_icons=true&count_private=true&include_all_commits=true&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=00d4ff&icon_color=3fb950&text_color=c9d1d9"/>
  <img src="https://github-readme-stats.vercel.app/api?username=rishi-sangare&show_icons=true&count_private=true&include_all_commits=true&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=00d4ff&icon_color=3fb950&text_color=c9d1d9" height="165"/>
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=rishi-sangare&theme=github-dark-blue&hide_border=true&background=0D1117&ring=00D4FF&fire=3FB950&currStreakLabel=00D4FF"/>
  <img src="https://streak-stats.demolab.com?user=rishi-sangare&theme=github-dark-blue&hide_border=true&background=0D1117&ring=00D4FF&fire=3FB950&currStreakLabel=00D4FF" height="165"/>
</picture>

<br/><br/>

<!-- Activity Graph -->
<img src="https://github-readme-activity-graph.vercel.app/graph?username=rishi-sangare&theme=github-compact&hide_border=true&bg_color=0d1117&color=00d4ff&line=3fb950&point=f778ba" width="100%"/>

</div>

---

<img src="https://img.shields.io/badge/rishi%40github%3A~%24-cat%20README.txt-6E7681?style=for-the-badge&labelColor=0d1117"/>

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Some repositories contain architecture documentation only.                │
│  Client source code not shared due to IP policies.                         │
│  System designs and decisions are real + production-tested.                │
│                                                                             │
│  Happy to discuss tradeoffs and implementation details.                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<div align="center">

<a href="https://github.com/rishi-sangare">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=16&duration=2000&pause=5000&color=6E7681&center=true&vCenter=true&repeat=true&width=400&height=25&lines=rishi%40github%3A~%24+exit;Connection+closed.+%E2%96%88" alt="Typing SVG" />
</a>

<br/><br/>

```
└──────────────────────────────────────────────────────────────────────────────────────────────┘
```

</div>
