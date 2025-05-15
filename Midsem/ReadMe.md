# 🧠 CSE667 – Mid-Semester Paper (Set-1): Decision Making Models in Robotic Systems (DMMRS)

Welcome to the **CSE667 (DMMRS)** Midsem (Set-1) repository. This repository contains detailed solutions and formal definitions for the **Mid-Semester Exam held on 24-Feb-2025** at **IIIT-Delhi**. It serves as a learning aid for students, researchers, and instructors interested in **game theory**, **multi-agent decision making**, and **robotic planning models**.

---

## 📘 Exam Overview

- **Course Title:** Decision Making Models in Robotic Systems (DMMRS)  
- **Course Code:** CSE667  
- **Exam Type:** Midsem (Set-1)  
- **Full Marks:** 30  
- **Institution:** IIIT-Delhi  
- **Instructor:** Prof. Dr. Tanmoy Kundu  
- **Exam Date:** 24-Feb-2025  
- **Repository Maintainer:** Sahil Tushir

---

## 📝 Questions & Themes

### 🧩 Q1: Conceptual — True/False [6 Marks]
Evaluate six statements related to dominant strategies, Nash equilibria, expected utilities, and best responses in strategic form games.

### 📘 Q2: Formal Definitions [6 Marks]
Define the following formally in the context of a strategic form game Γ = ⟨N, (Si), (ui)⟩:
- Weakly dominated strategy  
- Pure strategy Nash equilibrium (PSNE)  
- Best response correspondence  
- Maxmin strategy  

📖 *References:* Book by Narahari (Sections 5.2, 6.1, 6.6)

### 🔢 Q3: Auction Equilibrium [4 Marks]
Analyze a discrete bidding auction between two players. Compute a PSNE, if one exists.

### 📊 Q4: Mixed Strategy Equilibrium (MSNE) [4 Marks]
Two-player game:
- **Strategy spaces:** S₁ = [0, 1], S₂ = [3, 4]  
- **Utilities:** u₁(x, y) = –u₂(x, y) = |x – y|

Tasks:
- Count possible strategies
- Compute MSNE

### 🎯 Q5: Iterated Elimination of Dominated Strategies [4 Marks]
Given a 3×3 payoff matrix, eliminate strongly dominated strategies step-by-step and show each reduction. Final strategy profile: **(B, Y)**

### 🚁 Q6: Drone-Ground Vehicle Assignment Cost [3 Marks]
Model a cost function for a drone path based on ground vehicle assignment. Variables include:
- Path: pi = (e₁ᵢ, ..., eTᵢ)
- Assignment vector: Ai = (a₁ᵢ, ..., aTᵢ)
- Edge costs: c(ekᵢ)

### 🏭 Q7: Warehouse Recharge Scheduling [3 Marks]
Propose a computationally feasible algorithm to manage mobile rechargers and worker robots over a time horizon T. Ensure trade-offs between:
- Initial/final locations
- Charge levels
- Intractability at final time step

---

## 📂 Folder Structure

```bash
Midsem-Paper/
├── Midsem_Set1_Questions.pdf
├── Midsem_Set1_Solutions.md
└── README.md
```
