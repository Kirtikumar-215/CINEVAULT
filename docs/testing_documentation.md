# Testing Documentation

## Automated Tests

Run:

```bash
pytest -q
```

## Test Categories

- Validation tests
- Analytics tests
- Movie search/filter tests
- File save/load tests

## Manual GUI Tests

| Test Case | Expected Result |
|---|---|
| Add valid movie | Movie appears in collection |
| Empty title | Validation error |
| Rating above 5 | Validation error |
| Invalid year | Validation error |
| Edit movie | Updated information appears |
| Delete movie | Movie is removed |
| Search | Matching movies are displayed |
| Genre filter | Only selected genre appears |
| Status filter | Only selected status appears |
| Open reports | Matplotlib chart opens |
| Restart application | Saved CSV data remains |
