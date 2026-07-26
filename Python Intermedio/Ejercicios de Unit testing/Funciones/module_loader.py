import importlib.util
from unittest.mock import patch


def load_module_from_file(module_name, file_path, mock_input_value="placeholder"):
    """Load a .py file as a module without blocking on top-level input()/print() calls.

    The exercise files run demo code (input/print) at module level, since they
    are not guarded by `if __name__ == "__main__":`. To import them safely for
    testing, we mock input() so it returns a placeholder value and silence
    print() so the demo output doesn't clutter the test results.
    """
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)

    with patch("builtins.input", return_value=mock_input_value), patch("builtins.print"):
        spec.loader.exec_module(module)

    return module
