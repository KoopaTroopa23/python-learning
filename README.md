# Python Learning Project

A professional Python learning project demonstrating backend API development, ETL data pipelines, automated testing, and full CI/CD deployment pipelines.

---

## 🚀 Live Deployment

| Service | URL |
|--------|-----|
| FastAPI REST API | https://python-learning-fpds.onrender.com |
| API Documentation (Swagger) | https://python-learning-fpds.onrender.com/docs |
| Health Check | https://python-learning-fpds.onrender.com/health |

---

## ⚙️ CI/CD Pipeline

### GitLab
- **Repository:** https://gitlab.com/DevOps-Kw/python-learning
- **Pipeline:** `.gitlab-ci.yml`
- **Stages:** Extract/Transform/Load → Test → Deploy
- Automatically triggers on every push to `main`

### Jenkins
- **Jenkinsfile:** Located in project root (stages: Extract Transform Load → Run Tests → Deploy)
- Runs locally against `http://localhost:8080`; no job is configured there yet -- the
  Jenkinsfile exists and can be pointed at a Pipeline job, but it isn't wired up
  to auto-trigger on push (unlike GitLab CI, which is)

### Render
- **Service:** `python-learning`
- **URL:** https://python-learning-fpds.onrender.com
- **Auto-deploys** on every successful pipeline run via deploy hook

---

## 📁 Project Structure

```
python-learning/
├── app/
│   ├── api/
│   │   ├── main.py          # FastAPI REST API
│   │   └── database.py      # SQLite database module
│   ├── basics/              # Python fundamentals practice
│   ├── etl/
│   │   ├── 01_extract_transform_load_csv.py  # ETL pipeline (Python transform)
│   │   ├── 02_elt_sql.py                     # ELT pipeline (SQL transform)
│   │   ├── 03_etl_pandas.py                  # ETL with pandas
│   │   ├── 04_etl_parquet.py                 # ETL to partitioned Parquet (pyarrow)
│   │   ├── 05_data_quality.py                # Schema validation with pandera
│   │   └── 06_pipeline_flow.py               # Orchestration with Prefect (tasks + flow, retries)
│   └── intermediate/        # Intermediate Python exercises
├── tests/
│   ├── test_main.py         # basic test
│   ├── test_etl.py          # ETL transform tests
│   ├── test_api.py          # API endpoint tests
│   ├── test_parquet.py      # Parquet round-trip test
│   └── test_data_quality.py # pandera schema validation tests
├── terraform/               # Infrastructure as Code
├── Dockerfile               # Docker configuration
├── Jenkinsfile              # Jenkins CI/CD pipeline
├── .gitlab-ci.yml           # GitLab CI/CD pipeline
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info and available endpoints |
| GET | `/health` | Health check |
| GET | `/user/{name}` | Get user by name |
| POST | `/access` | Create user access record |
| GET | `/access` | Get all user access records |
| PUT | `/access/{name}?access=granted` | Change a user's access (404 if not found) |

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Framework:** FastAPI
- **Database:** PostgreSQL in production (Render-managed), SQLite fallback for local dev --
  same code path via SQLAlchemy Core (`app/api/database.py`)
- **Data:** pandas, SQL, Parquet (pyarrow)
- **Data quality:** pandera schema validation
- **Orchestration:** Prefect (tasks, flow, retries)
- **Testing:** PyTest
- **CI/CD:** GitLab CI/CD, Jenkins
- **Deployment:** Render
- **Infrastructure:** Terraform
- **Containerization:** Docker

---

## 🏃 Run Locally

```bash
# Clone the repo
git clone https://gitlab.com/DevOps-Kw/python-learning.git
cd python-learning

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn app.api.main:app --reload

# Run tests
pytest tests/ -v

# Run ETL pipeline
python app/etl/01_extract_transform_load_csv.py   # ETL
python app/etl/02_elt_sql.py                      # ELT
python app/etl/03_etl_pandas.py                   # ETL with pandas
python app/etl/04_etl_parquet.py                  # ETL to partitioned Parquet
python app/etl/05_data_quality.py                 # Data quality validation (pandera)
python app/etl/06_pipeline_flow.py                # Orchestrated with Prefect
```

By default the API connects to a local SQLite file. To use Postgres instead, set
`DATABASE_URL` (e.g. to a local or Render Postgres instance) before running.

---

## 👤 Author

**Kevin Wingfield**
- GitLab: https://gitlab.com/DevOps-Kw
- Email: wingfield.ke@gmail.com