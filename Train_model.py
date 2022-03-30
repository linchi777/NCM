from snownlp import sentiment

print('正在训练新模型：')
sentiment.train('C:\\Users\\Administratior\\Desktop\\ncm\\neg.txt','C:\\Users\\Administratior\\Desktop\\ncm\\pos.txt')
sentiment.save('C:\\Users\\Administratior\\Desktop\\ncm\\ncm.marshal')
print('训练完成！')