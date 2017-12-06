import math
import sys

def get_idealism(transitions, ideal):
	return math.log(2 - abs(1 - transitions / ideal), 2)

def get_transitions(bitstring):
	transitions = ""

	for i in range(len(bitstring) - 1):
		transitions += str(int(bitstring[i] != bitstring[i + 1]))

	return transitions

def get_formatted_bitstring(bitstring, number):
	if number > 1:
		formatted_bitstring = ""

		for i in range(number):
			for j in range(len(bitstring) / number):
				formatted_bitstring += bitstring[number * j + i]

		bitstring = formatted_bitstring + bitstring[len(bitstring) - len(bitstring) % number:]

	return bitstring 

def main():
	bitstring = "0101010001101000011010010111001100100000011010010111001100100000011000010110111000100000011001010110111001100011011011110110010001100101011001000010000001000001010100110100001101001001010010010010000001110011011101000111001001101001011011100110011100101110"

	options = []

	for i in range(len(bitstring) / 2):
		formatted_bitstring = get_formatted_bitstring(bitstring, i + 1)

		ideal = (len(formatted_bitstring) - 1) / 2.0

		options.append(get_idealism(sum(int(bit) for bit in get_transitions(formatted_bitstring)), ideal))

	sys.stdout.write(str(min(options)) + "\n")

if __name__ == "__main__":
	try:
		main()

	except KeyboardInterrupt:
		sys.stdout.write("\nInterrupted.\n")