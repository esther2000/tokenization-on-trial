import re
from collections import defaultdict
from tqdm import tqdm


def get_enum_lines(lines, patterns):
    """Retrieve a dictionary of human-aligned legal text through aligning enumeration markers."""
    enum_lines = defaultdict(list)
    for line in lines:
        if len(line) > 12:
            splits = re.split("("+patterns+")", line)[1:]
            if splits:
                for item in splits:
                    if splits.index(item) % 2 == 0 and len(item) < 10:  # enum
                        line = splits[splits.index(item)+1]
                        if len(line) > 20:  # crude filter
                            item = item.replace("Stk.", "Imm.")  # for matching later
                            enum_lines[item].append(line.strip().replace("\xa0", "").replace("\u00ad", ""))

    if enum_lines:
        return enum_lines


def main():

    # define structural markers
    enum_pat_da = "§\s+[0-9]{1,}[.]|Stk.\s+[0-9]{1,}|[0-9]{1,}[)]|^[abcdefghijk]{1,}[)]"
    enum_pat_gl = "§\s+[0-9]{1,}[.]|Imm.\s+[0-9]{1,}|[0-9]{1,}[)]|^[abcdefghijk]{1,}[)]"

    for i in tqdm(range(10, 2545)):  # note: first 10 contain DA in GL; skip
        # retrieve lines
        with open(f"raw_text/da/{i}.da") as da_infile:
            da_lines = [line.strip() for line in da_infile.readlines()]
        with open(f"raw_text/gl/{i}.gl") as gl_infile:
            gl_lines = [line.strip() for line in gl_infile.readlines()]

        # retrieve dicts with enumerated lines per doc
        da_dict = get_enum_lines(da_lines, enum_pat_da)
        gl_dict = get_enum_lines(gl_lines, enum_pat_gl)

        # get parallel text
        da_par, gl_par = [], []
        if da_dict and gl_dict:
            matched_keys = set(list(da_dict.keys())+list(gl_dict.keys()))
            for k in matched_keys:
                if len(da_dict[k]) == len(gl_dict[k]):
                    for da_line, gl_line in zip(da_dict[k], gl_dict[k]):
                        if da_line != gl_line and \
                                not (da_line.startswith("[") or gl_line.startswith("[")) and not "....." in da_line:
                            da_par.append(da_line)
                            gl_par.append(gl_line)

        # write to outfiles
        with open("da_lines.txt", "a") as da_outfile:
            for line in da_par:
                if line.startswith("."):  # hacky last-minute cleaning
                    line = line[1:]
                da_outfile.write(f"{line.strip()}\n")

        with open("gl_lines.txt", "a") as gl_outfile:
            for line in gl_par:
                if line.startswith("."):  # hacky last-minute cleaning
                    line = line[1:]
                gl_outfile.write(f"{line.strip()}\n")


if __name__ == "__main__":
    main()
