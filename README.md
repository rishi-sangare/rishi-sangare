```
┌──────────────────────────────────────────────────────────────────────────────┐
│  ●  ●  ●   rishi@github:~/profile                                            │
└──────────────────────────────────────────────────────────────────────────────┘
```

<div align="center">
  
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=00D4FF&center=true&vCenter=true&width=600&lines=Welcome+to+my+terminal.;Backend+%26+LLM+Systems+Engineer;Building+production-grade+AI+systems.)](https://git.io/typing-svg)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/Rishi-19)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:sangarerishi@gmail.com)

</div>

---

### `rishi@github:~$` whoami

```yaml
Name:      Rishi Sangare
Role:      Backend & LLM Systems Engineer
Location:  Mumbai, India
Education: MBATech (CS + Finance) @ NMIMS | 2021-2026

Focus:
  - Production LLM Systems
  - Search Infrastructure (Elasticsearch, OpenSearch)
  - Cloud Architecture (AWS, Linode)
  - API Pipeline Design

Philosophy: "Treat LLMs as unreliable. Add guardrails. Validate everything."
```

---

### `rishi@github:~$` cat tech_stack.json

```json
{
  "languages": ["Python", "Java", "JavaScript", "SQL", "C++"],
  "backend": ["FastAPI", "Flask", "REST APIs", "Async Pipelines"],
  "cloud": ["AWS ECS", "ECR", "Lambda", "API Gateway", "CDK", "Docker", "Linode"],
  "search": ["Elasticsearch", "OpenSearch", "Hybrid RAG", "BM25 + Vector"],
  "ai_ml": ["LLM APIs", "OpenAI", "Claude", "Fine-tuning", "Transformers"],
  "devops": ["GitHub Actions", "Blue-Green Deployment", "CloudWatch", "CI/CD"],
  "tools": ["Postman", "APIDog", "Notion", "Slack", "Git"]
}
```

---

### `rishi@github:~$` ls projects/

```
drwxr-xr-x  recruiter-copilot/
drwxr-xr-x  hybrid-rag/
drwxr-xr-x  cloud-infra/
drwxr-xr-x  chrome-extension/
drwxr-xr-x  llm-from-scratch/
```

---

#### `recruiter-copilot/` — LLM + Search Pipeline

Production system evaluating candidates against job descriptions using search + LLM reasoning.

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#00d4ff', 'primaryTextColor': '#fff', 'lineColor': '#3fb950'}}}%%
flowchart LR
    A[Job Description] --> B[Feature Extraction]
    B --> C[Query Generation]
    C --> D[OpenSearch]
    D --> E[Candidate Pool]
    E --> F[LLM Evaluation]
    F --> G[Ranked Results]
```

| Metric | Value |
|--------|-------|
| Latency Reduction | `2.5 min → 40 sec` |
| Tokens per Batch | `~80,000` |
| Candidates Evaluated | `~40 per request` |

---

#### `hybrid-rag/` — Retrieval Augmented Generation

Full RAG system combining lexical (BM25) and semantic (vector) retrieval.

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#3fb950', 'primaryTextColor': '#fff', 'lineColor': '#00d4ff'}}}%%
flowchart LR
    Q[Query] --> T[Transform]
    T --> B[BM25]
    T --> V[Vector]
    B --> M[Merge]
    V --> M
    M --> R[Re-rank]
    R --> C[Context]
    C --> L[LLM]
```

| Design Constraint | Status |
|-------------------|--------|
| Deterministic Retrieval | ✓ |
| Bounded Context | ✓ |
| Testable Outputs | ✓ |
| Anti-Hallucination | ✓ |

---

#### `cloud-infra/` — AWS + Linode CI/CD

Designed deployment architecture across managed (AWS) and self-hosted (Linode) environments.

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#f778ba', 'primaryTextColor': '#fff', 'lineColor': '#00d4ff'}}}%%
flowchart LR
    subgraph AWS
        A1[GitHub] --> A2[Actions] --> A3[ECR] --> A4[ECS]
    end
    subgraph Linode
        L1[GitHub] --> L2[Actions] --> L3[Blue] & L4[Green]
    end
```

| Feature | Implementation |
|---------|---------------|
| AWS | ECS + ECR + CDK (IaC) |
| Linode | Blue-Green + Health Checks |
| Rollback | Automatic on failure |

---

#### `chrome-extension/` — LinkedIn Data Pipeline

Recruiter-facing tool for structured LinkedIn profile extraction.

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#ffa657', 'primaryTextColor': '#fff', 'lineColor': '#3fb950'}}}%%
flowchart LR
    E[Extension] --> L[LinkedIn]
    L --> X[Extract]
    X --> A[Lambda]
    A --> D[DynamoDB]
    D --> R[Client Format]
```

| Metric | Value |
|--------|-------|
| Daily API Hits | `~70-80` |
| Active Users | Recruiters @ Sachi (Japan) |
| Uptime | `99.9%` |

---

#### `llm-from-scratch/` — Transformer Implementation

Built a language model following *Attention Is All You Need*.

```
Components Built:
├── Multi-Head Self-Attention
├── Positional Embeddings  
├── Feed-Forward Networks
├── Training Loop
└── Streamlit Visualization UI

Outcome: Deep understanding of why LLM failures are system-level, not model-level.
```

---

### `rishi@github:~$` git log --oneline experience

```
Feb 2025  LD Technologies ──────────── Backend & LLM Systems Engineer
          │ FastAPI, AWS CDK, OpenSearch, LLM Pipelines
          │ Chrome Extension, CI/CD, Production Systems

Jul 2024  Splan Infocom ────────────── Backend API Developer
          │ Invoice Processing API, OpenAI, AWS EC2

Jun 2024  Paragon Dynamics ─────────── Backend Intern
          │ Logistics Chatbot, Ledger Reconciliation

Dec 2023  Mitwa.ai ─────────────────── Founding Engineer
          │ MERN Stack, LLM Fine-tuning (Mistral-7B), RunPod
```

---

### `rishi@github:~$` cat education.txt

```
NMIMS Mumbai
├── Degree: MBATech (Computer Engineering + Finance)
├── Duration: 2021 - 2026
├── GPA: 3.09 / 4.00
└── Coursework: DSA, ML, AI, DBMS, Financial Planning, Tech Management

Certifications:
├── Generative AI with LLMs — DeepLearning.AI & AWS
└── Advanced Data Science & AI — IIT Madras
```

---

### `rishi@github:~$` cat README.txt

```
Note on Repositories:
├── Some repos contain architecture documentation only
├── Client source code not shared (IP policies)
└── System designs and decisions are real + production-tested

Happy to discuss tradeoffs and implementation details.
```

---

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  rishi@github:~/profile$ exit                                                │
│  Connection closed.                                                          │
└──────────────────────────────────────────────────────────────────────────────┘
```
