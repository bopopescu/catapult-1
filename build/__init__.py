# Copyright (c) 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
import os
import sys


def _AddToPathIfNeeded(path):
  if path not in sys.path:
    sys.path.insert(0, path)

def _UpdatePathsIfNeeded():
  catapult_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                         '..', '..'))

  _AddToPathIfNeeded(os.path.join(catapult_dir))

_UpdatePathsIfNeeded()