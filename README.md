MAST-U Validation (FreeGSNKE vs. Fiesta vs. EFIT++)
====================================================

Aims
----------

The aim of this work was to:

1. validate that the static forward equilibrium solver in FreeGSNKE (and Fiesta) can simulate the equilbria produced by a magnetics-only EFIT++ reconstruction on the MAST-U tokamak.
2. compare poloidal flux quantities, shape control measures (e.g. midplane radii, magnetic axis, separatrix positions), and other targets (e.g. X-points, strikepoints) from both solvers for a few different MAST-U shots using EFIT++ as the reference solution. 


Installation requirements
----------

To re-run the notebooks/scripts in the repository you'll need to be able to:

1. Clone this repository. 
2. Install FreeGSNKE (and FreeGSfast).
3. Optional: install Fiesta (available, possibly with permisiion, from https://git.ccfe.ac.uk/kpentlan/Fiesta). 

Where to start
----------

 - After installation, try to run the Python scripts in the 'freegsnke' directory. These should be able to re-generate the results in the paper using FreeGSNKE only.
 - The Fiesta simulation results used in these Python scripts have already been generated and stored in '.mat' files in the 'data' directory. 
 - If you have access and can run Fiesta, you can also run the Fiesta scripts in the 'fiesta' directory. 
 - To do this you will need to open the 'startup.m' file in 'fiesta' and change the 'home' path to the directory where your Fiesta installation exists.

If the above steps don't work, please do get in contact. 


References
----------

* K. Pentland, N. C. Amorisco, O. El-Zobaidi, S. Etches, A. Agnello, G. K. Holt, C. Vincent, J. Buchanan, S. J. P. Pamela, G. McArdle, L. Kogan, and G. Cunningham. Validation of the static forward Grad-Shafranov equilibrium solvers in FreeGSNKE and Fiesta using EFIT++ reconstructions from MAST-U. In preparation. 2024. 

* N. C. Amorisco, A. Agnello, G. Holt, M. Mars, J. Buchanan, and S. Pamela. FreeGSNKE: A python-based dynamic free- boundary toroidal plasma equilibrium solver. Physics of Plasmas, 31(4):042517, 2024. doi:10.1063/5.0188467.

* A. Agnello, N. C. Amorisco, A. Keats, G. K. Holt, J. Buchanan, S. Pamela, C. Vincent, and G. McArdle. Emulation techniques for scenario and classical control design of tokamak plasmas. Physics of Plasmas, 31(4):043901, 2024. doi:10.1063/5.0187822.