# QRAM-Era Threat Model for "Secure" Databases

This thought experiment stress-tests the assumption that encrypted databases remain safe once post-quantum cryptography (PQC) patches key exchange. It frames an Iron Dillo–style warning: even if we fix the keys, the way we store and query data can still be exploited by an attacker with a fault-tolerant quantum computer and large-scale QRAM.

## Scenario: Rural Credit Union in Texas
- **Context:** A small rural credit union runs a cloud-hosted database with 7–10 years of customer records (structured profiles, transaction logs, audit tables) and long-lived snapshots/backups.
- **Protections in place:** Data at rest encrypted under AES with PQC-protected key wrapping; application-level access; deterministic or tokenized search for common queries.
- **Attacker:** APT or criminal syndicate with fault-tolerant QC + QRAM, holding either (a) a stolen snapshot/backup or (b) oracle-style access to the production API.
- **Goal:** Show how QRAM-backed analytics erode the safety margin even without breaking PQC keys.

## Threat Vector 1 — QRAM-Accelerated Pattern Mining on Leaked Snapshots
- **Leakage surface:** Deterministic/format-preserving ciphertexts, tokenized identifiers, fixed-length encrypted records, timestamps, and structural metadata in backups or snapshots.
- **QRAM move:** Load ciphertexts/tokens/metadata as superposition-addressable arrays, then run quantum search, walks, and clustering to rapidly:
  - Spot rare sequences ("only 12 accounts show this odd token cluster") and correlate them across tables.
  - Build relationship graphs (payer→payee, account→merchant) and run quantum-accelerated subgraph search.
- **Impact on a small shop:** Faster re-identification of supposedly anonymized customers, reconstruction of spending patterns, and prioritization of high-value/vulnerable targets—without ever decrypting every field.

## Threat Vector 2 — QRAM + Oracle Access to "Secure" Search
- **Setup:** The attacker compromises an app/API path and issues many queries that the backend answers honestly.
- **QRAM move:** Model the backend as a quantum oracle `f(query) → result/yes-no/count` and apply Grover-style search or amplitude estimation to:
  - Solve membership problems ("Is this person in the dataset?") with fewer queries than classical brute force.
  - Estimate how many records match sensitive predicates (debt levels, diagnosis codes, merchant categories) even when fields are deterministically encrypted.
- **Why rate limits fail:** Classical throttling assumes linear query cost; QRAM-enabled oracles turn "lots of queries" into a quantum microscope on customer data.

## Threat Vector 3 — QRAM + Long-Term Logs and Backups
- **Reality:** Rural institutions often hoard logs, CSV exports, and historical backups indefinitely because storage is cheap.
- **QRAM move:** Combine old API logs, tokenized exports, partial plaintext, and OS logs in superposition to:
  - Infer schemas and field alignments across time.
  - Reconstruct identity mappings across pseudonymized datasets.
  - Identify choke points (privileged service accounts, webhook URLs, admin devices) for focused intrusion.
- **Time shift:** A messy 2025 backup becomes a QRAM-minable gold vein in 2045.

## Why PQC Alone Is Not Enough
- PQC hardens key exchange and protects against record-now, decrypt-later attacks on encrypted channels.
- It does **not** stop structural leakage from deterministic/searchable encryption, access-pattern leakage from search endpoints, or QRAM-accelerated mining of historical artifacts.
- Iron Dillo takeaway: "Post-quantum crypto patches the math on the keys; it doesn’t fix how recklessly we design, store, and query data."

## Defensive Takeaways for Small Orgs
- **Data minimization:** Stop storing what you do not need; put expirations on logs/backups.
- **Schema discipline:** Avoid deterministic/format-preserving encryption where possible; reduce repeated tokens and stable identifiers.
- **Access-path hardening:** Treat APIs/search as future quantum oracles—rate-limit, monitor, and anomaly-detect aggressively.
- **Backup/log governance:** Classify backups and logs as long-term cryptographic assets and plan for quantum-era analytics against today’s archives.
- **Quantum-aware risk framing:** When saying "we use encryption," add "safe from what, and under what future compute assumptions?" Include QRAM-assisted analytics in long-term threat models.
