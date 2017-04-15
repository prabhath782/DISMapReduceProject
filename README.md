#MapReduce Project

Team members :  Suresh Kumar Madugula,Prabhath Teja Kommirisetty
Project-Course: 44-564. Design of Data Intensive Systems

Contributors Client Denise Case, PhD, PE, Assistant Professor, Assistant Coordinator, Masters of Applied Computer Science Program, School of Computer Science and Information Systems, Colden Hall 2280, Northwest Missouri State University. dcase@nwmissouri.edu https://www.linkedin.com/in/denisecase

Faculty:Dr.Denise Case
Assistants:Sai Sri Ravali Chinthareddy, Course Assistant

Prerequisites:
VMWare,Python should be installed on working system, Any Text editor( Notepad++ is recommended).
Recommended links to  download Software
VMWare:https://www.virtualbox.org/wiki/Downloads
Python:https://www.python.org/download/releases/2.6.6/ ( For current project  worked on python version 2.6.6)
Notepad++: https://notepad-plus-plus.org/download/v7.3.3.html

Our dataset is a subset of data on migraine treatments collected by Tammy Kostecki-Dillon. In our current project we trying to find about the age groups of people and their medication type and headtype.

Working with the Project:

Overview: Desired fields data is retrieved by using mapper program on input dataset. Output from mapper program is sorted & shuffled before passing it to the reducer program. In reducer program, we apply various  functions to get the desired results.
  
 Repository creation and working(Cloning, changes): https://www.youtube.com/watch?v=73I5dRucCds
 
Mapper, Reducer for data set:

Run commands in command prompt( open command prompt as administratorn by selecting the sourrce folder contaning the files) Mapper: python Smapper.py Reducer: python Sreducer.py

Mapper:

![mapper](https://cloud.githubusercontent.com/assets/25209715/25059669/6cb8a56c-2150-11e7-8ea1-065542ebc3d9.PNG)


Reducer:

![reducer](https://cloud.githubusercontent.com/assets/25209715/25059638/e70fed9e-214f-11e7-9e1f-f2cb8160b8c5.PNG)


Results Graph:





References:
Course Slides,
https://blog.matthewrathbone.com/2013/11/17/python-map-reduce-on-hadoop-a-beginners-tutorial.html
