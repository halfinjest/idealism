import math
import sys

def get_randomness(ideal, real):
	return math.log(2 - abs(1 - real / ideal), 2)

def get_transitions(bitstring):
	transitions = 0

	for i in range(len(bitstring) - 1):
		transitions += int(bitstring[i] != bitstring[i + 1])

	return transitions

def get_formatted_bitstring(bitstring, number):
	if number > 1:
		bitstring_ = ""

		segments = len(bitstring) / number

		for i in range(number):
			for j in range(segments):
				bitstring_ += bitstring[number * j + i]

		return bitstring_ + bitstring[number * segments:]

	return bitstring

def main():
	bitstring = "0101010001101000011010010111001100100000011010010111001100100000011000010110111000100000011001010110111001100011011011110110010001100101011001000010000001000001010100110100001101001001010010010010000001110011011101000111001001101001011011100110011100101110"

	options = []

	for i in range(1, len(bitstring) / 2):
		bitstring_ = get_formatted_bitstring(bitstring, i)

		options.append(get_randomness((len(bitstring_) - 1) / 2.0, get_transitions(bitstring_)))

	sys.stdout.write(str(min(options)) + "\n")

if __name__ == "__main__":
	try:
		main()

	except KeyboardInterrupt:
		sys.stdout.write("\nInterrupted.\n")