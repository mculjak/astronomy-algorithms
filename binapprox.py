# Implementation of binapprox algorithm for efficient approximate median calculation

import numpy as np

def median_bins(values, num_bins):
  a = np.array(values)
  mean = np.mean(a)
  std_dev = np.std(a)
  bin_counts = np.zeros(num_bins)
  minval = mean - std_dev
  maxval = mean + std_dev
  width = 2*std_dev/num_bins
  ignore_bin_count = 0
  for val in values:
    if val < minval:
      ignore_bin_count += 1
    elif val < maxval:
      bin = int((val - minval)/width)
      bin_counts[bin] += 1
  return (mean, std_dev, ignore_bin_count, bin_counts)

def median_approx(values, num_bins):
  (mean, std_dev, ignore_bin_count, bin_counts) = median_bins(values, num_bins)
  sum = ignore_bin_count
  for i in range(len(bin_counts)):
    sum += bin_counts[i]
    if sum >= (len(values)+1)/2:
      break
      
  width = 2*std_dev/num_bins
  lower = i*width + (mean - std_dev)
  median = lower + width/2
  return median


