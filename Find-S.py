def find_s(examples):
    '''
    Implements my interpretation of the Find-S algorithm, Chapter 2, page 26 in the 1997 International Edition
    Rather than passing in definitions of the examples, possible options, etc. it attempts to infer them from the training set.
    The one assumption is that the examples are all list-like objects of the same length.
    The format of the examples is (target value, [list of attributes]), where the target value is True or False
    It will output the most specific consistent hypothesis, with each attribute being in [None, single value from examples, set of values from examples]
    '''
    # length of the hypothesis
    hyp_length = len(examples[0][1])
    # initialize to the most specific hypothesis
    h = [] 
    for i in range(hyp_length):
        h.append([])
    positive_instances = [x[1] for x in  examples if x[0]]
    for x in positive_instances:
        for i in range(len(h)):
            if x[i] not in h[i]:
                h[i].append(x[i])

    return h

def enjoy_sport():
    examples = [
                (True, ['sunny', 'warm', 'normal', 'strong', 'warm', 'same']),    
                (True, ['sunny', 'warm', 'high', 'strong', 'warm', 'same']),    
                (False, ['rainy', 'cold', 'high', 'strong', 'warm', 'change']),    
                (True, ['sunny', 'warm', 'high', 'strong', 'cool', 'change'])
               ]
    print find_s(examples)



if __name__ == "__main__":
    enjoy_sport()
    
