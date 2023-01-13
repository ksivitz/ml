## Note and Instrument Identification

### Project description:

For this project my focus was to create a model that can take an audio wav file of a instrument being played and identify what instrument it is and what note is being played on that instrument. The ideal application of this model would be to assist create sheet music for a song from a recording. 

### 1. The Data

Magenta has created a audio dataset called the [NSynth Dataset](https://magenta.tensorflow.org/datasets/nsynth#note-qualities), aimed at giving data scientists an entrypoint into the field of audio machine learning. This dataset contains 4 second audio clips of various instruments playing notes found on a standard MIDI 0-scale. Each sample comes pre-classified with the pitch of the note and instrument being played. Using this data we can extract information from the audio sample and create various supervised machine learning algorithms to idenify the note and instrument. The full dataset contains over 300,000 classified audio samples, however due to computation constraints we will be working with a subset of roughly 12,600 of these samples. 

### 2. Assess assumptions on which statistical inference will be based

As we can see from the Spectrograms (graphs that display the amplitudes of the frequency components of an audio signal over time) of a selection of samples from the data, frequencies can vary greatly by instrument and the pitch of the sound being played. Higher notes result in higher frequencies being emitted, and each instrument emits a unique combination of frequencies at various amplitutes(loudness) that combine to make up the note being played.

<center><img src="images/guitar_bass_spec.png?raw=true"/></center>

<center><img src="images/mallet_keyboard_spec.png?raw=true"/></center>

There are a number of quantifiable metrics we can pull from these audio files that can help train our algorithim to correctly classify these various audio signals into categories. Using the Librosa python library we can extract many useful features from each audio sample. 

fAudio Signals can be best described in wave form, with the 

### 3. Support the selection of appropriate statistical tools and techniques

<img src="images/spec_band.png?raw=true"/>

<img src="images/mfcc3_inst.png?raw=true"/>

<img src="images/mfcc8_inst.png?raw=true"/>

<img src="images/pairplot.png?raw=true"/>

### 4. Provide a basis for further data collection through surveys or experiments

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).
