import random
from tqdm import tqdm
import os

random.seed(0)
TEST_SIZE=1000
VALID_SIZE=1000

# open files
with open("da_lines.txt", "r") as da_file:
    da_lines = [line.strip() for line in da_file.readlines()]
with open("gl_lines.txt", "r") as gl_file:
    gl_lines = [line.strip() for line in gl_file.readlines()]

# deduplication
un_da, un_gl = [], []
for da, gl in zip(tqdm(da_lines), gl_lines):
    if da not in un_da and gl not in un_gl:
        un_da.append(da)
        un_gl.append(gl)

# shuffle
par = list(zip(un_da, un_gl))
random.shuffle(par)
da_shuf, gl_shuf = zip(*par)

# split
test_da = da_shuf[:TEST_SIZE]
test_gl = gl_shuf[:TEST_SIZE]
valid_da = da_shuf[TEST_SIZE:TEST_SIZE+VALID_SIZE]
valid_gl = gl_shuf[TEST_SIZE:TEST_SIZE+VALID_SIZE]
train_da = da_shuf[TEST_SIZE+VALID_SIZE:]
train_gl = gl_shuf[TEST_SIZE+VALID_SIZE:]

# write to files
os.mkdir("cleaned")

# test
with open("cleaned/test.da", "w") as da_test_f:
    for line in test_da:
        da_test_f.write(f"{line.strip()}\n")
with open("cleaned/test.gl", "w") as gl_test_f:
    for line in test_gl:
        gl_test_f.write(f"{line.strip()}\n")

# valid
with open("cleaned/valid.da", "w") as da_valid_f:
    for line in valid_da:
        da_valid_f.write(f"{line.strip()}\n")
with open("cleaned/valid.gl", "w") as gl_valid_f:
    for line in valid_gl:
        gl_valid_f.write(f"{line.strip()}\n")

# train
with open("cleaned/train.da", "w") as da_train_f:
    for line in train_da:
        da_train_f.write(f"{line.strip()}\n")
with open("cleaned/train.gl", "w") as gl_train_f:
    for line in train_gl:
        gl_train_f.write(f"{line.strip()}\n")
