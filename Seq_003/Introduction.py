"""
EEG Analysis Tool

This program assists in analyzing and visualizing EEG (Electroencephalogram) data 
to detect patterns associated with various cognitive states or neurological conditions.

Student ID: 2546414
"""

import textwrap
def display_introduction():
  intro_text = """
  Welcome to the EEG Analysis Tool

  This program is designed to assist the streamlining of the process of analyzing EEG data,
  making it easier for scientists to extract meaningful insights from complex brain activity recordings.

  Key features:
  - Automated preprocessing of EEG data
  - Advanced filtering techniques
  - Feature extraction (e.g. power spectral density, coherence)
  - Interactive visualizations
  - Statistical analysis of EEG features

  Applications:
  - Identifying markers of neurological disorders such as epilepsy, Alzheimer's
  - Studying cognitive processes such as memory retention and decision making processes
  - Developing brain-computer interfaces for assistive technologies

  Key aim
  - To reduce time spent on the time-consuming yet critical process of EEG data analysis, 
  allowing researchers to focus more on interpreting results and advancing their understanding of brain functions.
  """
  print(textwrap.dedent(intro_text))

display_introduction()
