# FinOpsAI

**AI-Native Cloud Cost Intelligence & Optimization**

FinOpsAI platform that helps engineers understand cloud spending, investigate cost anomalies, and identify optimization opportunities using data analytics, Retrieval-Augmented Generation (RAG), and agentic AI.

## Planned Capabilities

- **Cloud Cost Analytics:** Ingest and analyze cloud billing data, starting with AWS, Google Cloud.
- **Cost Anomaly Detection:** Identify unusual spending patterns and cost increases.
- **Cost Optimization:** Recommend opportunities to reduce unnecessary cloud spending.
- **AI Cost Investigation Agent:** Investigate cost anomalies using structured billing data and external tools.
- **RAG-Powered Knowledge Retrieval:** Retrieve cloud pricing documentation, optimization guidance, and historical investigations.
- **AI Evaluation:** Measure investigation accuracy, retrieval quality, latency, and operational cost.

These capabilities are planned and will be implemented progressively.

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| Frontend (planned) | React, TypeScript |
| Database | PostgreSQL |
| Vector Search (planned) | pgvector |
| AI Orchestration (planned) | LangGraph |
| Development Tools | uv, Ruff, pytest |
| Local Infrastructure | Docker Compose |

## Architecture

The planned architecture consists of a React frontend, a FastAPI backend, PostgreSQL for structured billing data, and an AI investigation agent that combines deterministic analytics with knowledge retrieval.

Billing calculations will be performed using structured data rather than relying on LLM-generated numerical estimates.


The project is under active development and is not currently intended for production deployment.

## License

License to be determined.