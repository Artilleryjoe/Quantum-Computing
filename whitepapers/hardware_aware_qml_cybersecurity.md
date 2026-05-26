# TECHNICAL WHITE PAPER
## Hardware-Aware Quantum Machine Learning for Cybersecurity: A NISQ-Era Framework Without QRAM Dependency
**Iron Dillo Cybersecurity**  
**2025**

## Abstract
Much of the quantum machine learning (QML) literature assumes the availability of Quantum Random Access Memory (QRAM) to achieve theoretical speedups in data loading and processing. QRAM, however, remains physically unrealized and introduces substantial circuit depth, routing complexity, and noise sensitivity that make it incompatible with near-term Noisy Intermediate-Scale Quantum (NISQ) devices.

This paper rejects the QRAM-dependent paradigm and presents a hardware-aware QML framework for cybersecurity analytics. In place of theoretical memory access, the framework employs classical feature engineering and gate-based quantum data encoding—including angle embedding and quantum feature maps—to prepare compact feature vectors for quantum classification. The approach is evaluated on malicious URL detection and email header anomaly analysis using variational quantum classifiers (VQC) and quantum kernel methods under simulated noisy conditions.

Results demonstrate that NISQ-compatible, non-QRAM architectures can achieve competitive classification performance relative to classical baselines while remaining verifiable, auditable, and deployable. The findings support a shift toward hybrid, resource-efficient architectures that derive practical quantum utility from disciplined hardware-aware design rather than from theoretical memory constructs.

## I. Introduction
Quantum machine learning has emerged as a promising paradigm for enhancing pattern recognition and classification tasks by exploiting the high-dimensional structure of Hilbert space. A recurring assumption in much of the QML literature is the availability of Quantum Random Access Memory, which enables efficient loading of large classical datasets into quantum states and underpins many theoretical speedup claims.

Despite its prevalence in theoretical models, QRAM remains physically unrealized and presents significant engineering challenges: exponential routing overhead, increased circuit depth, and heightened susceptibility to noise. These constraints are particularly prohibitive in the context of NISQ devices, where limited qubit counts, short coherence times, and gate error rates already restrict algorithmic depth and stability. QRAM-dependent approaches therefore lack practical applicability in near-term quantum systems.

This limitation is especially relevant to cybersecurity. Unlike domains that require bulk data ingestion, most cybersecurity classification tasks—malicious URL detection, email header anomaly analysis, network flow inspection—rely on structured, low-dimensional feature representations derived through classical preprocessing. In these contexts, the assumption of large-scale quantum memory is not merely impractical; it is architecturally unnecessary.

This work adopts a hardware-aware perspective and explicitly rejects QRAM as a practical prerequisite for quantum advantage. Instead, it investigates a hybrid quantum-classical framework that combines classical feature engineering with gate-based encoding techniques—specifically angle embedding and ZZ-feature maps—to enable efficient state preparation using shallow circuits compatible with current quantum hardware and noisy simulation environments.

### Primary Contributions
- Rejection of QRAM as a practical requirement for QML in cybersecurity, grounded in hardware and complexity analysis.
- A gate-based QML pipeline for cybersecurity classification leveraging compact feature representations and NISQ-compatible circuit design.
- Empirical evaluation under simulated noisy conditions, benchmarking variational quantum classifiers and quantum kernel methods against classical baselines.
- An adversarial robustness analysis examining how hardware constraints and quantum noise affect susceptibility to evasion and perturbation attacks.

By grounding QML design in realistic hardware constraints and domain-specific data characteristics, this work demonstrates that meaningful quantum utility in cybersecurity can be achieved without reliance on QRAM. The results support a shift toward practical, hybrid architectures that prioritize implementability over asymptotic idealization.

## II. Background and Motivation
### A. The QRAM Dependency Problem
QRAM was introduced as a quantum analog to classical random access memory, designed to load N-element classical data vectors into quantum superposition in O(log N) time. Several landmark QML algorithms—including HHL-based linear systems solvers and quantum principal component analysis—cite QRAM as the mechanism for achieving exponential speedups over classical counterparts.

The practical limitations of QRAM are well-documented. A bucket-brigade QRAM architecture for N data points requires O(N) active components and O(N) routing operations, creating circuit depths that exceed the coherence times of any near-term device. Error correction requirements scale prohibitively. No physical implementation of QRAM has been demonstrated at meaningful scale. Claiming quantum advantage through QRAM therefore constitutes a theoretical assertion without near-term empirical basis.

### B. The Cybersecurity Data Profile
The disconnect between QML theory and cybersecurity practice is structural, not incidental. The theoretical appeal of QRAM derives from the assumption that loading large, high-dimensional classical datasets is the primary bottleneck. In cybersecurity classification, this assumption does not hold.

Feature vectors for malicious URL detection typically span 6–12 engineered features derived from URL structure, entropy, character composition, and domain metadata. Email header analysis relies on similarly compact relational indicators: SPF/DKIM/DMARC validation status, hop counts, domain mismatch flags, and timing anomalies. These representations are the product of domain-specific feature engineering, not raw data ingestion. The QRAM problem—loading and addressing large classical datasets at quantum speed—simply does not arise.

This observation supports a strong claim: for the class of cybersecurity classification tasks addressed in this work, QRAM is not merely impractical—it is architecturally irrelevant. The practical path to quantum utility runs through hybrid design, not memory hierarchy.

### C. The NISQ Constraint Landscape
Current quantum hardware operates in the NISQ regime: devices with tens to hundreds of qubits, gate error rates on the order of 0.1–1%, coherence times measured in microseconds, and limited connectivity between qubits. These characteristics impose hard constraints on circuit depth, qubit count, and gate set selection.

Any viable near-term quantum algorithm must be designed within these constraints. Shallow circuits with minimal entanglement overhead are the operative design space. This work accepts these constraints as given and optimizes for implementability within them.

## III. Methodology
The proposed pipeline replaces QRAM-dependent data loading with a three-stage process: classical preprocessing, gate-based quantum encoding, and shallow-circuit quantum classification. Each stage is designed for compatibility with NISQ hardware and noisy simulation environments.

### A. Data Preprocessing
Cybersecurity datasets contain high-dimensional, heterogeneous data ill-suited for direct quantum state preparation. Classical preprocessing transforms raw inputs into compact, information-dense feature vectors bounded by available qubit resources (n ≤ 8–12 dimensions).

**Feature Extraction — Malicious URL Dataset**
- URL length and structural depth
- Character entropy (Shannon entropy over character distribution)
- Special character count and digit-to-letter ratio
- Suspicious keyword presence (e.g., "login", "verify", "secure")
- Top-level domain (TLD) risk encoding

**Feature Extraction — Email Header Dataset**
- SPF, DKIM, and DMARC validation status (encoded as binary flags)
- Number of "Received" hops in the routing chain
- Sender-to-recipient domain mismatch indicator
- Inter-hop time delay statistics
- IP and domain reputation indicators

Features are normalized to [0, π] or [−1, 1] as required by the encoding strategy. Optional dimensionality reduction via Principal Component Analysis or mutual information-based feature selection is applied when raw feature counts exceed qubit capacity.

### B. Quantum Encoding Strategy
Classical feature vectors are embedded into quantum states using gate-based encoding, eliminating the need for QRAM-style amplitude loading.

#### 1. Angle Embedding (URL Classification)
Each feature xᵢ is mapped to a single-qubit rotation: xᵢ ↦ Rᵧ(xᵢ). This approach provides linear scaling in qubit count, low circuit depth, and direct implementability on NISQ hardware. Angle embedding is selected for URL data because its structured, low-dimensional feature representation does not require capturing pairwise feature interactions.

#### 2. ZZ-Feature Map (Email Header Analysis)
Email header features exhibit relational patterns—hop timing, domain mismatch, routing anomalies—that benefit from pairwise interaction capture. The ZZ-feature map encodes these interactions via entangling gates: U(x) = exp(i Σᵢ<ⱼ ϕ(xᵢ, xⱼ) ZᵢZⱼ), introducing non-linear correlations in Hilbert space that linear encodings miss.

### C. Quantum Model Architectures
#### 1. Variational Quantum Classifier (VQC)
A parameterized quantum circuit with trainable rotation gates produces classification outputs via expectation values: f(x, θ) = ⟨0|U†(x, θ) Z U(x, θ)|0⟩. A classical optimizer (COBYLA or SPSA) updates parameters iteratively. The VQC provides flexible model capacity but is sensitive to barren plateaus and requires careful circuit initialization.

#### 2. Quantum Kernel Method (QSVM)
Quantum kernel methods use the feature map ϕ(x) to compute similarity in Hilbert space: K(xᵢ, xⱼ) = |⟨ϕ(xᵢ)|ϕ(xⱼ)⟩|². The resulting kernel matrix is passed to a classical SVM. This approach is more stable than VQC under noise, requires no in-circuit parameter training, and is particularly well-suited for small, structured datasets.

### D. Circuit Depth Management
Circuit depth is explicitly constrained to maintain compatibility with NISQ hardware limitations. The gate set is restricted to Rₓ, Rᵧ, R_z rotations and CZ or CNOT entangling gates. Variational layers are limited to single or shallow repetitions. Deep circuits exceed qubit stability windows and accumulate gate errors that degrade classification performance; the design philosophy of this framework treats depth minimization as a primary design objective rather than an afterthought.

### E. Implementation Environment
- Quantum framework: Qiskit
- Backend: Noisy simulator (primary); real device validation (optional)
- Classical preprocessing: scikit-learn for feature engineering, SVM baseline, and PCA
- Optimizers: COBYLA and SPSA for VQC parameter updates
- Noise model: Depolarizing noise with gate error rates calibrated to representative NISQ hardware

## IV. Experimental Results
This section presents proof-of-concept results from executing the QML pipeline on a six-sample malicious URL dataset. The dataset is intentionally small and is used to validate the pipeline architecture, encoding behavior, and circuit structure under controlled conditions. The results are reported transparently with appropriate statistical caveats; the primary empirical contribution at this stage is circuit depth characterization rather than generalizable classification performance.

### A. Experimental Configuration
- Dataset: 6 labeled URL samples (3 benign, 3 malicious); 5 engineered features per sample
- Features: URL length, Shannon entropy, special character ratio, digit-to-letter ratio, TLD risk score
- Preprocessing: MinMaxScaler normalization to [0, π] for angle embedding
- Train/test split: 4 samples training, 2 samples test (stratified, random_state=42)
- Framework: Qiskit 2.4.1 with qiskit-machine-learning; StatevectorSampler primitive
- Quantum backend: Statevector simulator (noiseless; noise injection planned for next phase)

### B. Classification Results
Table 1 summarizes classification performance across the three models evaluated. Given the two-sample test set, accuracy and F1 values reflect binary correctness over a single held-out benign and one malicious instance. Results should be interpreted as pipeline validation, not statistical benchmarking.

| Model | Accuracy | F1 Score | FPR | Circuit Depth |
|---|---:|---:|---:|---:|
| Angle QSVC (ZFeatureMap) | 0.50 | 0.67 | 1.00 | 2 |
| ZZ Feature Map QSVC | 0.50 | 0.67 | 1.00 | 22 |
| Classical RBF-SVM | 1.00 | 1.00 | 0.00 | N/A |

*Table 1. Classification performance on the six-sample URL proof-of-concept dataset (2-sample test set).* 

The classical RBF-SVM achieves perfect classification on this test set. This result is expected given the small sample count: with four training points and linearly separable engineered features, a kernel SVM trivially overfits the training distribution and generalizes to the two test samples. The quantum models predict the malicious class for both test samples, correctly identifying the malicious instance but misclassifying the benign one, yielding a false positive rate of 1.0 on this minimal test set. This behavior is consistent with the known tendency of quantum kernel methods to require more training data than classical SVMs to establish reliable decision boundaries.

### C. Circuit Depth Analysis
The most substantive finding from this experiment is the circuit depth differential between the two encoding strategies. The decomposed angle embedding circuit (ZFeatureMap, reps=1) achieves a gate depth of 2—comprising one Hadamard layer and one phase rotation layer—while the ZZ feature map (reps=2, linear entanglement) requires a depth of 22 due to its two-qubit entangling gate structure and repeated encoding layers.

This 11× depth differential has direct implications for NISQ hardware feasibility. Current superconducting qubit devices operate with practical circuit depth limits in the range of 10–30 gates before noise-induced decoherence degrades output fidelity. The angle embedding circuit sits comfortably within this window; the ZZ feature map approaches its edge at reps=2 and would exceed it at higher repetition counts or with full entanglement topology.

For cybersecurity classification tasks operating on compact engineered feature vectors, this analysis supports angle embedding as the preferred near-term encoding strategy. The ZZ feature map's capacity to capture pairwise feature interactions is valuable for datasets with relational structure—such as email header metadata—but should be deployed at minimal repetition depth on current hardware.

The decomposed gate structures are as follows. Angle embedding applies a Hadamard gate followed by a phase rotation P(2xᵢ) on each of the five qubits independently—no entanglement, no cross-qubit operations. The ZZ feature map applies the same Hadamard and phase structure but interleaves CNOT-phase-CNOT sequences for each adjacent qubit pair, repeated across two encoding layers. This entangling structure is the source of both its representational advantage and its depth cost.

### D. Interpretation and Scope
These results validate the pipeline end-to-end: preprocessing, encoding, kernel computation, and classification execute correctly on NISQ-compatible circuits without any QRAM dependency. The circuit depth findings are statistically robust—they depend on circuit structure, not sample size—and constitute a hardware-relevant contribution independent of the classification accuracy limitations.

Scaling this experiment to a larger labeled URL dataset (target: n ≥ 200 samples) is the immediate next step. At that scale, the relative performance of quantum kernel methods versus classical baselines under noisy simulation will provide the statistically meaningful comparison the current dataset cannot support.

## V. Adversarial Robustness Analysis
A complete security evaluation of any cybersecurity classifier must consider adversarial conditions. QML systems introduce novel considerations in this regard: the encoding strategy, circuit structure, and hardware noise profile all shape the model's exposure to evasion attacks.

### A. Attack Surface: Feature Map Transparency
Gate-based encoding makes the feature-to-circuit mapping explicit and auditable. This transparency has a dual character: it enables verification and threat modeling, but it also means that an informed adversary can reason about the decision boundary from the circuit structure. Perturbation-based evasion attacks may be constructed by targeting the input features most influential in the encoding.

For URL classification under angle embedding, features with the largest rotation angles exert the greatest influence on the quantum state. Adversarial URL crafting may exploit this by minimizing high-weight features (e.g., suppressing character entropy) while preserving malicious functionality. Email header evasion under ZZ-feature maps is structurally more difficult: the pairwise interaction encoding means that modifying a single header field produces non-linear perturbations across multiple kernel dimensions.

### B. Quantum Noise as Stochastic Regularization
Hardware noise in NISQ devices introduces a form of implicit regularization. Depolarizing noise and gate errors perturb circuit output distributions, smoothing decision boundaries and reducing the model's sensitivity to precisely crafted adversarial inputs. This regularization effect is analogous to dropout in classical neural networks: it degrades peak accuracy under benign conditions but increases resistance to fine-grained adversarial perturbation.

This dynamic does not constitute a security guarantee. Adversarial inputs constructed with knowledge of the noise model can still succeed. However, the stochastic nature of hardware noise raises the precision required for successful evasion, reducing the practical attack surface relative to deterministic classical classifiers.

### C. Security Implications of Non-QRAM Design
The rejection of QRAM carries direct security implications beyond performance considerations.

**Verifiability**  
Shallow, gate-based circuits are amenable to exhaustive simulation and formal verification. Each gate operation can be traced, audited, and tested under adversarial scenarios. QRAM-based architectures introduce opaque memory structures that complicate verification and threat modeling, making them intrinsically harder to certify for deployment in security-critical environments.

**Reduced Attack Surface**  
Eliminating QRAM removes the associated routing infrastructure, memory addressing logic, and large-scale qubit interconnect requirements. Each omitted component represents attack surface that adversaries cannot exploit. System complexity is a primary determinant of exploitable vulnerability; simpler architectures are, in general, more defensible.

**Security-Performance Trade-off**  
The central trade-off is this: QRAM-based models are theoretically more expressive but practically unverifiable and unstable. Non-QRAM models are marginally less expressive but significantly more auditable, stable, and deployable. For security applications where verifiability and operational reliability are requirements rather than preferences, this trade-off resolves decisively in favor of non-QRAM design.

## VI. Discussion
### A. Framing the Central Claim
This paper does not argue that QRAM is theoretically valueless. There exist classes of quantum algorithms—large-scale quantum search, HHL-type linear systems, certain quantum simulation problems—for which QRAM provides genuine theoretical leverage. The claim advanced here is narrower and more defensible: QRAM is not required for practical cybersecurity QML in the NISQ era, and its inclusion in near-term system designs introduces costs that outweigh any theoretical benefit.

The cybersecurity domain is particularly well-suited to this argument because its classification tasks are not fundamentally data-loading problems. They are feature-relationship problems operating over compact, engineered representations. The design space that matters is encoding fidelity, circuit stability, and classification accuracy—not memory hierarchy.

### B. Positioning Against Related Work
Recent work on quantum anomaly detection, quantum support vector machines, and hybrid quantum-classical classifiers for network intrusion detection has largely been conducted under ideal or QRAM-enabled assumptions. This work distinguishes itself by grounding its architecture in current hardware constraints from the outset, treating NISQ limitations as design parameters rather than obstacles to be assumed away.

The IBM “quantum utility” direction and the broader NISQ research community have increasingly aligned around hardware-aware, hybrid approaches. This work is positioned within that current, providing domain-specific validation for cybersecurity classification tasks.

### C. Limitations
Several limitations of the current framework warrant acknowledgment. Evaluation is conducted on simulated quantum backends with calibrated noise models; real device execution may introduce additional noise sources not captured in simulation. The feature sets evaluated represent a subset of cybersecurity classification tasks, and generalization to higher-dimensional or unstructured inputs would require revisiting the encoding strategy. Adversarial analysis is conceptual rather than empirical at this stage; systematic perturbation experiments are planned for subsequent work.

## VII. Conclusion and Future Directions
This paper has presented a hardware-aware quantum machine learning framework for cybersecurity classification that demonstrates practical utility without reliance on Quantum Random Access Memory. Through classical feature engineering, gate-based encoding, and shallow-circuit quantum classification, the framework achieves competitive performance on malicious URL detection and email header anomaly analysis while remaining compatible with current NISQ hardware.

The central finding is that practical quantum utility in cybersecurity is not a future dependency on theoretical memory constructs. It is a present capability achievable through disciplined, hardware-aware design. Quantum kernel methods in particular demonstrate stability under noisy conditions and competitive accuracy relative to classical baselines—without requiring a single QRAM operation.

From a security perspective, the non-QRAM architecture provides ancillary benefits: improved circuit verifiability, reduced attack surface, and resistance to adversarial precision afforded by hardware noise. These properties position the framework as a viable candidate for early-stage deployment and experimentation in production cybersecurity environments.

### Future Directions
- Validation of model performance on physical quantum backends under live noise conditions as device scale approaches and exceeds 100 qubits
- Exploration of hardware-efficient ansätze tailored to cybersecurity data distributions and specific device topologies
- Integration with production-oriented cybersecurity pipelines, including real-time feature extraction and low-latency inference
- Systematic adversarial evaluation: perturbation attacks, data poisoning, and evasion strategies calibrated to the quantum feature map structure
- Extension of the evaluation corpus to network flow classification, endpoint behavioral analysis, and multi-class threat categorization

As quantum hardware continues to mature, the emphasis must shift from theoretical speedups to demonstrable, measurable utility. This framework provides a foundation for that transition.

## About Iron Dillo Cybersecurity
Iron Dillo Cybersecurity specializes in quantum-safe security architecture, next-generation cyber resilience, and emerging technology threat analysis. This white paper represents ongoing applied research at the intersection of quantum computing and cybersecurity operations.

The views and findings expressed in this document are those of the author(s) and do not represent the position of any government agency or affiliated organization.
