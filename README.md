# HSanders_AIS - GraderClass Unit Testing

Python unit testing assignment for the GraderClass application.

## Files

- `GraderClass.py` - Original Grader application.
- `test_GraderClass.py` - Unit tests created for the application.

## Testing

The test suite uses Python's built-in `unittest` framework.

The tests cover:

- Statement coverage
- Branch coverage
- Condition coverage
- Expression coverage
- Boundary value testing
- Input domain testing
- Invalid input testing

The test suite contains 14 tests covering:

- A, B, C, and D grade ranges
- Grade boundaries from 0 through 100
- Negative and over-100 grades
- Non-numeric input
- Decimal grades

All 14 tests pass successfully.