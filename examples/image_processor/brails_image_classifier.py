# Copyright (c) 2024 The Regents of the University of California
#
# This file is part of BRAILS++.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# You should have received a copy of the BSD 3-Clause License along with
# BRAILS++. If not, see <http://www.opensource.org/licenses/>.
#
# Contributors:
# Frank McKenna
# Barbaros Cetiner
#
# Last updated:
# 11-06-2024

"""
Example demonstrating use of aerial and street-level image classifiers.

 Purpose: Testing 1) get_class method of Importer
                  2) set_directory and print_info methods of ImageSet objects
                  3) predict methods of RoofShapeClassifier,
                     OccupancyClassifier, and NFloorVLM
"""

from brails.types.image_set import ImageSet
from brails import Importer

importer = Importer()
aerial_images = ImageSet()
aerial_images.set_directory("./images/satellite_easy", True)
street_images = ImageSet()
street_images.set_directory("./images/street", True)

# Test importer using a couple of the aerial imagery classifiers:
aerial_images.print_info()
print('ROOF SHAPE PREDICTIONS USING MODEL TRAINED ON CUSTOM DATASET:')
my_class = importer.get_class('RoofShapeClassifier')
my_classifier = my_class()
predictions = my_classifier.predict(aerial_images)
print(predictions)

# Test importer and a couple of the street-level imagery classifiers:
street_images.print_info()
print('\nOCCUPANCY CLASS PREDICTIONS USING MODEL TRAINED ON CUSTOM DATASET:')
my_class = importer.get_class('OccupancyClassifier')
my_classifier = my_class()
predictions = my_classifier.predict(street_images)
print(predictions)

print('\nNUMBER OF FLOOR PREDICTIONS USING CLIP VLM:')
my_class = importer.get_class('NFloorVLM')
my_classifier = my_class()
predictions = my_classifier.predict(street_images)
print(predictions)
