# this will convert scrapper from jupyter notebook to python which makes it easier to run from command line and receive standard out 
cd ..
jupyter nbconvert --to script ./init.ipynb
jupyter nbconvert --to script ./nifty_matrix_scrapper.ipynb
