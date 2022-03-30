#coding:UTF-8
import sys
from snownlp import SnowNLP

input_file = ('C:\\Users\\Administratior\\Desktop\\ncm\\pos.txt')
output_file = ('C:\\Users\\Administratior\\Desktop\\ncm\\pos_score.txt')

def read_and_analysis(input_file, output_file):
  f = open(input_file)
  fw = open(output_file, "w")
  while True:
    line = f.readline()
    if not line:
      break
    lines = line.strip().split("\t")
    if len(lines) < 2:
      continue

    s = SnowNLP(lines[1].decode('utf-8'))
    # s.sentiments 查询最终的情感分析的得分
    fw.write(lines[0] + "\t" + lines[1] + "\t" + seg_words.encode('utf-8') + "\t" + str(s.sentiments) + "\n")
  fw.close()
  f.close()

if __name__ == "__main__":
  input_file = sys.argv[1]
  output_file = sys.argv[2]
  read_and_analysis(input_file, output_file)