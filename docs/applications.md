# Python in practice

[Back to the repository](../README.md)

Choose a language according to the problem, the team's experience, operational requirements, and the libraries available.

| Application | What Python contributes | Ecosystem examples | Important tradeoff |
| --- | --- | --- | --- |
| Automation | File processing, reports, scheduled scripts | pathlib, csv, argparse | Validate inputs before changing real files |
| Web backends | Routing, business logic, APIs | Django, Flask, FastAPI | Deployment also needs authentication, observability, and operations |
| Data analysis | Cleaning, aggregation, visualization | pandas, NumPy, Matplotlib | Data quality determines whether results are useful |
| Machine learning | Feature processing, training, inference | scikit-learn, PyTorch | Evaluate on unseen data and monitor model behavior |
| Scientific computing | Numerical methods and experiments | NumPy, SciPy | Understand units, precision, and numerical assumptions |
| Testing and tooling | Test suites, build scripts, developer utilities | unittest, pytest | Automation should produce reproducible results |
| Desktop applications | Event-driven graphical interfaces | tkinter, PySide | Packaging and platform integration add work |
| Education | Readable programs and interactive exercises | Python interpreter, Jupyter | Learn underlying concepts alongside library APIs |

The linked projects below are examples of the ecosystem, not dependencies of this repository.

## How the examples connect to larger systems

**Business reporting:** an exported CSV can become a summary that feeds a dashboard. Example 07 shows the aggregation step using exact decimal arithmetic. A complete application also checks headers, validates missing values, handles returns, and defines currency rules.

**Web integrations:** a service often exchanges JSON. Example 08 demonstrates decoding and selecting records from a fixed payload. It makes no HTTP request. A live integration also needs timeouts, error handling, schema validation, and appropriate credential management.

**Database applications:** example 10 uses parameterized SQL to keep query data separate from query syntax. It creates an in-memory database, so its contents disappear when the connection closes. File-backed storage adds durability but also requires migration and backup decisions.

**Concurrent tasks:** example 13 simulates I/O with asynchronous waits. Concurrency lets other work proceed during a wait; it does not inherently make CPU-heavy Python calculations faster. Blocking work inside an async function can stall the event loop.

**Predictive modeling:** example 15 fits a line to four synthetic points. A perfect fit on invented data is not evidence that a model generalizes. Real modeling requires suitable measurements, held-out evaluation, error analysis, and a justified use case.

## When another tool may be a better fit

- Browser interfaces typically use JavaScript or TypeScript.
- Hard real-time systems and low-level memory control often call for systems languages.
- CPU-intensive loops may benefit from compiled extensions, vectorized libraries, or another runtime.
- Mobile applications usually need platform-specific tools or an additional framework.

Python can still coordinate components implemented in other languages.

## Explore the ecosystem

- [Python application overview](https://www.python.org/about/apps/)
- [Django documentation](https://docs.djangoproject.com/)
- [Flask documentation](https://flask.palletsprojects.com/)
- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [pandas documentation](https://pandas.pydata.org/docs/)
- [NumPy documentation](https://numpy.org/doc/)
- [Matplotlib documentation](https://matplotlib.org/stable/)
- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)
- [PyTorch documentation](https://docs.pytorch.org/docs/stable/index.html)
- [SciPy documentation](https://docs.scipy.org/doc/scipy/)
- [pytest documentation](https://docs.pytest.org/)
- [tkinter documentation](https://docs.python.org/3/library/tkinter.html)
- [Qt for Python documentation](https://doc.qt.io/qtforpython-6/)
- [Jupyter documentation](https://docs.jupyter.org/)
