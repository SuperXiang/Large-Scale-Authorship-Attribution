####################################################################################################################################################
#
# The script aims to get detailed information of datasets. 
#
# Environment Requirement: Python 3.5, Anaconda3
# Date of Last Modified: 06/19/2020
# Author: Yingfei(Jeremy) Xiang
#
####################################################################################################################################################

import os, sys, glob
import numpy as np
import nltk

def main(argv):
  in_path = argv[0]
  outfile = argv[1]

  dirs = os.listdir(in_path)

  num_auth = 0
  num_samples = 0
  samples_per_subj = []
  sample_len_char = []
  sample_len_word = []
  sample_len_sent = []
  
  # Collect statistics from all folders and files
  for dirname in dirs:
    if dirname.endswith('.txt'):
      continue
    num_auth += 1
    full_dirname = in_path + '/' + dirname  
    files = glob.glob(full_dirname + '/*.txt')
    numfiles = len(files)
    num_samples += numfiles
    samples_per_subj.append(numfiles)
    for fname in files:
      with open(os.path.join(full_dirname,fname),'r') as fp:
        text = fp.read()
        sample_len_char.append(len(text))
        words = nltk.tokenize.word_tokenize(text)
        sample_len_word.append(len(words))
        sents = nltk.sent_tokenize(text)
        sample_len_sent.append(len(sents))

  # Convert list to array
  arr_samples_per_subj = np.array(samples_per_subj)
  arr_sample_len_char = np.array(sample_len_char)
  arr_sample_len_word = np.array(sample_len_word)
  arr_sample_len_sent = np.array(sample_len_sent)

  # Compute statistics
  avg_samples_per_subj = int(np.mean(arr_samples_per_subj))
  avg_sample_len_char = int(np.mean(arr_sample_len_char))
  avg_sample_len_word = int(np.mean(arr_sample_len_word))
  avg_sample_len_sent = int(np.mean(arr_sample_len_sent))
  std_samples_per_subj = int(np.std(arr_samples_per_subj))
  std_sample_len_char = int(np.std(arr_sample_len_char))
  std_sample_len_word = int(np.std(arr_sample_len_word))
  std_sample_len_sent = int(np.std(arr_sample_len_sent))

  # Write statistics to file
  with open(outfile,'w') as f:
    f.write('#authors = ' + str(num_auth) + '\n')
    f.write('#samples = ' + str(num_samples) + '\n')
    f.write('#samples/author = ' + str(avg_samples_per_subj) + ' +/- ' + str(std_samples_per_subj) + '\n')
    f.write('samples length in characters = ' + str(avg_sample_len_char) + ' +/- ' + str(std_sample_len_char) + '\n')
    f.write('samples length in words = ' + str(avg_sample_len_word) + ' +/- ' + str(std_sample_len_word) + '\n')
    f.write('samples length in sentences = ' + str(avg_sample_len_sent) + ' +/- ' + str(std_sample_len_sent) + '\n')
        
if __name__ == "__main__":
  main(sys.argv[1:])

