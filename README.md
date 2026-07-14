# Arabic Medical Text Generation — Severity-Aware Learning Framework

A graduation project on generating clinically reliable Arabic medical responses with Large Language Models (LLMs). Instead of treating every patient complaint as equally important, this project explores several **severity-aware** techniques that teach or guide models to pay more attention to clinically urgent cases.

## Motivation

Standard fine-tuning of LLMs on medical Q&A data treats every training sample and every token identically, even though a headache and a case of severe chest pain do not carry the same clinical risk if the model gets it wrong. This project asks: what happens if severity is explicitly modeled — either by reordering training data, reweighting the loss, combining multiple models, or injecting severity directly into the prompt?

## Dataset

All experiments use a subset of the **Medical Arabic Question Answering (MAQA) dataset**, containing Arabic patient complaints paired with trusted medical responses. Since MAQA doesn't include urgency labels, each study derives its own severity annotation (rule-based keyword matching, a fine-tuned AraBERT classifier, or expert-authored metadata, depending on the approach).

## Approaches

### 1. Severity-Based Curriculum Learning
Questions are labeled Mild / Moderate / Critical, and the model is fine-tuned in three progressive stages — starting with mild cases and gradually introducing more severe ones — using LoRA.

### 2. Multi-Model Response Selection
Extends the curriculum idea to an ensemble: several LLMs are trained under the same curriculum, and at inference time the response with the highest BERTScore is selected as the final output.

### 3. Severity-Aware Weighted Loss
Instead of reordering data, this approach reweights the loss function itself. A severity classifier produces soft probabilities per complaint, and token-level loss is scaled based on how critical the case is.

### 4. STEAD-PE (Structured Static-Dynamic Prompt Engineering)
A training-free alternative: severity and other clinical metadata are injected directly into the prompt at inference time, comparing Zero-Shot, Static, and Dynamic prompting strategies.

## Repository Contents

- `CurriculumLearning.ipynb` — severity annotation and 3-stage curriculum fine-tuning
- `SeverityProbabilities.ipynb` — AraBERT-based severity classifier
- `WeightedLoss.ipynb` — severity-weighted loss fine-tuning
- `StaticDynamic.ipynb` — Zero-Shot / Static / Dynamic prompting (STEAD-PE)
- `Multi-Model.py` — selects the best response across multiple fine-tuned models

## Disclaimer

This project is a research/academic effort exploring severity-aware NLP methods for Arabic medical text generation. It is not a certified medical device and generated responses should not replace professional medical advice.
