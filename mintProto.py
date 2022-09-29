import subprocess
from pprint import pprint
import json
from bitmath import *

filename = "/Users/edrihan/Documents/python/07. It's Your Thing-Christian McBride.flac"
result = subprocess.check_output(['ffprobe', '-show_format', '-of',
'json', filename])
result2 = subprocess.check_output(['ffprobe', '-show_streams', '-of',
'json', filename])



result2 = json.loads(result2)
result = json.loads(result)


used_keys = ('filename','format_name','tags','bit_rate')
for stream in result2['streams']:
    if stream['codec_type'] != 'audio':
        continue
    
    result2 = stream
    
    break # will only find one (stereo) stream
bit_depth = stream['bits_per_raw_sample']
bit_rate = result['format']['bit_rate']
bit_rate_printable = Byte(int(bit_rate)).to_KiB()




print('Bitrate of {} is: \n{}-bit {}/s {} {}.'.format(
    filename,
    bit_depth,
    bit_rate_printable,
    'mono' if result2['channels'] == '0' else 'stereo',
    result['format']['format_name']))


