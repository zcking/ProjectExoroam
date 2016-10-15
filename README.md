# Project ExoRoam
An open-source interactive map of the universe. 

Note: you can view this site at https://zach-king.github.io/ProjectExoroam/

---

## The Concept
The idea for Project ExoRoam is to use the open data that has been collected on extra-solar 
planets to produce a fully interactive map interface of our solar system--our entire known 
universe even. Imagine Google Maps, but with the entire universe. Currently, there are 
two developers working on this project--moi and [@andersy005](https://github.com/andersy005). 

---

## Technical Background
I am not an expert in astronomy, space exploration, or other topics of that sort, so I must 
do a fair amount of research prior to implementing the fine-grain details of this project. 
As far as the technical background however, I will be using the 
[Open Exoplanet Catalog](https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue) 
as my primary source for data. The interface must be interactive and web-based. 

---

## Todo
Keep in mind I am one person and can't work on this 24/7...
* Design initial web UI with D3
    * Base it off of this example? : https://bl.ocks.org/mbostock/7607535
* Design graph or other data structure to contain the planetary data
* Optimize planetary container to only use data being requested at the time (i.e. only 
load the solar system being looked at)
* Minimap? 
* Orbital lines for each planet?