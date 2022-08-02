# VISSOFT2022
This repository contains material and data of the experiment described in our (Falko Galperin, Rainer Koschke, Marcel Steinbeck) VISSOFT 2022 publication "Visualizing Code Smells: Tables or Code Cities? A Controlled Experiment".

## Included files
- **[`_Vissoft2022CodeSmellsCodeCities.pdf`](_Vissoft2022CodeSmellsCodeCities.pdf)**: The paper submitted to Vissoft 2022.
- **[`BachelorThesis.pdf`](BachelorThesis.pdf)**: The original bachelor thesis describing the paper's experiment as well as the implementation of the code smell visualization
    in SEE in more detail, though it's written in German. 
- **[`calc_results.R`](calc_results.R)**: An R script which outputs all relevant results (e.g., from the Mann-Whitney-U tests) and generates all PDFs used in the paper and original bachelor thesis.
- **[`Common-Eval.xlsx`](Common-Eval.xlsx)**: The questionnaire (including the tasks themselves) in a format compatible with the survey tool [KoBoToolbox](https://www.kobotoolbox.org). 
    Note that this contains both the questionnaire for group alpha (SEE->Dashboard) and beta (Dashboard->SEE) concatenated together,
    whereas these two questionnaires are divided by the invisible field title "HIER AUFHÖREN".
- **[`Dashboard_SEE.csv`](Dashboard_SEE.csv)**: Contains raw data for the above questionnaire for each participant, including task results.
    Columns `dsus` resp. `ssus` contain the SUS questions for the Axivion Dashboard resp. SEE.
    At the end, columns with `_c` suffixes have been appended which specify the correctness of each answer for the respective question.
    Various timestamps are included which describe the time a respective field was last edited, this was used to determine the time participants
    took to solve a task ($\max(t_2, t_3, \ldots, t_n) - t_1$, whereas there are $n$ fields and $t_i$ contains the timestamp for field $i$.).
- **[`Dashboard-Solution.txt`](Dashboard-Solution.txt)**: Solution for the Dashboard tasks. These were automatically calculated by the `findDash.py` script.
- **[`DashboardUseCases.txt`](DashboardUseCases.txt)**: An anonymized listing of Axivion employees' descriptions of possible use cases for the Axivion Dashboard.
- **[`findCorrelation.py`](findCorrelation.py)**: A python script which calculates Pearson correlation coefficients between architecture, style, and metric violations.
- **[`findDash.py`](findDash.py)**: A python script which calculates the solution for the Dashboard tasks. Output is contained in `Dashboard-Solution.txt`.
- **[`SEE-Solution.txt`](SEE-Solution.txt)**: Solution for the SEE tasks. These were manually determined by using the Unity Editor.
- **[`Visualizing code smells in SEE.mp4`](Visualizing code smells in SEE.mp4)**: This is a short demonstration of how code smells are visualized in the Code City software SEE. 
    The Code City used as a basis here is the source code of SEE itself.
    The smells are visualized as icons above each node, whereas the red tint of an icon shows the relative occurrence of that kind of code smell within its level. 
    At the bottom, key inputs are shown to demonstrate how SEE can be controlled.
    This video has been shown to participants of the study.
