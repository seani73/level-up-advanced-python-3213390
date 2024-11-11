def pairwise_offset(sequence, fillvalue='*', offset=0):
    outputList = []
    seqLength = len(sequence)

    if offset == 0:
        for item in sequence:
            outputList.append((item, item))
    elif offset > 0 and offset < seqLength:
        pos = 0
        for i in range(offset):
            outputList.append(sequence[i], fillvalue)
            pos += 1
        for i in range(seqLength - offset):
            outputList.append(sequence[i], sequence[pos-offset])
            pos += 1
        for i in range(offset):
            outputList.append(fillvalue, sequence[i])
    elif offset == seqLength:
        for i in range(seqLength):
            outputList.append(sequence[i], fillvalue)
        for i in range(seqLength):
            outputList.append(fillvalue, sequence[i])
    elif offset > seqLength:
        for i in range(seqLength):
            outputList.append(sequence[i], fillvalue)
        for i in range(offset - seqLength):
            outputList.append(fillvalue, fillvalue)
        for i in range(seqLength):
            outputList.append(fillvalue, sequence[i])


    return None

print(pairwise_offset(['a', 'b', 'c']))
