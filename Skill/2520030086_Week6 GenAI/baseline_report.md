# Week 6 – Generative AI Programming Practical

## Experiment: Golden Question Set – Baseline Evaluation

**Release Version:** v0.1  
**Model:** Llama 3.2  
**Evaluation Date:** 20 November 2026

### 1. Objective
To create a golden question set containing 30 questions with expected answers, keywords and reference sources, and evaluate the baseline responses using the Llama 3.2 model.

### 2. Tools and Technologies
- Python
- Ollama
- Llama 3.2
- Requests library
- VS Code

### 3. Experiment Results

| Metric | Result |
|---|---:|
| Total Questions | 30 |
| Successful Responses | 29 |
| Passed Questions | 11 |
| Questions for Review | 18 |
| Failed Requests | 1 |
| Average Keyword Coverage | 47.41% |

### 4. Observations
- The model successfully generated responses for 29 questions.
- 11 questions achieved PASS status.
- 18 questions were marked for REVIEW due to insufficient keyword coverage.
- Question Q023 encountered a request timeout.
- The average keyword coverage was 47.41%.

### 5. Output
The program generated `baseline_results.csv`, containing the questions, expected answers, LLM responses, matched keywords, missing keywords, scores and evaluation status.

### 6. Conclusion
The first baseline evaluation using Llama 3.2 was completed successfully. The results were recorded in the CSV output file and the experiment was officially labelled as **Release v0.1**.

**Final Status: BASELINE RUN COMPLETED – RELEASE v0.1**