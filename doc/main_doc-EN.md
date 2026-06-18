<h1 align="center">Technical Documentation — open-blockchain</h1>

<p align="center">
  <a href="main_doc-RU.md">RU</a> | <strong>EN</strong>
</p>

---

## 🏗️ System Architecture

The project is built using a **server-driven architecture with a dedicated background core**. The Admin Panel is not an external client; it serves as an integrated local host management console accessible only to the server administrator.

1. **Background Core (Blockchain Node):** Runs silently in the background as a daemon (`server.py`). It manages the blockchain state in memory, handles mining, and exposes an internal API built with **FastAPI**.
2. **Admin Panel (Host Console):** An integrated text-based interface (`main.py`) for direct node management on the local server. It communicates with the background core locally via `127.0.0.1`.

---

## 🛠️ API Endpoint Reference (FastAPI)

The local node server processes internal requests at `http://127.0.0.1:8000`.

### 1. Node Status
* **Method:** `GET`
* **Endpoint:** `/status`
* **Returns:** Current mining difficulty, block count, and node runtime status.

### 2. Retrieve Blockchain
* **Method:** `GET`
* **Endpoint:** `/blocks`
* **Returns:** A complete JSON array containing all blocks in the ledger.

### 3. Mine New Block
* **Method:** `POST`
* **Endpoint:** `/mine`
* **Request Body (JSON):** `{"data": "string_payload"}`
* **Logic:** Triggers the Proof-of-Work (PoW) mining algorithm on the server side.

### 4. Update Configuration
* **Method:** `POST`
* **Endpoint:** `/set_difficulty`
* **Request Body (JSON):** `{"difficulty": 2}`
* **Returns:** Success status and the updated mining difficulty value.

---

## 📦 Block Data Structure (Schema)

Every block in the ledger is structured as a JSON object with the following properties:

```json
{
  "index": 0,
  "previous_hash": "64_character_hex_string",
  "timestamp": 1718712345.12,
  "data": "Block payload (transactions, logs, or plain text)",
  "nonce": 4215,
  "hash": "target_hash_with_leading_zeros"
}
```

---

## 🤝 Contribution Guidelines

We highly encourage contributions that enhance the core architecture! Before submitting a Pull Request, please ensure you comply with these strict technical rules:

1. **Strict Cross-Platform Design:** Do not use OS-specific utilities (such as Windows `taskkill` or Unix-only shell utilities). Rely strictly on built-in, cross-platform Python modules (`os`, `sys`, `subprocess`, `signal`).
2. **Commit Message Standards:** Use meaningful and descriptive commit messages (preferably following the **Conventional Commits** standard, e.g., `feat: ...`, `fix: ...`, `refactor: ...`).
3. **Decoupled Architecture:** Keep the core blockchain logic (`server.py`) completely separated from the host interface logic (`main.py`).
4. **Pull Request Descriptions:** Every PR must explicitly document what was modified, added, or resolved.
