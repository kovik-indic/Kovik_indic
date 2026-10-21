# Kovik-Indic 🇮🇳
### Deterministic Devanagari Script Integrity & Pluralization Engine

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?style=for-the-badge&logo=vercel)](https://763w3n-6n8gsz0a2-intelligence-agentic-models.vercel.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Encoding](https://img.shields.io/badge/Unicode-NFC%20Normalized-orange?style=for-the-badge)](https://unicode.org/)
[![Status](https://img.shields.io/badge/Production-Ready-success?style=for-the-badge)](#)

> **Kovik-Indic** is a lightweight, zero-dependency, mathematically rigorous Python engine engineered to enforce Devanagari Unicode orthographic validity and deterministic plural inflection in software internationalization (i18n), localization (l10n), and generative AI pipelines.

---

## 🌐 Live Interactive Web Playground

Experience the real-time validator and pluralization engine live in production:

👉 **[Launch Kovik-Indic Live Web Demo](https://763w3n-6n8gsz0a2-intelligence-agentic-models.vercel.app/)**

*Test orphan matras, dangling viramas, ligature boundaries, and plural inflections directly in your browser.*

---

## ⚡ The Problem Solved

Traditional i18n libraries and LLM text generation pipelines often introduce silent orthographic bugs into Devanagari rendering:
1. **Orphan Matras:** Dependent vowels rendered without consonant anchors (e.g., `ागलत` instead of `गलत`).
2. **Dangling Viramas:** Floating halants left at word boundaries (e.g., `क् ` or `त्`).
3. **Glyph & Accent Clashes:** Illegal vowel clashes (e.g., double matras `कीी`, double anusvaras, or halant-matra conflicts `क्ा`).
4. **Broken Pluralization:** Naive plural concatenation that fails on Indic morphophonemic rules.

**Kovik-Indic** solves these problems deterministically with microsecond latency without requiring heavy neural networks.

---

## 📦 Quick Installation

Clone this repository directly into your project:

```bash
git clone https://github.com/your-username/kovik-indic.git
cd kovik-indic
```

Zero external dependencies required — runs out-of-the-box on standard Python 3.8+.

---

## 🚀 Usage Guide

### 1. Script Integrity Validation

```python
from kovik_indic import validate_indic_text

# Clean valid sentence
result = validate_indic_text("प्रधानमंत्री सूर्य घर मुफ्त बिजली योजना")
print(result)
# Output: {'valid': True, 'errors': []}

# Broken string with orphan matra
flagged = validate_indic_text("ागलत शब्द")
print(flagged)
# Output: {'valid': False, 'errors': ["Orphan matra at token start: 'ागलत'"]}
```

### 2. Deterministic Pluralization Engine

```python
from kovik_indic import pluralize_indic

# Singular (Count = 1)
print(pluralize_indic("महीना", 1))
# Output: {'count': 1, 'pluralized': '1 महीना', 'rule': 'singular'}

# Plural (Count > 1)
print(pluralize_indic("महीना", 3))
# Output: {'count': 3, 'pluralized': '3 महीने', 'rule': 'oblique/direct_plural'}
```

---

## 📜 Citation & Research

If you use Kovik-Indic in academic research, localization frameworks, or open-source products, please cite:

```bibtex
@software{kovik_indic_2026,
  author = {Sinha, R. R.},
  title = {Kovik-Indic: Deterministic Devanagari Script Integrity & Pluralization Engine},
  year = {2026},
  organization = {Kovik Indic (An initiative of Kovik Enterprises)},
  url = {https://763w3n-6n8gsz0a2-intelligence-agentic-models.vercel.app/}
}
```

---

## 🛡️ License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for complete legal details.

**Author:** R. R. Sinha  
**Organization:** Kovik Indic *(An initiative of Kovik Enterprises)*
