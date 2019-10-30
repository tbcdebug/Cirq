import sys

raise SystemError(
    '\n'
    'Cirq no longer supports python ' + sys.version + '.\n'
    '\n'
    'You can either:\n'
    '\n'
    '1. UPDATE TO PYTHON 3.6 OR LATER\n'
    '2. INSTALL AN OLDER VERSION OF CIRQ LIKE THIS:\n'
    '        python -m pip install cirq==0.5.0'
)
