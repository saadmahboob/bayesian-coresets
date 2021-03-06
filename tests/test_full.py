import bayesiancoresets as bc
import numpy as np


np.random.seed(1)


def test_empty():
  x = np.zeros((0, 0))
  fd = bc.FullDataset(x)
  assert fd.error() == 0, "full wts failed: error not 0"
  assert np.all(fd.weights() == np.ones(x.shape[0])), "full wts failed: weights not ones"
  for m in [0, 1, 10]:
    fd.run(m)
    assert fd.error() == 0, "full wts failed: error not 0"
    assert np.all(fd.weights() == np.ones(x.shape[0])), "full wts failed: weights not ones"


def test_one():
  x = np.zeros((1, 3))
  fd = bc.FullDataset(x)
  assert fd.error() == 0, "full wts failed: error not 0"
  assert np.all(fd.weights() == np.ones(x.shape[0])), "full wts failed: weights not ones"
  for m in [0, 1, 10]:
    fd.run(m)
    assert fd.error() == 0, "full wts failed: error not 0"
    assert np.all(fd.weights() == np.ones(x.shape[0])), "full wts failed: weights not ones"

def test_many():
  x = np.zeros((10, 3))
  fd = bc.FullDataset(x)
  assert fd.error() == 0, "full wts failed: error not 0"
  assert np.all(fd.weights() == np.ones(x.shape[0])), "full wts failed: weights not ones"
  for m in [0, 1, 10]:
    fd.run(m)
    assert fd.error() == 0, "full wts failed: error not 0"
    assert np.all(fd.weights() == np.ones(x.shape[0])), "full wts failed: weights not ones"

