# CineVault — Movie Collection & Preference Analyzer

CineVault is a Python desktop application designed for the university P67 problem statement:
"A viewer maintains a growing movie collection with information such as genre, rating and viewing status. They want to organize it and understand their viewing preferences."

## Features

- Add, update and delete movie records
- Search and filter by title, genre, status, language and favorite
- Sortable/structured collection data
- Persistent CSV storage
- Automatic backup before deletion
- Dashboard with collection KPIs
- Rating, genre, language and status summaries
- Preferred genre and language analysis
- Period/year analysis
- Simple preference-based suggestions
- Four Matplotlib visual reports
- Input validation and exception handling
- Modular Python architecture
- Automated tests with pytest

## Technology

- Python
- Tkinter
- Pandas
- NumPy
- Matplotlib
- CSV
- Pytest

## Installation

Python 3.10+ is recommended.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Run tests:

```powershell
pytest -q
```

## Project Structure

- `main.py` — application entry point
- `modules/` — business logic, analytics, validation and persistence
- `gui/` — Tkinter screens
- `charts/` — Matplotlib reports
- `data/` — persistent CSV data
- `tests/` — automated tests
- `docs/` — documentation

## University Requirement Mapping

| Requirement | Implementation |
|---|---|
| Python functions/data structures | All application modules |
| File handling | `modules/file_manager.py` + CSV |
| Minimum 3 user-defined modules | 5+ modules |
| NumPy/Pandas | `analytics.py` |
| Tkinter GUI | `gui/` |
| 2 Matplotlib visualizations | 4 reports |
| Input validation | `validation.py` |
| Exception handling | File and GUI operations |
| Documentation/testing | README + docs + pytest |

## Future Scope

Possible future enhancements include SQLite storage, user accounts, online movie APIs, posters, advanced recommendations and export to PDF.
