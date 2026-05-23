TASKMASTER FULL PROJECT PLAN – HMRC SENIOR DATA ANALYST
Project Title: HMRC Preventable Risk Detection Product – ADAS Secondary Crash Analysis
Goal: Build a complete, production-like analytical product (not just a script) that demonstrates senior-level capability from business problem to deployed solution. This will be your star technical presentation for the HMRC interview.

FULL PROJECT PHASES (End-to-End Lifecycle)
Phase 0: Business Requirements & Scoping (Done in README + Presentation)

Define business problem, objectives, stakeholders, success criteria, risks, ethical considerations.
Expected output: Professional README + 1-page scoping document.

Phase 1: Project Setup & Governance

GitHub repo, folder structure, requirements, linting, testing framework.
Expected: Clean, professional repo structure with Makefile, CI workflow.

Phase 2: Data Ingestion & Automation

YouTube metadata extraction (yt-dlp + optional API).
Initial labelling schema (Google Sheet or CSV template).
Expected: Script that can pull 50–100+ video metadata automatically.

Phase 3: Data Model & Labelling Process

Define robust data schema with QA rules.
Create labelling template + instructions.
Expected: Consistent, auditable dataset.

Phase 4: Core Analytics Pipeline

Data loading, cleaning, validation (with pytest).
Risk calculations, segmentation (weather, road type, country).
Expected: Modular, tested Python modules (src/).

Phase 5: Insight Generation & Visualisation

Summary statistics, breakdowns, risk profiles.
Interactive visuals (Plotly).
Expected: Clear, actionable outputs.

Phase 6: Product Delivery Layer

Streamlit interactive dashboard (demo-ready).
One-page briefing / executive summary.
Expected: Professional, user-friendly product.

Phase 7: Testing, Documentation & Reproducibility

Unit tests, data quality checks, documentation.
GitHub Actions for auto-deployment.
Expected: High-quality, maintainable code.

Phase 8: Technical Presentation Package

10–12 minute slide deck + demo script.
Expected: Ready-to-deliver interview presentation.


CHECKLIST – We will go one phase at a time
Phase 0: Business Requirements & Scoping (I have prepared this for you)
Phase 1: Project Setup → I will give files when you say "Phase 1"
Phase 2: Data Ingestion → when you say "Phase 2"
And so on.

PHASE 0: BUSINESS REQUIREMENTS & SCOPING (Ready Now)
Business Problem
Chain-reaction road crashes often result in significant secondary damage, injuries, and insurance claims. Assuming the first impact is unavoidable, how many secondary impacts (2nd, 3rd, 4th+) could be prevented using existing ADAS technologies (Automatic Emergency Braking, Forward Collision Warning, etc.)?
Business Objective
Develop a Preventable Risk Detection Product that:

Quantifies preventable secondary crash risk from real-world dashcam data.
Produces risk profiles by condition (weather, road type, country).
Delivers reproducible, auditable, and interactive outputs for risk analysts.

Stakeholders

Risk & Intelligence analysts (HMRC RIS style)
Compliance / Preventative Risking teams
Senior leadership / policy makers

Success Criteria

Analyse ≥100 real crashes
Deliver ≥85% preventable rate with confidence intervals
Fully reproducible pipeline + interactive dashboard
Clear documentation and QA framework

Scope
In scope: Metadata extraction, manual labelling with QA, analysis, dashboard.
Out of scope: Full computer vision (for future phase).
Ethical & Governance Considerations

Publicly available YouTube videos only
No personal data
Transparent methodology and limitations
Bias mitigation in labelling (inter-rater checks)

Key Risks & Mitigations

Video availability → Use multiple search strategies
Labelling subjectivity → Strict decision tree + QA rules