# QMISC
 

<div align="center">

  <a><img src="https://badges.aleen42.com/src/cli.svg" width="6.5%"/></a>
  <a><img src="https://img.shields.io/badge/Python3.9+-FFD43B?style=for-the-badge&logo=python&logoColor=blue" width="11.5%"/></a>
  <a href="https://opensource.org/licenses/MIT" target="_blank"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat" alt="MIT License"/></a>

</div>

---



# QMISC

<div align="center">
  <img src="./doc/images/QMISC_logo.png" width="80%"/>  
</div>

# Table of contents

- [Introduction](#Introduction)
- [Installation](#Installation)
- [Algorithm](#Algorithm)
- [Implementation of QMISC](#Implementation-of-QMISC)
- [Supporting this project](#Supporting-this-project)
- [Contacts](#Contacts)
- [Licence](#Licence)
- [cite QMISC](#cite-QMISC)
- [References](#References)

# Aims
[Go to the top](#Table-of-contents)

<div>
<img src="./doc/images/algorithm.png" width="60%" align="right"/>

QMISC is a user-friendly command-line interface (CLI) software that enables quantifying mutation-induced surface changes from PDB files.
</div>


# Installation
[Go to the top](#Table-of-contents)

### Requirements

QMISC is a CLI tool that runs on all OS system. It is written in python (version 3.9). It relies on the already included Graphein software ([1](#ref-1)) and ESM ([2](#ref-2)).

<details>
<summary><b>For a usage on your local OS</b></summary>

- an UNIX-based OS system (any linux distribution, a MacOS system or [WSL2](https://learn.microsoft.com/fr-fr/windows/wsl/install) on windows)
- [Python >= 3.9](https://www.python.org/downloads)
 
</details>
<br>



## How to install QMISC
[Go to the top](#Table-of-contents)

First, make sure you meet the [system requirements](#requirements) outlined earlier and consider the [recommendation](#recommendation). Then, follow instructions described in option 1.
<a id="install_option1"></a>
<details open>
<summary><h4>Option 1: from the pip (git not required)</h4></summary>

```bash
# upgrade pip to its latest version
python -m pip install --upgrade pip

# install QMISC vx.x.x
pip install QMISC
```
</details>


# How it works
[Go to the top](#Table-of-contents)


### QMISC workflow: inputs/outputs

<div align="center">
  <img src="./doc/images/QMISC_workflow.png" width="70%"/>

<i>The figure above represents the main steps of the QMISC worflow to quantify mutation-induced surface changes from PDB files. More details about each step can be found in our article: see the [published version]()</i>
</div>
<br>

QMISC accepts as input a *PDB file*.
<br>
<br>

[Using a PDB file as input](#from-a-pdb-structure) is the usage of QMISC. In this case, two outputs are generated: 
- the graph representation of PDB files.
- a statistical plot showing the quantification of mutation-induced surface changes.

<br>
<br>


# Usage of QMISC
[Go to the top](#Table-of-contents)

Once you have [installed the QMISC package](#how-to-install-QMISC), you should be ready to use QMISC. 

#### The example directory
To guide the user in the usage of QMISC, we will make use of files that you can find in the `example/` directory of QMISC.

#### QMISC options

<!-- <details> -->
<!-- <summary>List of all QMISC options</summary> -->

<!-- <pre>usage: QMISC [-h] (-pdb PDB | -mat MAT | -v) -tomap TOMAP [-proj PROJ] [-res RES] [-rad RAD] [-d D] [-s S] [--nosmooth] [--png] [--keep]
               [--docker] [--pqr PQR] [-ff FF] [-verbose VERBOSE]

options:
  -h, --help        show this help message and exit
  -pdb PDB          Path to a PDB file
  -mat MAT          Input matrix. If the user gives an imput matrix, QMISC will directly compute a map from it.
  -v, --version     Print the current version of QMISC.
  -tomap TOMAP      Specific key of the feature to map. One of the following: stickiness, kyte_doolittle, wimley_white, electrostatics,
                    circular_variance, bfactor, binding_sites, all.
  -proj PROJ        Choice of the projection. Argument must be one of the following: flamsteed, mollweide, lambert. Defaults to flamsteed.
  -res RES          File containing a list of residues to map on the projection. Expected format has the following space/tab separated column
                    values: chainid resid resname
  -rad RAD          Radius in Angstrom added to usual atomic radius (used for calculation solvent excluded surface). The higher the radius the
                    smoother the surface. Defaults to 3.0
  -d D              Output directory where all files will be written. Defaults to &apos;./output_QMISC_$pdb_$tomap&apos; with $pdb and $tomap based on
                    -pdb and -tomap given values
  -s S              Value defining the size of a grid cell. The value must be a multiple of 180. Defaults to 5.0.
  --elec-max-value ELEC_MAX_VALUE
                        Maximum value to be used for the electrostatics color scale. The value will be converted as an absolute value to make the scale symetric around 0. For
                        instance, a value of 5.63 will scale the electrosctatics color values from -5.63 to 5.63.
  --bfactor-min-value BFACTOR_MIN_VALUE
                        Minimum value to be used for the bfactor color scale.
  --bfactor-max-value BFACTOR_MAX_VALUE
                        Maximum value to be used for the bfactor color scale.
  --nosmooth        If chosen, the resulted maps are not smoothed (careful: this option should be used only for discrete values!)
  --png             If chosen, a map in png format is computed (default: only pdf format is generated)
  --keep            If chosen, all intermediary files are kept in the output (default: only final text matrix and pdf map are kept)
  --docker          If chosen, QMISC will be run on a docker container (requires docker installed).
  --pqr PQR         Path to a PQR file used for electrostatics calculation. Option only available if &apos;-tomap electrosatics&apos; is requested.
                    Defaults to None.
  -ff FF            Force-field used by pdb2pqr for electrostatics calculation. One of the following: AMBER, CHARMM, PARSE, TYL06, PEOEPB,
                    SWANSON. Defaults to CHARMM.
  -verbose VERBOSE  Verbose level of the console log. 0 for silence, 1 for info level, 2 for debug level. Defaults to 1.
</pre>
</details>


## Projection of a protein surface feature on a 2D map

In order to generate a 2D map projection of a protein surface feature, two inputs are required:
- either a PDB file (`-pdb` option) OR a matrix text file written in a QMISC-specific format (`-mat` option)
- a valid key referring to a feature to map (listed in the table below)

| Valid feature key | Feature details |
| --- | --- |
`kyte_doolittle` | Residue hydrophobicity directly derived from the Kyte-Doolittle scale ([3](#ref-3))
`wimley_white` | Residue hydrophobicity directly derived from the Wimley-White scale ([4](#ref-4))
`stickiness` | Propensity of each amino acid to be involved in protein−protein interfaces ([5](#ref-5))
`circular_variance` | Descriptor of the local (residue scale) geometry of a surface region: low values reﬂects protruding residues, while high values indicates residues located in cavities ([6](#ref-6))
`circular_variance_atom` | Descriptor of the local geometry (atomic scale) of a surface region: low values reﬂects protruding atoms, while high values indicates atoms located in cavities. ([6](#ref-6))
`electrostatics` | Electrostatic potential of the protein surface (atomic scale) - Requires the APBS software ([2](#ref-2))
`bfactor` | Any feature stored in the temperature factor of the input PDB ﬁle
`all` | Compute sequentially the following features: `kyte_doolittle`, `wimley_white`, `stickiness` and `circular_variance`

#### From a PDB structure

```bash
# example - command to map the stickiness values for residues at the surface of the chain A of 1g3n.pdb
QMISC -pdb 1g3n_A.pdb -tomap stickiness --docker
```

The output has the following structure and content:
<pre><font color="#12488B"><b>output_QMISC_1g3n_A_stickiness/</b></font>
├── <font color="#12488B"><b>maps</b></font>
│   └── 1g3n_A_stickiness_map.pdf
├── parameters.log
├── QMISC.log
└── <font color="#12488B"><b>smoothed_matrices</b></font>
    └── 1g3n_A_stickiness_smoothed_matrix.txt
</pre>

with:
- `parameters.log`: a summary of the parameters used to compute the map
- `QMISC.log`: a log file of each of the step of the QMISC workflow
- `1g3n_A_stickiness_map.pdf`: the generated 2D map in PDF format
- `1g3n_A_stickiness_smoothed_matrix.txt`: a computed smoothed matrix file (txt file) used to generate the 2D map. This matrix has the expected format of a matrix file that can be used as a direct input of QMISC through the used of the `-mat` argument.
 -->


# Supporting this project
[Go to the top](#Table-of-contents)

- If you find a bug or have a suggestion for a new feature, please report it via an [issue](https://github.com/DUAN-GAO/QMISC/issues)
- If you find QMISC useful, consider starring the repository or donate via `Bitcoin` bitcoin address 0xf815a71225f9935cde182c3ef555252bda31eef8 (BNB Smart Chain)



# Contacts
[Go to the top](#Table-of-contents)

If you have any question regarding QMISC, you can contact us:
- [@gaoduan666@gmail.com](mailto:gaoduan666@gmail.com) (project leader)
- [@zn1@sanger.ac.uk](mailto:zn1@sanger.ac.uk) 
- [@yiqiangz@cau.edu.cn](mailto:yiqiangz@cau.edu.cn) 


# Licence
[Go to the top](#Table-of-contents)

This project is under the MIT License terms. Please have a look at the LICENSE file for more details.


# How to cite QMISC
[Go to the top](#Table-of-contents)

If QMISC has been useful to your research, please cite us:

> Duan Gao, Zemin Ning, Yiqiang Zhao. Mapping the Allosteric Landscape: Quantifying Mutation-Induced Surface Changes with Graph Neural Networks. Front. Bioinform. 2025. [Link]()


<br>

# References
[Go to the top](#Table-of-contents)

<a id="ref-1"></a>

> (1) Jamasb, Arian & Lio, Pietro & Blundell, Tom. (2020). Graphein - a Python Library for Geometric Deep Learning and Network Analysis on Protein Structures. 10.1101/2020.07.15.204701. 


<a id="ref-2"></a>

> (2) Lin Z, Akin H, Rao R, Hie B, Zhu Z, Lu W, Smetanin N, Verkuil R, Kabeli O, Shmueli Y, Dos Santos Costa A, Fazel-Zarandi M, Sercu T, Candido S, Rives A. Evolutionary-scale prediction of atomic-level protein structure with a language model. Science. 2023 Mar 17;379(6637):1123-1130.


<a id="ref-3"></a>

> (3) Berman HM, Westbrook J, Feng Z, Gilliland G, Bhat TN, Weissig H, Shindyalov IN, Bourne PE. The Protein Data Bank. Nucleic Acids Res. 2000 Jan 1;28(1):235-42.

