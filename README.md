# skeleton_tool_cmd

## Usage:
Navigate to the sklt.py file

### Command
python sklt.py [-h] input thresh prune out <br/>

input : path + name of input image <br/>
thresh : segmentation threshold in percentage (0 - 100) <br />
prune : pruning threshold in percentage (0 - 100) <br />
out : path + name of output file <br />

### Example

skeleton_tool_cmd\skeleton_plugin> python sklt.py imgs/32test.png 10 5 ./outs/32test.ply
