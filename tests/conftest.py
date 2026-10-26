from hypothesis import settings

# Fixed profile so property tests give the same result on every CI run.
# derandomize=True makes Hypothesis pick examples from the test's own code, not a random seed.
settings.register_profile("ci", max_examples=100, derandomize=True, deadline=None)
settings.load_profile("ci")
