from src.generator import Generator
import sys

filename = sys.argv[1]
gen = Generator(filename)
print(gen.gen_sentence())
