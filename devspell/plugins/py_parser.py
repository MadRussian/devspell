from lang_parser import LangParser
from lang_parser import Section
import tokenize
import token
import os

PARSE_TYPES = [
  tokenize.STRING,
  tokenize.COMMENT,
]

class PyParser(LangParser):

  def parse(self):
    """This uses tokenize to parse the content"""
    if not self.path:
      return
    if not os.path.exists(self.path):
      return
    with open(self.path, 'r') as fp:
      token_gen = tokenize.generate_tokens(fp.readline)
      for ttype, tok, start, end, line in token_gen:
        if ttype not in PARSE_TYPES:
          continue
        srow, scol = start
        erow, ecol = end

        if ttype == tokenize.COMMENT:
          # Ignore shebang
          if tok.find("#!/") == 0:
            continue

        # Strip based on the first char
        tok = tok.strip(tok[0])

        lines = tok.split('\n')
        line_ix = 0
        for data in lines:
          item = Section(self, data.strip())
          item.line = srow + line_ix
          self.sections.sections.append(item)
          line_ix += 1
