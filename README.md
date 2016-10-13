# Project ExoRoam
An open-source interactive map of the universe.

---

## The Concept
The idea for Project ExoRoam is to use the open data that has been collected on extra-solar 
planets to produce a fully interactive map interface of our solar system--our entire known 
universe even. Imagine Google Maps, but with the entire universe. Is the scope of this 
project too large for just one developer (moi)? Probably, but hey, it's possible, someone should 
do it, and I can...so why not? 

---

## Technical Background
I am not an expert in astronomy, space exploration, or other topics of that sort, so I must 
do a fair amount of research prior to implementing the fine-grain details of this project. 
As far as the technical background however, I will be using the 
[Open Exoplanet Catalog](https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue) 
as my primary source for data. The graphical interface has yet to be designed, but should 
be very simple yet able to display/translate to other solar systems and such. At the moment 
I am not concerned with cross-platform compatibility--especially since I would rather make 
this a web application on down the road. The application will keep a local cached copy of the 
open exoplanet catalog for offline use, but otherwise will request the copy online in order 
to keep the data up-to-date.

---

## Todo
Keep in mind I am one person and can't work on this 24/7...
* Design initial web UI with D3
* Design graph or other data structure to contain the planetary data
* Optimize planetary container to only use data being requested at the time (i.e. only 
load the solar system being looked at)
* Minimap? 