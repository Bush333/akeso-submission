# Akeso-submission

Paper Implementation : http://jcse.kiise.org/files/V17N2-01.pdf

Dataset : 
          1.  http://datasets.d2.mpi-inf.mpg.de/MPIIGaze/MPIIGaze.tar.gz
          2.  http://datasets.d2.mpi-inf.mpg.de/MPIIGaze/MPIIFaceGaze.zip

Steps :
We need to first download and extract the MPIIGaze and MPIIFaceGace dataset
  1.  Install all the packages mentioned in requirements.txt
  2.  python3 download_extract_dataset.py
  3.  python3 prepare_and_process_data.py
  4.  Execute final-ptge.ipynb  [ Implementation of Gaze Model, Calibration Model, Spaze Models. Training and Validation over clean and corrupted data ]
        a.  The outputs/results are stored in ptge_spaze_comparison_results.csv
  5. Execute ptge-spaze-evaluation-on-varied-callibration-params.ipynb
        a.  The outputs/results are stored in ptge_spaze_robustness_results.csv
  6. Execute angular-error-analysic.ipynb to get analysis of angular errors for ptge and spaze models
        a. The outputs/results are stored in : ptge_spaze_angular_error_results-variations-calibration-params.csv  and   ptge_spaze_angular_error_results-clean-corrupted-data.csv  


Limitations:
Though there are 15 subjects in the dataset, only 3 were considered. The leave-out strategy was also applied to one subject.
This was done due to less computational resources and limited time for execution
The keywords "TODO" highlights places where we can increase the number of subjects and also apply the leave-out strategy to other subjects if we have better resources available.

Though we have implemented on limited dataset, it was made sure to capture the experiments of the paper
