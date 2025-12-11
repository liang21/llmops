import dotenv
import numpy as np
from langchain_community.embeddings import OpenAIEmbeddings
from numpy.linalg import norm

dotenv.load_dotenv()


def cosine_similarity(vec1: list, vec2: list) -> float:
    # 计算两个向量的点积
    np_dot = np.dot(vec1, vec2)
    # 计算向量的长度
    vec1_norm = norm(vec1)
    vec2_norm = norm(vec2)

    # 计算余弦相似度
    return np_dot / (vec1_norm * vec2_norm)


embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

embed_query = embeddings.embed_query("我叫幕小课,我喜欢打篮球")

print(embed_query)
print(len(embed_query))

embed_documents = embeddings.embed_documents(
    ["我叫慕小课，我喜欢打篮球", "这个喜欢打篮球的人叫慕小课", "求知若渴，虚心若愚"])
print(len(embed_documents))

# 4.计算余弦相似度
print("向量1和向量2的相似度:", cosine_similarity(embed_documents[0], embed_documents[1]))
print("向量1和向量3的相似度:", cosine_similarity(embed_documents[0], embed_documents[2]))
