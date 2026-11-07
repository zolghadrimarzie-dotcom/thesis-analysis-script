markdown
#Thesis Data Analysis and Visualization pipeline
## Overview
This repository contains python_based data processing and visualization scripts developed for two tables of my master's thesis research in teaching English as a Foreign Language
## Context and Supervision
**Supervisor:** Dr.Shiva Kayvanpanah
**Researcher: Marzieh Zolghadri
**Field of Study:**Teaching English(A Needs Analysis of Hardware and Software Engineering Students)
##Key Features
-**Modular Data Setting('data_setting'): A custom function designed to ingest row data dictionaries, convert them into 'pandas'
-** Advanced Pandas Configuration;**Optimized display settings('max_columns' and 'width') to handle wide statistical tables cleanly in the terminal or IDE output.
-** Automated Bar Chart Generation('draw_bar_chart'):** A dynamic plotting function using 'matplotlib' that accepts custom column parameters('x_axis') to render,format and save publication-quality figures at '300 dpi'.
## Tech Stack 
-**language:** Python
-**Libraries:**
-'pandas' (data manipulation and structuring)
-'matplotlib' (Data visualization and plotting)
## Repository Structure
'''text
thesis_analysis.py       # Main script containing data structure and processing functions
README.md                # Project documentation
.gitignore               # Excluded local/temporary files
Usage
1.Ensure required libraries are installed
bash
    pip install pandas
    pip install matplotlib
2. Run the analysis script in PyCharm or any standard Python programming environment