from langchain_core.runnables import RunnableLambda

counter = -1

def func(x):
    global counter
    counter += 1
    print(counter)
    return x


chain = RunnableLambda(func).with_retry(stop_after_attempt=3)

resp = chain.invoke(2)

print(resp)