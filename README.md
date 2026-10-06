<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img alt="Rishi Sangare, AI / LLM Systems Engineer. I ship LLM products to production, and prove they work." src="assets/hero-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://www.linkedin.com/in/rishi-sangare"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-rishi--sangare-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a href="https://huggingface.co/Rishi-19"><img alt="Hugging Face" src="https://img.shields.io/badge/Hugging%20Face-Rishi--19-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"></a>
  <a href="mailto:sangarerishi@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-sangarerishi%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://github.com/rishi-sangare/case-studies"><img alt="Case studies" src="https://img.shields.io/badge/Read-Case%20studies-8957e5?style=for-the-badge&logo=readthedocs&logoColor=white"></a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stats-dark.svg">
  <img alt="372 pull requests authored, 253K+ CRM records migrated, recall@10 0.19 to 0.57, 24-model LLM bake-off, 4 production AI products" src="assets/stats-light.svg" width="100%">
</picture>

### What I do

I build **production LLM systems end to end** at [LD Technologies](https://github.com/Saachi-AI) (since Feb 2025): retrieval, orchestration, evals, security and the infra that keeps them up. My clients include a large Japanese recruiting database platform and a UK recruitment CRM, and I ship our own SaaS products.

- **LLM products, not demos.** Multi-turn LLM flows, multi-provider fallbacks, structured output that survives bad model responses.
- **Search and evals.** Elasticsearch relevance, golden sets, recall@k, LLM-as-judge, bias probes. I measure before I claim.
- **Ownership.** CI/CD with rollback, Slack alerting, security hardening, and incident response when things break.
- **AI-native speed.** I run coding agents (Claude Code, MCP, browser automation) as a daily force multiplier, with guardrails.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/pipeline-dark.svg">
  <img alt="Production pipeline: request, clarify (3-turn LLM), retrieve (Elasticsearch, recall@10 0.19 to 0.57), evaluate (parallel LLM judges), deliver (HMAC webhook), all driven by an eval harness" src="assets/pipeline-light.svg" width="100%">
</picture>

### Featured work

<table>
<tr>
<td width="50%"><a href="https://github.com/rishi-sangare/case-studies/blob/main/refinecv.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-refinecv-dark.svg"><img alt="RefineCV: B2B CV-formatting SaaS" src="assets/card-refinecv-light.svg" width="100%"></picture></a></td>
<td width="50%"><a href="https://github.com/rishi-sangare/case-studies/blob/main/recruiter-copilot.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-copilot-dark.svg"><img alt="Recruiter Copilot: AI candidate scoring Chrome extension" src="assets/card-copilot-light.svg" width="100%"></picture></a></td>
</tr>
<tr>
<td width="50%"><a href="https://github.com/rishi-sangare/case-studies/blob/main/crm-migration.md"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-migration-dark.svg"><img alt="CRM migration: 18 GB SQL Server to REST-only CRM" src="assets/card-migration-light.svg" width="100%"></picture></a></td>
<td width="50%"><a href="https://github.com/rishi-sangare/cosmeon-fs-lite"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-cosmeon-dark.svg"><img alt="COSMEON FS-LITE: orbital file system simulator" src="assets/card-cosmeon-light.svg" width="100%"></picture></a></td>
</tr>
</table>

<p align="center"><sub>Most of my work is in private client repos. The <a href="https://github.com/rishi-sangare/case-studies">case studies</a> explain the architecture, the decisions and the measured results, without client code.</sub></p>

### Open source

- **keras-team/keras** · [#22407](https://github.com/keras-team/keras/pull/22407) (merged): implemented `numpy.view` for the OpenVINO backend.
- **Hugging Face** · [Rishi-19](https://huggingface.co/Rishi-19): Mistral-7B fine-tunes (including DPO on 6k and 18k-example datasets) for an AI wellbeing companion, plus a DistilBERT profanity classifier.
- **Smart India Hackathon** 2024 and 2025: sign-language detection; a document-processing platform for Kochi Metro (FastAPI, MinIO, Postgres, Gemini).

### Toolbox

<p align="center">
  <img alt="Python, FastAPI, TypeScript, React, Next.js, Node.js, Postgres, Supabase, Elasticsearch, Docker, AWS, GitHub Actions, Cloudflare, Tailwind, Astro, PyTorch, Linux" src="https://skillicons.dev/icons?i=py,fastapi,ts,react,nextjs,nodejs,postgres,supabase,elasticsearch,docker,aws,githubactions,cloudflare,tailwind,astro,pytorch,linux&perline=9">
</p>

<p align="center"><sub>Also: Cerebras · OpenRouter · Bedrock · Claude · OpenAI · Gemini · MCP · n8n · Playwright · pytest · Vitest · WeasyPrint · Chrome MV3 · MLX</sub></p>

### Contribution graph, in 3D

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="profile-3d-contrib/profile-night-rainbow.svg">
  <img alt="3D contribution calendar" src="profile-3d-contrib/profile-green-animate.svg" width="100%">
</picture>

<details>
<summary><b>More projects</b></summary>
<br>

| Project | What it is | Stack |
|---|---|---|
| Tamago AI services | LLM candidate ↔ job matching for a Japanese recruiting database: 3-turn pre-screening, ES retrieval, eval harness | FastAPI · Elasticsearch · Cerebras · Supabase |
| Hybrid search ingestion | BM25 + vector search over job descriptions on AWS OpenSearch, switchable LLM extraction | FastAPI · OpenSearch · AWS CDK |
| LinkedIn → ATS extension | Recruiter tool syncing LinkedIn profiles into a client ATS | Chrome · Lambda · DynamoDB |
| Revenue Rail | Self-hosted n8n replacing Zapier: Stripe → Thinkific → Slack, duplicate-safe, 11/11 failure scenarios pass | n8n · Postgres · Docker |
| Signal Lab | Privacy-first Meta Conversions API relay with Apple AdAttributionKit JWS verification | Next.js · TypeScript |
| AI Video Studio | Agent-operated video pipeline with on-device ASR/TTS and automated QA gates | Python · MLX · Remotion |
| Consistency Check | Does an LLM answer the same in English, Hindi and Hinglish? | FastAPI · Ollama · Claude |
| [My_LLM](https://github.com/rishi-sangare/My_LLM) | A transformer from scratch | Python |

</details>

<details>
<summary><b>How I work</b></summary>
<br>

1. **Plan in public.** A short design doc or diagram before code, and plain-English explainers for non-engineers.
2. **Measure, then claim.** Golden sets and holdouts. When I caught my own +30% reranker result inflated, I reported the honest +12.9%.
3. **Guardrails on everything.** Staging-first releases, idempotent writes, LLM output validation, spend caps.
4. **Treat LLMs as unreliable components.** Validate, fall back, alert.

</details>

<p align="center"><br><b>Open to full-time remote roles</b> · AI / LLM engineering · search & relevance · applied AI<br><sub>Based in Mumbai (IST) · comfortable working US hours · <a href="mailto:sangarerishi@gmail.com">sangarerishi@gmail.com</a></sub></p>
