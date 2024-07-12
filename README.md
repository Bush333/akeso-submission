# Akeso-submission

Paper Implementation : http://jcse.kiise.org/files/V17N2-01.pdf

Dataset : http://datasets.d2.mpi-inf.mpg.de/MPIIGaze/MPIIGaze.tar.gz
          http://datasets.d2.mpi-inf.mpg.de/MPIIGaze/MPIIFaceGaze.zip

Steps :
We need to first download and extract the MPIIGaze and MPIIFaceGace dataset
  1.  python3 download_extract_dataset.py
  2.  python3 prepare_and_process_data.py
  3.  Execute final-ptge.ipynb  [ Implementation of Gaze Model, Calibration Model, Spaze Models. Training and Validation over clean and corrupted data ]
        a.  The outputs/results are stored in ptge_spaze_comparison_results.csv
  4. Execute ptge-spaze-evaluation-on-varied-callibration-params.ipynb
        b.  The outputs/results are stored in ptge_spaze_robustness_results.csv


Limitations:
Though there are 15 subjects in the dataset, only 3 were considered. The leave-out strategy was also applied to one subject.
This was done due to less computational resources and limited time for execution
The keywords "TODO" highlights places where we can increase the number of subjects and also apply the leave-out strategy to other subjects if we have better resources available.

Though we have implemented on limited dataset, it was made sure to capture the experiments of the paper
