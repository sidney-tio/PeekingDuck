"""
Copyright 2021 AI Singapore

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import pytest
import numpy as np
import numpy.testing as npt
from peekingduck.pipeline.nodes.model.hrnetv1.hrnet_files.preprocessing \
    import project_bbox, box2cs, crop_and_resize


@pytest.fixture
def projected_bbox_arr():
    return np.array([[359.5, 239.5, 143.8, 95.8],
                     [0.0, 239.5, 719, 95.8],
                     [359.5, 0.0, 143.8, 479.0]])


class TestPreprocessing:
    def test_project_bbox(self, projected_bbox_arr):
        test_arr = np.array([[0.5, 0.5, 0.7, 0.7],
                             [-0.5, 0.5, 1.5, 0.7],
                             [0.5, -0.5, 0.7, 1.5]])
        test_size = (720, 480)
        output_arr = project_bbox(test_arr, test_size)

        npt.assert_almost_equal(output_arr, projected_bbox_arr)

    def test_box2cs(self, projected_bbox_arr):
        test_arr = projected_bbox_arr
        test_aspect_ratio = 1280/720
        actual_output = box2cs(test_arr, test_aspect_ratio)

        expected_output = np.array([[431.4, 287.4, 170.31111111,  95.8],
                                    [359.5, 287.4, 719., 404.4375],
                                    [431.4, 239.5, 851.55555556, 479.]])

        npt.assert_almost_equal(actual_output, expected_output)

    def test_crop_and_resize(self):
        pass