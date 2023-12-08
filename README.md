<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url] 
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">nba_predictive_model</h3>

  <p align="center">
    Classifing NBA Players based on counting stats
    <br />
    <a href="https://github.com/genezaleski/nba_predictive_model/blob/master/Data%20Mining%20final%20Report.pdf"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

Data Mining Project Fall 2019

This project classifies an inputted statline of points, rebounds, and assists into categories such as all star, rebounder, playmaker,
scorer, and average nba player. To create this predictive model, I used the nba_py python module to scrape stats.nba.com for the stats of
the ~~3,000 unique players in the history of the nba. I processed this into a csv with player name, points, reb, assists, and would assign
a class to each player based on semi-arbitrary boundaries I thought of by looking at nba.com. These are used to train both Naive Bayes
and KNN classifers. For more, read the project spec file, "Data Mining Final Report.pdf"

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

[![Python][Python.link]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Python must be installed on this computer to execute some of the 
Installation instructions for python can be found <a href="https://www.python.org/downloads/">here.</a>

Relevant python libraries used for this project include:<br />
  ast 
  csv
  math
  nba_py
  os
  time

nba_py is used to scrape nba stats from stats.nba.com. It is not included in the default python installation. Please install it using pip:<br />

  /path/to/your/python -m pip install nba_py

Note: The nba_py library was a preferred method of scraping nba stats at the time of the creation of this project. For a more up to date scraping method, see the classify_nba_stats repo on my main page.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Relavent commands to get important data have been uploaded into a wrapping shellscript at the top level of this repository.

Please see driver.sh for more!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Gene Zaleski - zaleskig8@students.rowan.edu.com

Project Link: [https://github.com/genezaleski/nba_predictive_model](https://github.com/genezaleski/nba_predictive_model)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/genezaleski/nba_predictive_model.svg?style=for-the-badge
[contributors-url]: https://github.com/genezaleski/nba_predictive_model/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/genezaleski/nba_predictive_model.svg?style=for-the-badge
[forks-url]: https://github.com/genezaleski/nba_predictive_model/network/members
[stars-shield]: https://img.shields.io/github/stars/genezaleski/nba_predictive_model.svg?style=for-the-badge
[stars-url]: https://github.com/genezaleski/nba_predictive_model/stargazers
[issues-shield]: https://img.shields.io/github/issues/genezaleski/nba_predictive_model.svg?style=for-the-badge
[issues-url]: https://github.com/genezaleski/nba_predictive_model/issues
[license-shield]: https://img.shields.io/github/license/genezaleski/nba_predictive_model.svg?style=for-the-badge
[license-url]: https://github.com/genezaleski/nba_predictive_model/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gene-zaleski-56b2a0175
[product-screenshot]: images/screenshot.png
[Python.link]: https://img.shields.io/pypi/pyversions/Django?logo=python&logoColor=#3776AB
[Python-url]: https://www.python.org/
