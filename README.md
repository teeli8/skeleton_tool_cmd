# skeleton_tool_cmd

## Usage:
Navigate to the sklt.py file

### Command
python sklt.py [-h] input thresh prune out \n

input : path + name of input image \n
thresh : segmentation threshold in percentage (0 - 100) \n
prune : pruning threshold in percentage (0 - 100) \n
out : path + name of output file \n

### Example

skeleton_tool_cmd\skeleton_plugin> python sklt.py imgs/32test.png 10 5 ./outs/32test.ply
