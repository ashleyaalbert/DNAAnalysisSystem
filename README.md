# 311-group-project


## DNA Analysis System
This project analyzes a DNA sequence against a DNA query to find similarities. The way these pieces of DNA are matched is up to the user! Choose between different algorithms, such as longest common subsequence or edit distance, to see the matches you get!

## Description
The DNA Analysis System allows for a user to analyze DNA sequences against a DNA query. The user will be welcomed and prompted to either enter their own files or use the current system's files. These files will be checked to ensure they are valid. The user will then be prompted to select an algorithm to go through the DNA. The possible options include Longest Common Substring, Longest Common Subsequence, Edit Distance, Needleman-Wunsch Algorithm, and Substring Alignment and Frequency Algorithm. The algorithm selected will then return a score and what DNA sequence best matches the DNA query. The user will then be prompted to continue by choosing another algorithm or quitting the system.  

## Installation
In order to run this code, ensure that you have a recent version of Python3 downloaded onto your machine. 

## Downloading the repository
To download this repo, simply clone the project using the URL below or download the zip file on the gitlab page under "Code", found here: https://gitlab.bucknell.edu/kbw011/311-group-project.

```
# Clone the repo
cd repo_location
git clone https://gitlab.bucknell.edu/kbw011/311-group-project.git
```

## Run the code  
Once the repo is downloaded, ensure that you are in the directory with the project files. From there, type ```python3 interface.py``` into the terminal to run the code. You will then be prompted to enter input in the terminal.  

## Interact with the code  
Once ```interface.py``` is running, you will be prompted to choose which query and sequence files to use in running the algorithms. Type ```y``` to use the default files or type ```n``` to use additional text files within the folder.   

You will then be prompted to choose one of five algorithms in order to generate matching DNA sequences. Entering a number 1 through 5 will use the corresponding algorithm to generate matches. Output will be generating describing how well the query performed against the sequence, the closer to 1.0 the better. The most similar sequence/query match will be printed at the end.  

You will then be prompted to enter another algorithm to analyze the DNA with or quit the program. Entering ```y``` will bring you back to the previous algorithm choices.  

## Usage
One example of the use of this system is as follows:
If you opt to use the system files and select option 3, Edit Distance, the expected output will return:

All Scores:

SCORE: (0.5604472396925226) : NC_000011.10:c2161209-2159779 Homo sapiens chromosome 11, GRCh38.p13 Insulin


SCORE: (0.43986254295532645) : NT_176377.1:12394966-12397002 Guinea pig insulin gene


SCORE: (0.5191717791411044) : V00179.1 Dog gene encoding insulin


SCORE: (0.8071553228621291) : V01243.1 Rat gene for insulin 2


SCORE: (0.4817927170868347) : AY092023.1 Gorilla gorilla insulin gene, partial cds


SCORE: (0.4715219421101774) : NC_052536.1 Gallus gallus isolate bGalGal1 chromosome 5, Insulin


SCORE: (0.27472527472527475) : NC_045512.2:21563-25384 SARS-Cov-2 - surface spike protein


SCORE: (0.48351648351648346) : NC_002018.1:21-1385 Influenza A virus (A/Puerto Rico/8/1934(H1N1)) segment 6, neuraminidase 


SCORE: (0.455026455026455) : NC_007366.1:30-1730 Influenza A virus (A/New York/392/2004(H3N2)) segment 4, hemagglutinin    


SCORE: (0.4771241830065359) : MH537830.1 Streptococcus pyogenes strain SH2902A RopB-like (ropB) genes



MOST SIMILAR:
V01243.1 Rat gene for insulin 2


## Authors and acknowledgment
Authors of this project include Ashley Albert, Charlie Ehrbar, Sam Vickers, and Katrina Wilson.

