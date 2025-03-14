## Note and Instrument Identification

### Project description:

For this project my focus was to create a model that can take an audio wav file of an instrument being played and identify what instrument it is and what note is being played on that instrument. The ideal application of this model would be to assist in creating sheet music from a recording. 

### 1. The Data

Magenta has created a audio dataset called the [NSynth Dataset](https://magenta.tensorflow.org/datasets/nsynth#note-qualities), aimed at giving data scientists an entry point into the field of audio machine learning. This dataset contains 4 second audio clips of various instruments playing notes found on a standard MIDI 0-scale. Each sample comes pre-classified with the pitch of the note and name of the instrument being played. Using this data, we can extract information from the audio sample and create various supervised machine learning algorithms to identify the note and instrument. The full dataset contains over 300,000 classified audio samples, however for this project we will be working with a subset of roughly 12,600 of these samples. 

As we can see from the Spectrograms (graphs that display the amplitudes of the frequency components of an audio signal over time) of a selection of samples from the data, frequencies can vary greatly by instrument and the pitch of the sound being played. Higher notes result in higher frequencies being emitted, and each instrument emits a unique combination of frequencies at various amplitudes(loudness) that combine to make up the note being played.

<center><img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/guitar_bass_spec.png?raw=true"/></center>

<center><img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/mallet_keyboard_spec.png?raw=true"/></center>

There are several quantifiable metrics we can pull from these audio files that can help train our algorithm to correctly classify them into categories. Using the Librosa python library we can extract many unique features from each audio sample. 

The most useful feature we can extract from these audio files are the [Mel Frequency Cepstrum Coefficients](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum), a set of coefficients meant to describe an audio wave. As you can see from the following charts, these coefficients can vary widely by instrument, giving us good separation to work into our algorithm. 

<img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/mfcc3_inst.png?raw=true"/>

<img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/mfcc8_inst.png?raw=true"/>

Other features we can extract using Librosa are spectral values such as bandwidths and centroids, as well as the [chroma values](https://en.wikipedia.org/wiki/Chroma_feature) for each clip. Each chroma value relates to one of the twelve pitch (or note) classes found in western music. The following chart shows the different spectral bandwidth ranges for the various instruments we are looking to classify and the separation between them. 

<img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/spec_band.png?raw=true"/>

As for pitch classification, we can look at how the zero-crossing rate for our different samples relates to the spectral centroids, and then use Seaborn’s hue feature to show where the various pitches fall on this scatterplot. As you can see, lower values of the spectral centroid and zero-crossing rates relate to lower pitches, while high values tend to be related to higher pitched notes. 

<img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/cent_zero_cross_scatter.png?raw=true"/>

The following pairplot shows how a number of these features relate to each other as well as how the pitch of each audio clip relates to the various audio features. There appears to be a fair amount of grouping between similar pitch values, suggesting a prediction model may be fairly accurate at determining note values given the provided features. 

<img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/pairplot.png?raw=true"/>

### 2. Model Testing and Evaluation

Now that we have prepared and examined our data, it is time to create some models. The first set of models will be used to create predictions for the instrument being played in the clips. I started with a Logistic Regression model, with a C value of 60 and L1 penalty as our hyperparameters, which were selected using a grid search. Using this model, I was able to receive an accuracy score of 81%, with the best scores coming from vocals and reed instruments. 

<img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/log_class_music.JPG?raw=true"/>

The next model I tested was K Nearest Neighbors. By graphing the error rates for various k values, I was able to determine that error rates increased immediately when more neighbors were considered, and the best value was with k = 1. This led to a model with an accuracy score of 98%. Although this is a much better score than our Logistic model, a value of k=1 may lead to overfitting, so I decided to see if I could repeat these scores with another method.

<img src = "https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/k_val_inst.jpg?raw=true"/>
<img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/class_k_inst.JPG?raw=true"/>

The last model I tested for instrument classification was a Random Forest Classification model. Using the default parameters, I was able to get an accuracy score of 100%, with only 3 of the 1800 test samples being misclassified. 

<img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/class_rand_inst.JPG?raw=true"/>

Next, we will look at models for note classification. Because we are using the same features to classify notes that we used for instruments, I decided that the Random Forest model was the best place to start. Using the default parameters, Random Forest gave us an accuracy score of 92%, with the lowest scores coming from notes on the extreme low and high ends of the spectrum. By doing a grid search, I found the hyperparameters that best fit our data are a max depth of 25 and number of estimators set to 150. These parameters give us an accuracy of 93%. 

### Random Forest with Default Values
<img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/rand_note_default.JPG?raw=true"/>

### Random Forest: Max Depth 25, N Estimators 150
<img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/rand_note_param.JPG?raw=true"/>

Now that we are able to predict the notes and instrument of an audio file, we can use this information to plot notes on a staff to create sheet music from our audio samples. I created a simple plot to showcase one of the uses of our algorithm, with the lines representing lines on a sheet music staff. Combined with a note separating algorithm and a bit of front-end design, these models could be very useful in creating sheet music for a variety of songs and instruments!

<img src="https://github.com/ksivitz/ksivitz.github.io/blob/ebc75764e30570dd709c10f43f48623710aaac96/images/staff.jpg?raw=true"/>



Below is the notebook containing the full workup of this project

[Note and Instrument Classification](https://ksivitz.github.io/note_class.html)
