## Note and Instrument Identification

### Project description:

For this project my focus was to create a model that can take a wav file of a instrument being played and identify what instrument it is and what note is peing played on that instrument. This ideal application of this model would be to help create sheet music for a song from a recording. 

### 1. The Data

Magenta has created a audio dataset called the [NSynth Dataset](https://magenta.tensorflow.org/datasets/nsynth#note-qualities), aimed at giving data scientists an entrypoint into the field of audio machine learning. This dataset contains a 4 second audio clip for various instruments and notes found on a standard MIDI 0-scale. each sample comes pre-classified with the pitch of the note and instrument being played. Using this data we can extract information from the audio sample and create various supervised machine learning algorithms to idenify the note and instrument. This dataset contains over 300,000 classified audio samples, ho due to computation constraints we will be working with a subset of roughly 12,600 of these samples. 

### 2. Assess assumptions on which statistical inference will be based

Using the Librosa python library we can extract a number of useful features from each audio sample such as spectral length, harmonics, croma frequencies, and other unique identifiers of each note and instrument. 
<center>
<img src="images/guitar_bass_spec.png?raw=true"/>

<img src="images/mallet_keyboard_spec.png?raw=true"/>
</center>




### 3. Support the selection of appropriate statistical tools and techniques

<img src="images/spec_band.png?raw=true"/>

<img src="images/mfcc3_inst.png?raw=true"/>

<img src="images/mfcc8_inst.png?raw=true"/>

<img src="images/pairplot.png?raw=true"/>

### 4. Provide a basis for further data collection through surveys or experiments

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).
