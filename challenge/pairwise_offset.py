def pairwise_offset(sequence, fillvalue='*', offset=0):
    outputList = []
    seqLength = len(sequence)
    i = 0

    if offset == 0:
        for item in sequence:
            outputList.append((item, item))
    else:
        for item in sequence:
            if i <= offset:
                outputList.append((item, fillvalue))
                i += 1
            else:
                outputList.append()
                #Need to know the length of the sequence and the offset to know how many there well be
                #to know if there will be (item, item) tuples
                
                #Need to check if 


    return None

print(pairwise_offset(['a', 'b', 'c']))
