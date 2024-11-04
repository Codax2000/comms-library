# Communcations Library

This is meant to be a Python library that I can deploy to Anaconda for
general use. There are a series of blocks that can be connected and
used together to simulate a variety of communcations systems, assuming
1D or 2D signal space.

## Included blocks
Here is a list of the classes and their methods. Note that these are all
abstract methods and have specific instances 

### `Constellation` class
This class defines a signal constellation in 2D space.

| Function | Purpose |
| :--- | :--- |
| `plot` | Plot the constellation in IQ plane |
| `e_b` | Return the energy per bit of the constellation |
| `d_E` | Return the minimum Euclidean distance between signal vectors |
| `rate` | Return the signal rate in bits per dimension |
| `generate` | Generate a random stream of complex values from the constellation |
| `initiate` | Initiates a signal chain by calling `generate` and passing the resulting data to one or more `Pulse` instances |

### `Pulse` class
This class turns a stream of complex data into time-domain orthonormal waveforms.

| Function | Purpose |
| :--- | :--- |
| `plot` | Plot time and frequency domain signals after modulation |
| `modulate` | Modulate data stream with a pulse shape and store as internal state, also passing data to one or more `Mixer` instances |

### `Mixer` class
This class mixes input data to a carrier frequency.

| Function | Purpose |
| :--- | :--- |
| `mix` | Mix real input data up to a carrier frequency, also passing data to one or more `Channel` instances |
| `plot` | Plot time- and freuquency- domain signals after mixing

### `Channel` class
This class defines how incoming signals are distorted, with AWGN and/or propagation loss.

| Function | Purpose |
| :--- | :--- |
| `plot` | Plot time and frequency domain signals after distortion |
| `distort` | Distort incoming data and pass to one or more `Receiver` instances |

### `Receiver` class
This class mixes an incoming signal down by a carrier frequency

| Function | Purpose |
| :--- | :--- |
| `plot` | Plot time and frequency domain signals after mixing down |
| `mix` | Mix incoming signal down by a carrier frequency and pass to one or more `Filter` classes |

### `Filter` class
This class filters an incoming signal by convolution with a pulse shape

| Function | Purpose |
| :--- | :--- |
| `plot` | Plot time and frequency domain signals after filtering with $ h(t) $ |
| `filter` | Filter incoming data with a pulse and send to one or more `ADC` instances |

### `ADC` class
This class samples an incoming signal

| Function | Purpose |
| :--- | :--- |
| `plot` | Plot time and frequency domain signals after sampling at intervals |
| `sample` | Sample incoming data at regular invervals and send to one or more `Classifier` instances |

### `Classifier` class
This class classifies an incoming signal based on a `Constellation`.

| Function | Purpose |
| :--- | :--- |
| `plot` | Plot received and ideal signals in the IQ plane |
| `classify` | Classify incoming signals based on initializer `Constellation` |
| `calculate_pes` | Return the symbol error probability as a float |
| `calculate_peb` | Return the bit error probability as a float | 

## Target Sample Program
The goal use of this library is illustrated as follows:

```python
# Build receiver from the back to front
# parameters are examples, not real yet
classifier = Classifier('PSK', param=8)
converter = ADC(T, [classifier])
filter = Filter('SRRC', T, [converter])
receiver = Receiver(100e6, [filter])
channel = Channel(N0, [receiver], awgn=True)
mixer = Mixer(100e6, [channel])
srrc_pulse = SRRC(T)
generator = PSK(8)  # Constellation

# generate data in the chain
generator.initiate(1024)
print(f'Probability of Error: {classifier.calculate_pes}')

# plot signals of channel, input data, output data, and received constellation
mixer.plot()
receiver.plot()
classifier.plot()
```