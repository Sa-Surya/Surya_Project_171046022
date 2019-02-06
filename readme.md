Sentimentalytics

Twitter : Social Media and Text Analytics

(prediction of sentiment in english sentences)
 

 * Introduction

 * Requirements

 * Configuration

 * Execution

 * Troubleshooting

 * FAQ

 * Maintainers

 * License


INTRODUCTION
------------------

This project was aimed to implement four concepts, mainly distributed computing, machine learning, data retrieval and 

visualization. In the end, the results provide visual artifact on a given topic which can be used for later analysis.

Note: For detailed information on the project flow, please refer the report provided in the repository.


REQUIREMENTS
------------------

The modules require following packages and libraries for successful execution:

--------------------------------------------------------

 ***Python 2.7 or above***

 Can be found on the following link,

 https://www.python.org/downloads/

--------------------------------------------------------

 ***pip installer***

 (this is a package manager required to install other packages and libraries)

 command: python -mpip install -U pip

-------------------------------------------------------- 

 ***Tweepy***

 Install from PyPI:

 command: easy_install tweepy

 

 Install from source:

 commands:

 git clone git://github.com/tweepy/tweepy.git

 cd tweepy

 python setup.py install

--------------------------------------------------------

 ***TextBlob***

 command: pip install -U textblob

 To download necessary corpora:

 command: python -m textblob.download_corpora

--------------------------------------------------------

 ***Pandas***

 Installing from PyPI:

 command: pip install pandas

--------------------------------------------------------

 ***Numpy***

 Installing via pip:

 command: python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

 Install system-wide via a Linux package manager:

 command:
 
 sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python nose

 (above command also installs matplotlib and scipy)

--------------------------------------------------------

 ***Matplotlib***

 Install via pip:

 command: python -mpip install -U matplotlib

--------------------------------------------------------

Note: The above commands are for Linux distributions with an in-built terminal (command line interface) except for macOS. Alternative commands to install these packages and libraries for Windows and macOS can be found online in there respective documentation section of homepage.


CONFIGURATION
-------------------

Tweepy makes it easier to use the twitter streaming api by handling authentication, connection, creating and destroying the session, reading incoming messages, and partially routing messages.

Authentication:

In order to fetch tweets through Twitter Streaming API, one needs to register an App through the twitter account. Follow these steps for the same:

 1) Open this link:

    https://apps.twitter.com/ and click the button: ‘Create New App’

 2) Fill the application details. callback url field can be left empty.

 3) Once the app is created, the page will be redirected to the app page.

 4) Open the ‘Keys and Access Tokens’ tab.

 5) Copy ‘Consumer Key’, ‘Consumer Secret’, ‘Access token’ and ‘Access Token Secret’.

 Note: These four access tokens should be copied and replace the tokens inside config file in the project folder.


EXECUTION
-------------

The working has two phases,

1) Data retrieval using twitter streaming api.

2) Cleaning, Classifying and Visualizing the retrieved data.

 Phase 1: 
 
 --------

 Run the "streamTweets.py" module from terminal to fetch raw data from twitter which is in json format.
 
 command: python streamTweets.py
 
 Stop the script manually after collecting sufficient data.
 
 The retrieved data is stored in a .csv file which was given before execution.

 Phase 2:
 
 --------

 Run the "tweetAnalysis.py" module from the terminal to clean, classify and visualize the data which is in json format stored
 in the .csv file.

 command: python tweetAnalysis.py 


TROUBLESHOOTING
-----------------------

Disconnections:

For Twitter’s purposes, stream disconnections are grouped into two categories – client disconnections and forced disconnections.

1) Client disconnects

Client disconnects occur when the application independently terminates the connection to the data stream, whether because the code actively closes the connection, or where network settings or conditions terminate the connection.

2) Forced disconnects

Forced Disconnections occur when twitter's system actively disconnects client's app from the stream. There are 3 different types of forced disconnects.

   a) Full Buffer – app is not reading the data fast enough, or a network bottleneck is slowing data flow.

   b) Too many connections – established too many simultaneous connections to data stream in a short period.

   c) Server Maintenance – the Twitter team deployed a change or update to the system servers.


FREQUENTLY ASKED QUESTIONS - FAQ
--------------------------------------------

1) Why is there a error(disconnection) while fetching data?

Either the network connection is very poor or there is a forced disconnection from twitter's end. Depending on the severity, connections can be re-established either after 15 minutes or 24 hours later.

2) Why is the line chart(3rd graph) too dense?

Large amount of data plotted on that particular graph leads to very dense plot in both positive and negative ends. Zooming the graph can give significant difference.


MAINTAINERS
----------------

Current maintainers:

Surya Saravanan (Sa-Surya): https://github.com/Sa-Surya (surya.saravanan10@gmail.com)

Eldridge Gomes (eldgomes): https://github.com/eldgomes (gomes.eldridge@gmail.com )

This project was done under the guidance of:

Deepak Rao B

Assistant Professor – Selection Grade

School of Information Sciences

Manipal University, Manipal, India.


LICENSE
----------

This project is a open-source and is free to use in the public domain.
