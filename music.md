## Note and Instrument Identification

### Project description:

For this project my focus was to create a model that can take an audio wav file of a instrument being played and identify what instrument it is and what note is being played on that instrument. The ideal application of this model would be to assist in creating sheet music from a recording. 

### 1. The Data

Magenta has created a audio dataset called the [NSynth Dataset](https://magenta.tensorflow.org/datasets/nsynth#note-qualities), aimed at giving data scientists an entrypoint into the field of audio machine learning. This dataset contains 4 second audio clips of various instruments playing notes found on a standard MIDI 0-scale. Each sample comes pre-classified with the pitch of the note and name of the instrument being played. Using this data we can extract information from the audio sample and create various supervised machine learning algorithms to idenify the note and instrument. The full dataset contains over 300,000 classified audio samples, however due to computation constraints we will be working with a subset of roughly 12,600 of these samples. 

### 2. Assess assumptions on which statistical inference will be based

As we can see from the Spectrograms (graphs that display the amplitudes of the frequency components of an audio signal over time) of a selection of samples from the data, frequencies can vary greatly by instrument and the pitch of the sound being played. Higher notes result in higher frequencies being emitted, and each instrument emits a unique combination of frequencies at various amplitutes(loudness) that combine to make up the note being played.

<center><img src="images/guitar_bass_spec.png?raw=true"/></center>

<center><img src="images/mallet_keyboard_spec.png?raw=true"/></center>

There are a number of quantifiable metrics we can pull from these audio files that can help train our algorithim to correctly classify these various audio signals into categories. Using the Librosa python library we can extract many useful features from each audio sample. 

The most useful feature we can extract from these audio files are the [Mel Frequency Cepstrum Coefficients](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum), a set of coefficents ment to describe audio wave. As you can see from the following charts, these coefficents can vary widely by instrument, giving us good seperation to work into our algorithm. 

<img src="images/mfcc3_inst.png?raw=true"/>

<img src="images/mfcc8_inst.png?raw=true"/>

Other features we can extract using librosa are spectral values such as bandwidths and centroids, as well as the [chroma values](https://en.wikipedia.org/wiki/Chroma_feature) for each clip, each relating to one of the twelve pitch (or note) classes found in music. The following chart shows the different spectral bandwdith ranges for the various instruments we are looking to classify and the seperations between them. 

<img src="images/spec_band.png?raw=true"/>

As for pitch classification, we can look at how the zero-crossing rate for our differnt samples relates to the spectral centroids, and then use seaborns hue feature to show where the various pitches fall on this scatterplot. as you can see, lower values of the spectral centroid and zero-crossing rates relate to lower pitches, while high values tend to be related to higher pitched notes. 

<im src="zero_cross.jpg?raw=true"/>

The following pairplot shows how a number of these features relate to each other as well as how the pitch of each audio clip relates to the various audio features. There appears to be a fair amount of grouping between similar pitch values, suggesting a prediction model may be fairly accurate at determining note values given the provided features. 

<img src="images/pairplot.png?raw=true"/>

### 3. Support the selection of appropriate statistical tools and techniques

Now that we have prepared and examined our data, it is time to create some models.



### 4. Provide a basis for further data collection through surveys or experiments



For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).
