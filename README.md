# 🧠 Persona-Based Document Intelligence System
<p align="center"><i>Offline, containerized, and role-aware PDF summarization pipeline – built for Adobe Hackathon Challenge 1b.</i></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/SentenceTransformers-MiniLM-green"/>
  <img src="https://img.shields.io/badge/PyTorch-CPU--Only-red?logo=pytorch"/>
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?logo=docker"/>
  <img src="https://img.shields.io/badge/JSON-Structured-yellow"/>
</p>

---

## 🧠 Overview

This project is a submission for **Adobe India Hackathon 2025 – Challenge 1b**.

> ⚡ **Goal:** Given a persona and a job-to-be-done, intelligently extract and rank relevant sections from a collection of documents — with detailed subsection summaries — all in an offline, CPU-only, Dockerized environment.

---

## 🚀 Features

- ✅ Accepts **PDF collections** and **persona/task JSON** as input  
- ✅ Extracts and **ranks the most relevant sections** per persona and job  
- ✅ Provides **subsection-level summarization**  
- ✅ Fully **offline**, **Dockerized**, and **CPU-only**  
- ✅ Embedding-based ranking using `sentence-transformers/all-MiniLM-L6-v2`  
- ✅ Output includes complete **JSON metadata + analysis**

---

## 🧱 Architecture

```
📦 persona_doc_analyzer/
├── 📁 app/
│   ├── ranker.py
│   ├── summarizer.py
│   └── utils.py
│   └── extractor.py
├── 📁 models/
├── 📁 input/
├── 📁 output/
├── Dockerfile
├── requirements.txt
├── main.py
├── prepare_input.py
├── download_model.py
└── README.md
```

---

## 🔧 Modules & Responsibilities

| Module             | Description |
|--------------------|-------------|
| `main.py`          | Loads persona, extracts sections, ranks and summarizes, writes JSON |
| `prepare_input.py` | Reads challenge1b_input.json and copies PDFs/persona to `/input/` |
| `download_model.py`| Downloads and saves the transformer model locally |
| `ranker.py`        | Embeds and ranks each section using semantic similarity |
| `summarizer.py`    | Extracts key lines or insights from each top section |
| `utils.py`         | Reads persona/task, performs formatting or helper tasks |

---

## 🛠️ Technologies Used

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/SentenceTransformers-MiniLM-green"/>
  <img src="https://img.shields.io/badge/PyTorch-CPU--Only-red?logo=pytorch"/>
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?logo=docker"/>
  <img src="https://img.shields.io/badge/JSON-Structured-yellow"/>
</p>

---

## 🐳 Docker Usage

### 🔨 Build the Image

```bash
docker build --no-cache -t persona-doc-analyzer .
```

### 🚀 Run the Container

```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  persona-doc-analyzer
```

✅ Output JSON will appear inside the `/output` directory.

---

## ⚙️ How to Use (Step-by-Step)

### 1. Download the Sentence Transformer Model

```bash
python download_model.py
```

Creates: `./models/all-MiniLM-L6-v2`

---

### 2. Prepare the Input Folder

Ensure this structure:

```
your_folder/
├── challenge1b_input.json
└── PDFs/
    ├── doc1.pdf
    ├── doc2.pdf
```

Run:

```bash
python prepare_input.py /path/to/your_folder
```

This generates `input/` with:

- persona_job.txt
- doc1.pdf, doc2.pdf, ...

---

### 3. Run the Pipeline

```bash
python main.py
```

Creates: `output/output.json`

---

## 🧪 Sample Output Structure

```json
{
  "metadata": {
    "input_documents": ["doc1.pdf", "doc2.pdf"],
    "persona": "Banking Operations Head",
    "job_to_be_done": "Automate document workflow",
    "processing_timestamp": "2025-07-28T15:30:12"
  },
  "extracted_sections": [
    {
      "document": "doc2.pdf",
      "section_title": "Improving Workflow Automation",
      "importance_rank": 1,
      "page_number": 3
    }
  ],
  "subsection_analysis": [
    {
      "summary": "Section emphasizes RPA use in banking, including real-time approval mechanisms..."
    }
  ]
}
```

---

## ✅ Adobe Constraints Checklist

| Constraint                           | Status                                   |
|-------------------------------------|------------------------------------------|
| 🔒 Offline                          | ✅ Yes                                    |
| 🖥️ CPU-only                        | ✅ Yes                                    |
| 💾 Model Size ≤ 200MB              | ✅ ~90MB                                  |
| 🐳 Dockerized (AMD64)               | ✅ Yes                                    |
| 📊 JSON Schema Compatible           | ✅ Yes                                    |
| ⚡ Fast PDF Processing               | ✅ Under 10 seconds per 50-page doc       |

---

## ❗ Known Limitations

| Limitation            | Cause                            | Future Fix                            |
|-----------------------|----------------------------------|----------------------------------------|
| Scanned PDFs not supported | No OCR used                | Add lightweight OCR (Tesseract)        |
| Simple summaries      | Basic heuristic extraction       | Add transformer-based summarization    |
| No UI                 | CLI only                         | Add Flask/Streamlit frontend           |

---

## 🤝 Team & Credits

Built with 💡 by **Team Tech-Titans** for Adobe India Hackathon 2025.

👩‍💻 Contributors:
- Deepali Chauhan  
- Abhay Kanojia
  
