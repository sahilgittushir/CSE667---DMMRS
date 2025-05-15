# 🤖 CSE667 – Decision Making for Multi-Robot Systems (DMMRS)

Welcome to the official repository for **CSE667 – Decision Making for Multi-Robot Systems (DMMRS)**, a graduate-level course offered at **IIIT-Delhi**. This repository compiles code implementations, mathematical proofs, and theoretical insights related to the assignments in this course.

Whether you're a student, researcher, or robotics enthusiast, this resource is designed to aid your understanding of **strategic decision-making, game theory, belief modeling, and information-theoretic planning** in multi-robot systems.

---

## 📘 Course Overview

- **Course Title:** Decision Making for Multi-Robot Systems  
- **Course Code:** CSE667  
- **Semester:** Spring 2025  
- **Institution:** Indraprastha Institute of Information Technology, Delhi (IIIT-Delhi)  
- **Instructor:** Prof. Dr. **Tanmoy Kundu**  
- **Repository Maintainer:** [Your Full Name]  

---

## 📝 Assignment Breakdown

### 📂 Assignment 1 – Dominant Strategies & Maxmin Equilibria
**Focus:** Finite strategic-form games  
**Topics Covered:**
- Strongly & weakly dominant strategies
- Maxmin strategies and values
- Dominant strategy equilibria

**Implemented Outputs:**
- a) All strongly dominant strategies  
- b) All weakly dominant strategies  
- c) Maxmin values & corresponding strategies  
- d) Strongly dominant strategy equilibrium (if exists)  
- e) All weakly dominant strategy equilibria (if exist)  

---

### 📂 Assignment 2 – Nash Equilibria Computation
**Focus:** Equilibrium computation in strategic-form games  
**Tools Used:** Linear Programming (LP), Z3 SMT Solver  
**Topics Covered:**
- Pure strategy Nash equilibrium detection  
- Mixed strategy Nash equilibrium computation  

**Implemented Outputs:**
- a) A pure strategy Nash equilibrium (if one exists)  
- b) A mixed strategy Nash equilibrium  

*Note: Uses Z3 SMT solver for equilibrium calculation. See [Z3Py Tutorial](https://ericpony.github.io/z3py-tutorial/guide-examples.htm).*

---

### 📂 Assignment 3 – Belief Modeling, Entropy & Information Theory
**Focus:** Belief uncertainty and information gain in robot planning  
**Topics Covered:**
- Entropy and conditional entropy  
- Mutual information and KL-divergence  
- Belief-based action selection in exploration tasks  

**Key Concepts:**
- 🔍 Conditional entropy: \( H(X|Y) = H(X,Y) - H(Y) \)  
- 🔄 Information symmetry: \( I(X;Y) = I(Y;X) \)  
- 📊 Information gain via KL-divergence:  
  \( I(X;Y) = KL(P_{XY} || P_X P_Y) \)  
- 🤖 Optimal exploratory action selection via information maximization  

---

📂 Folder Structure
bash├── Assignment-1/
│   └── DominantStrategies_MaxminEquilibria.py
├── Assignment-2/
│   └── NashEquilibriumSolver.py
├── Assignment-3/
│   ├── Entropy_MutualInformation_Proofs.md
│   └── BeliefExploration_Strategy.md
└── README.md


🧠 Target Audience
This repository is intended for:

🎓 Graduate students enrolled in CSE667 (DMMRS) at IIIT-Delhi
🤖 Robotics researchers exploring decision-making models
🧪 Theorists & Mathematicians interested in game theory and belief modeling
👨‍🏫 Instructors looking for sample problem sets and solved assignments
👩‍💻 Developers & Learners working in autonomous systems, planning, and AI

🙏 Acknowledgements
A sincere thanks to Prof. Dr. Tanmoy Kundu for delivering this intellectually challenging and insightful course at IIIT-Delhi. The structure of the assignments, algorithms, and theoretical problems reflect his exceptional academic rigor and clarity.
All solutions, implementations, and writeups have been curated and maintained by [Your Full Name] to support current and future students of this course.
👤 Maintainer
Name: [Your Full Name]
Email: [your.email@example.com] (optional)
GitHub: https://github.com/yourusername
Affiliation: IIIT-Delhi
📜 License
This repository is made available for educational and academic use only. All code and content are original contributions unless otherwise credited.
📌 If you use any portion of this repository in your work or projects, please cite the author and acknowledge the course appropriately.
🌟 Contribute / Star / Fork
If you find this repository helpful, you're encouraged to:

⭐ Star to support the work
🍴 Fork to adapt and extend it
🛠️ Open issues or PRs for improvements or suggestions

🚀 Wishing you success in your multi-robot systems journey. Keep exploring and learning!














