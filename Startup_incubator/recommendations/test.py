from gensim.models import Word2Vec
import numpy 


def avg_sentence_vector(words, model):
    num_features = 150
    #function to average all words vectors in a given paragraph
    featureVec = numpy.zeros((num_features,), dtype="float32")
    nwords = 0

    for word in words:
        if word in model.wv.vocab:
            nwords = nwords+1
            featureVec = numpy.add(featureVec, model[word])

    if nwords>0:
        featureVec = numpy.divide(featureVec, nwords)
    return featureVec
    


def predict(investors,startup):
    model = Word2Vec.load("word2vec.model")
    f1 = avg_sentence_vector(startup.split(),model)
    for investor in investors:
        f2 = avg_sentence_vector(investor[1].split(),model)
        cosine_similarity = numpy.dot(f1,f2)/(numpy.linalg.norm(f1)* numpy.linalg.norm(f2))
        print(investor[0]," : ",cosine_similarity)
