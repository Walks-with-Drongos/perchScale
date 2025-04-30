# This is a spike that shows how to set directory to run exectuable python script
import sys
import glob

dir = sys.argv[1]
#lists .remove or .pop with index
#python addBox.py "D:\UCT Hot birds\Field work\2024\Whitney Fourie\Perch scale data\GA11"

filenames = glob.glob(dir+ "/**/*.txt")
print(filenames)

