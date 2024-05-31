# Strong Thermal Emissions Velocity Enhancements (STEVE)

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
![image](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![image](https://img.shields.io/badge/SciPy-654FF0?style=for-the-badge&logo=SciPy&logoColor=white)
![image](https://img.shields.io/badge/LaTeX-47A141?style=for-the-badge&logo=LaTeX&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

## Description

This project was done in association with the Solar-Terrestrial Research Department(CSTR) in the New Jersey Institute of Technology (NJIT) and was purposely crafted to find the phenomenon *STEVE*.

>**The Strong Thermal Emission Velocity Enhancement** (STEVE) is a type 
of phenomenon that appears as a night-time mauve emission, equatorward of the auroral oval, during strong plasma flows. They extend thousands of kilometers in the east-west direction and only tens of kilometers in the north-south direction.

Just a few notes about the event:
* PFISR observations near a STEVE event show an ion temperature enhancement parallel to the magnetic field.
* This is consistent with our understanding of STEVE events and their relationship to SAIDs, as well as the time-scales behind ion-neutral frictional heating [Goodwin et al, 2014].

## Methodology

To find a ion temperature enhancement, our algorithm searches for points that are bigger in ¨alue when compared to the preceding and subsequent points. It then filters out enhancements that are not larger than the collective standard de¨iation multiplied by a factor of 3.5.

<img src="./assets/methodology_graph.png">

>[!NOTE]
>Above is an example of "ion temperature enhancements" on an arbitrary dataset.

To filter out possible enhancements due to noise, enhancements must be observed at both 240 and 275 km altitude. These enhancements are then filtered by looking for the presence of “STEVE-like” structures in Swarm spacecraft data (see poster MDIT-3). This algorithm is applied to PFISR ion temperature data spanning between the years of 2014-2016.

<img src="./assets/240km.png">

>[!NOTE]
>Above is the Magnetic Local Time(MLT) graph of Ion temperature enhancements at the altitude of 240 km.

<img src="./assets/275km.png">

>[!NOTE]
>Above is the MLT graph of Ion temperature enhancements at the altitude of 275 km.

## Results

<img src="./assets/filtered_275.png">

The following project was also utilized in preparation for the CEDAR workshop in 2023 in San Diego, CA.
<object data="./assets/poster.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="http://yoursite.com/the.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="http://yoursite.com/the.pdf">Download PDF</a>.</p>
    </embed>
</object>
