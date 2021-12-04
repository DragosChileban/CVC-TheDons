# Car Accident Repair Cost Estimation
A CVC "The Dons" Final Project
## General Info
The car accident repair cost averages can vary depending on a lot of factors. Minor repairs can cost around $300 to $800 but the price could go up to $1,500 if it needs repaint. If the damage on the car affects its drivability, the repair cost can start somewhere at $4,000 but if the damage leaves it undrivable, it can go up to $6,000 or more.
No matter how careful you are, accidents can happen. So even if you haven’t been in an accident – we hope you won’t ever be in one – it is a good idea to know about car accident repair cost averages so you can prepare for it and will have an idea what to expect when it happens.
The main goal of this study is identifying the vehicle repair costs following road accidents in order to estimate the amount spent by users. Other goals are:
* Filter identify, analyse and filter relevat information from different datasets
* Facilitate the customer decision making process when estimating repair cost and services required
* Create an intuitive mobile application using the constructed model and data
### Data Analysis
The model is constructed on a [car models dataset](https://datasets.bifrost.ai/info/1077) the can be [downloaded here](https://www.dropbox.com/s/uwa7c5uz7cac7cw/VMMRdb.zip?dl=0), as well as a [car damage dataset](https://peltarion.com/knowledge-center/documentation/terms/dataset-licenses/car-damage). The application offers [repair shops info](https://keycollisioncenter.com/) that provide the required repair services as well as the range of prices that the user can use as a reference.
## Technologies
Java, Python, Flask
### Python Libraries 
* PyTorch, Numpy, Pandas, scikit-learn
### Java Packages and Libraries
* Okhttp3
## Models Accuracy
* Car Model Recognition: Accuracy(0.93), F1_mean(0.93)
* Damage Detection Model: Accuracy(0.84), F1_mean(0.83)
## Installation process:
* Install the Android App on your device or run it on an emulator
* Run the app.py script from the "Flask" directory
