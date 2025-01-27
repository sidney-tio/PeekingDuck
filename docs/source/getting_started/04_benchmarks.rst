*******************
CV Model Benchmarks
*******************

At PeekingDuck, we aim to give users as much flexibility as possible to cater to every possible use case.
From real-time object detection to high-accuracy pose estimation, PeekingDuck houses a wide range of models.
The full list of models can be found :mod:`here <peekingduck.pipeline.nodes.model>`.


In this document, we provide a summary of the model performance and FPS based on our own tests, and careful curation of the test conditions.
The purpose of these benchmarks is to allow users to have a quick understanding on the relative performance of each model, thereby enabling
users to decide on the model most suited for their use case.

However, this document is **NOT** a guaratee of performance for your own use case, as there are many variables that may affect performance.

Testing conditions
==================

Matrix-Multiplication
---------------------

Single target human object detection
-------------------------------------

Multiple target human object detection
-------------------------------------

COCO Eval (mAP)
-------------------------------------




Benchmarks
==========


FPS Benchmarks
--------------


+---------------+--------------+--------+-----------+-------------+--------+----------+--------+----------+--------+----------+-----------+--------------+
|               |              | matmul | posenet (mobilenet 101) | posenet (resnet)  | yolo (v4tiny)     | yolo (v4)         | yolo#hrnet (v4tiny, w48) |
+---------------+--------------+--------+------------+------------+--------+----------+--------+----------+--------+----------+-----------+--------------+
| Device Class  | No. of humans|        | single     | multiple   | single | multiple | single | multiple | single | multiple | single    | multiple     |
|               | in video     |        |            |            |        |          |        |          |        |          |           |              |
+===============+==============+========+============+============+========+==========+========+==========+========+==========+===========+==============+
|               |              |        |            |            |        |          |        |          |        |          |           |              |
+---------------+--------------+--------+------------+------------+--------+----------+--------+----------+--------+----------+-----------+--------------+
|               |              |        |            |            |        |          |        |          |        |          |           |              |
+---------------+--------------+--------+------------+------------+--------+----------+--------+----------+--------+----------+-----------+--------------+
|               |              |        |            |            |        |          |        |          |        |          |           |              |
+---------------+--------------+--------+------------+------------+--------+----------+--------+----------+--------+----------+-----------+--------------+
|               |              |        |            |            |        |          |        |          |        |          |           |              |
+---------------+--------------+--------+------------+------------+--------+----------+--------+----------+--------+----------+-----------+--------------+
|               |              |        |            |            |        |          |        |          |        |          |           |              |
+---------------+--------------+--------+------------+------------+--------+----------+--------+----------+--------+----------+-----------+--------------+
|               |              |        |            |            |        |          |        |          |        |          |           |              |
+---------------+--------------+--------+------------+------------+--------+----------+--------+----------+--------+----------+-----------+--------------+
|               |              |        |            |            |        |          |        |          |        |          |           |              |
+---------------+--------------+--------+------------+------------+--------+----------+--------+----------+--------+----------+-----------+--------------+


mAP Benchmarks
--------------


+---------------+---------------+----------+------------+------------------------------+-------------------------+
| model         | AP (0.5:0.95) | AP (0.5) | AP (0.75)  | AP (0.5:0.95), Single person | AP (0.5:0.95), multiple |
+===============+===============+=======================+==============================+=========================+
|               |               |          |            |                              |                         |
+---------------+---------------+----------+------------+------------------------------+-------------------------+
|               |               |          |            |                              |                         |
+---------------+---------------+----------+------------+------------------------------+-------------------------+
|               |               |          |            |                              |                         |
+---------------+---------------+----------+------------+------------------------------+-------------------------+
|               |               |          |            |                              |                         |
+---------------+---------------+----------+------------+------------------------------+-------------------------+
|               |               |          |            |                              |                         |
+---------------+---------------+----------+------------+------------------------------+-------------------------+