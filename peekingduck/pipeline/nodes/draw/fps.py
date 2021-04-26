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

from typing import Any, Dict
from time import perf_counter

from peekingduck.pipeline.nodes.node import AbstractNode
from .utils.drawfunctions import draw_fps

class Node(AbstractNode):
    """ FPS node class that calculates the FPS and draw the FPS onto the image
    frame
    """
    def __init__(self, config: Dict) -> None:
        super().__init__(config, node_path=__name__)

        self.current_frame_time = 0
        self.previous_frame_time = 0

    def run(self, inputs: Dict[str, Any]) -> None:
        """ Calculates FPS using the time difference between the current frame
        and the previous frame. Calculated FPS is then draw onto image frame

        Args:
            inputs: ["img"]

        Returns:
            outputs: [None]
        """

        self.current_frame_time = perf_counter()
        current_fps = 1 / (self.current_frame_time - self.previous_frame_time)
        self.previous_frame_time = self.current_frame_time
        draw_fps(inputs[self.inputs[0]], current_fps)

        return {}


